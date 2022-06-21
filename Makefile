IMAGE  ?= fusion-api
PROJECT ?= nirvana
VERSION ?= latest
PORT_HOST ?= 8000
PORT_CONTAINER ?= 8000
CONTAINER_NAME ?= fusion-api

docker-build:
	echo "Building $(IMAGE)" && \
	docker build . --build-arg PORT=$(PORT_CONTAINER) -t $(PROJECT)/$(IMAGE):$(VERSION)

docker-run:
	echo "Running $(IMAGE)" && \
	docker run --name="$(CONTAINER_NAME)" -dp $(PORT_HOST):$(PORT_CONTAINER) $(PROJECT)/$(IMAGE):$(VERSION)

clean:
	echo "Cleaning..." && \
	docker stop $(IMAGE) && \
	docker rm $(IMAGE)