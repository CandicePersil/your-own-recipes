POETRY ?= poetry
POETRY_CONF ?= ./pyproject.toml
PYTHON ?= python3
PIP ?= pip3
FLAKE8 ?= $(POETRY) run $(PYTHON) -m flake8


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

help: ## Details available commands
	@echo "-- Makefile commands --"
	@grep -E "^[^._][\$\(\)a-zA-Z_-]*:" Makefile \
		| awk -F '[:#]' '{print $$1, ":-:", $$NF}' \
		| sort \
		| column -t -s:

Dockerfile: ## Build if changes in docker file
	docker compose build

db-start: ## Start the database and check if there is an already running postgres db
	docker compose up -d || echo "Already running postgresql, \
		trying to stop it first." && sudo systemctl stop postgresql \
		&& docker compose up -d

db-connect: ## Connect to the postgress database
	docker exec -it your-own-recipes-db-1 psql -U dbadminuser postgres*

django-db-connect: ## Connect to the postgress database using django
	$(POETRY) run $(PYTHON) manage.py dbshell

db-migrate: ## Migrate new changes of dajngo database
	$(POETRY) run $(PYTHON) manage.py migrate

.PHONY: check_env db-connect django-db-connect db-migrate db-start \
		packages clean lint help test