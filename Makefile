.PHONY: install lock dev test format build run stop logs

IMAGE_NAME = ecommerce-api
CONTAINER_NAME = ecommerce-api-container
PORT = 8000
VOLUME_NAME = ecommerce-data
PROJECT_DIR ?= /opt/ecommerce-api


install: ## Install dependencies using pipenv
	pipenv install --dev

lock: ## Generate Pipfile.lock
	pipenv lock

build: ## Build Docker image
	docker build --build-arg PROJECT_DIR=$(PROJECT_DIR) -t $(IMAGE_NAME) .

create-volume: ## Create Docker volume for persistent data
	docker volume create $(VOLUME_NAME)

remove-volume: ## Remove Docker volume
	docker volume rm $(VOLUME_NAME)

run: create-volume ## Run Docker container with volume
	docker run -d \
		--name $(CONTAINER_NAME) \
		-p $(PORT):$(PORT) \
		-v $(VOLUME_NAME):$(PROJECT_DIR)/data \
		-e PROJECT_DIR=$(PROJECT_DIR) \
		$(IMAGE_NAME)

stop: ## Stop and remove Docker container
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

logs: ## View Docker container logs
	docker logs -f $(CONTAINER_NAME)

restart: stop run ## Restart Docker container

check-env: ## Verify development environment
	@echo "Checking development environment..."
	@command -v pipenv >/dev/null 2>&1 || { echo "pipenv is not installed. Install it using: pip install pipenv"; exit 1; }
	@command -v docker >/dev/null 2>&1 || { echo "docker is not installed. Please install Docker first"; exit 1; }
	@echo "Development environment looks good!"


setup: check-env install
all: install build run