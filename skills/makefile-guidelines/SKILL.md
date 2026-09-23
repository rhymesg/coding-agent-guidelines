---
name: makefile-guidelines
description: "Keeps a Makefile a small, self-documenting task runner with one target per scenario. Use when creating or editing a Makefile."
---

# Makefile Guidelines

## Targets

- One target per scenario, named after it: `make test`, `make run-sim`. Not `make run MODE=sim`.
- A target takes at most one command-line variable, for the input that changes between runs: `make run DATASET=euroc`. Every other setting lives in the configuration file.
- Declare every non-file target in `.PHONY`; default to `help`.
- Document each user-facing target with a `## target: description` comment and a `help` target that prints them.
- Keep a recipe to a few lines. Move longer logic into a script the target calls.

## Variables

- Use `:=` for internal variables, `?=` for the one the caller may set.
- Leave `SHELL` at the default unless a recipe needs a Bash feature.

## Build Systems

- The Makefile is a task runner. Build with CMake, or colcon for ROS packages, and keep compile rules out of the Makefile.
- When the repository has a Docker image, run builds and tools inside it, as the calling user.
- Start a new Makefile from [templates/Makefile](templates/Makefile).
