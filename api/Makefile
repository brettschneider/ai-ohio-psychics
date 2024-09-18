.PHONY: help
help:
	@echo "Available targets:"
	@echo
	@sed -n '/^## /s/^## //p' $(MAKEFILE_LIST) | column -t -s ':' | sed -e 's/^/ /'

## clean: Remove all temp Python files (*.pyc for example)
clean:
	@for d in $$(find . -type d -iname '__pycache__'); do \
		echo "Removing $$d"; \
		rm -r "$$d"; \
	done
	@for d in $$(find . -type d -iname '.pytest_cache'); do \
		echo "Removing $$d"; \
		rm -r "$$d"; \
	done
	@for d in $$(find . -type f -iname '.DS_Store'); do \
		echo "Removing $$d"; \
		rm -r "$$d"; \
	done

## install: Set up Python virtualenv
install:
	pipenv install

## rm: Remove the Python virtualenv
rm:
	pipenv --rm

## api: Run the API server
api:
	@pipenv run python main.py

## cli: Run the chatbot from the terminal
cli:
	@pipenv run python ./chatbot.py


## clear-sessions: Remove all the session data
clear-sessions:
	@for d in $$(find ./database/sessions -type f -iname '*.json'); do \
		echo "Removing $$d"; \
		rm -r "$$d"; \
	done
