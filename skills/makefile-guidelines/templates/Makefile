# Task runner for a repository built and run inside its Docker image.
# Replace <registry>, <name> and the recipes; keep the target names that apply.
REPO_DIR := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
IMAGE    := <registry>/<name>

# The container runs as the caller, so files it writes into the checkout stay
# owned by the developer. ROS 2 nodes also need --network host --ipc host.
RUN := docker run --rm --user $(shell id -u):$(shell id -g) \
	--env HOME=/tmp --volume $(REPO_DIR):/work --workdir /work $(IMAGE):latest

.DEFAULT_GOAL := help
.PHONY: help build-docker build test run shell clean

## build-docker: Build the image.
build-docker:
	docker build -f docker/Dockerfile -t $(IMAGE):latest .

## build: Build the sources in the image, output in build/.
build:
	$(RUN) cmake -B build -S . && $(RUN) cmake --build build -j$$(nproc)

## test: Build, then run the tests.
test: build
	$(RUN) ctest --test-dir build --output-on-failure

# CONFIG is the one per-run setting; everything else lives in the file.
CONFIG ?= config/default.yaml
## run: Run the application with CONFIG, default config/default.yaml.
run: build
	$(RUN) build/<name> --config $(CONFIG)

## shell: Interactive shell in the image.
shell:
	$(RUN) bash

## clean: Delete build output.
clean:
	rm -rf build/

## help: List the targets.
help:
	@grep -h '^## ' $(MAKEFILE_LIST) | sed 's/^## //' | column -t -s ':'
