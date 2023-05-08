POETRY ?= poetry
POETRY_CONF ?= ./pyproject.toml
PYTHON ?= python3
PIP ?= pip3
FLAKE8 ?= $(POETRY) run $(PYTHON) -m flake8
APP ?= your_own_recipes
PYSCRIPT ?= manage.py

# Check that virtual_env is set
check_venv = \
    $(if $(wildcard $(POETRY_CONF)),, \
      $(error poetry config file $(POETRY_CONF) not found))

packages: ## Install dependencies
	@:$(call check_venv)
	$(POETRY) install

lint: ## Run flake8 on python files
	@:$(call check_venv)
	@echo "-> Running flake8 on every file in the repo"
	@find . -name '*.py' -exec $(FLAKE8) {} + \
		&& echo "-> flake8 check passed"

check-format: ## Run black to format files
	@echo "-> Running black to auto format files"
	$(POETRY) run $(PYTHON) -m black --check --diff .

format: ## Run black to format files
	@echo "-> Running black to auto format files"
	$(POETRY) run $(PYTHON) -m black .

debug: ## Debug python scripts
	$(POETRY) run $(PYTHON) -m pdb $(PYSCRIPT)

Dockerfile: ## Build if changes in docker file
	docker compose build

db-start: ## Start the database and check if there is an already running postgres db
	docker compose up -d || echo "Already running postgresql, \
		trying to stop it first." && sudo systemctl stop postgresql \
		&& docker compose up -d

db-connect: ## Connect to the postgress database with psql
	$(POETRY) run $(PYTHON) manage.py dbshell

db-makemigrations: ## Generate migration files if changes
	$(POETRY) run $(PYTHON) manage.py makemigrations $(APP)

db-migrate: db-makemigrations ## Migrate new changes of django database
	$(POETRY) run $(PYTHON) manage.py migrate $(APP)

run: db-migrate ## Run django application
	$(POETRY) run $(PYTHON) manage.py runserver

help: ## Details available commands
	@echo "-- Makefile commands --"
	@grep -E "^[^._][\$\(\)a-zA-Z_-]*:" Makefile \
		| awk -F '[:#]' '{print $$1, ":-:", $$NF}' \
		| sort \
		| column -t -s:

.PHONY: check_env db-connect django-db-connect db-migrate db-start \
		packages clean lint help test