POETRY ?= poetry
POETRY_CONF ?= ./pyproject.toml
PYTHON ?= python3
PIP ?= pip3
FLAKE8 ?= flake8


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
	@find . -not -path './env*' -name '*.py' -exec $(POETRY) run $(PYTHON) -m $(FLAKE8) {} + && echo "-> flake8 check passed"

help: ## details available commands
	@echo "-- Makefile commands --"
	@grep -E "^[^._][\$\(\)a-zA-Z_-]*:" Makefile | awk -F '[:#]' '{print $$1, ":-:", $$NF}' | sort | column -t -s:

.PHONY: cli in docker-init docker-cli docker-in packages clean help test