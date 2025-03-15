.PHONY: clean lint test setup help

clean: ## Remove build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

lint: ## Check code style with flake8
	flake8 src tests

test: ## Run tests
	pytest tests/

setup: ## Set up development environment
	pip install -r requirements/dev.txt
	pre-commit install

docker-build: ## Build Docker image
	docker build -t ipl-analytics -f docker/Dockerfile .

docker-run: ## Run Docker container
	docker run -p 8050:8050 ipl-analytics

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'