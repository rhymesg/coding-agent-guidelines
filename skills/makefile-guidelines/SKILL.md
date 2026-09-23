---
name: makefile-guidelines
description: "Keeps a Makefile a small, self-documenting task runner with one target per scenario. Use when planning, creating, or editing a Makefile."
---

# Makefile Guidelines

- When creating a new Makefile, read the Makefiles of neighboring projects first and keep their conventions where they agree with the rules below.

## Targets

- Use the common names `help`, `build`, `test`, `run`; add one target per further scenario, named after it: `make run-sim`. Not `make run MODE=sim`.
- A target takes at most one command-line variable, for the input that changes between runs: `make play BAG=flight1`. Every other setting lives in the configuration file.
- Declare every non-file target in `.PHONY`; default to `help`.
- Document each user-facing target with a `## target: description` comment and a `help` target that prints them.
- Keep a recipe to a few lines. Move longer logic into a script the target calls.

## Variables

- Use `:=` for internal variables, `?=` for the one the caller may set.
- Leave `SHELL` at the default unless a recipe needs a Bash feature.

## Build Systems

- The Makefile is a task runner. Build with CMake, or colcon for ROS packages, and keep compile rules out of the Makefile.
- Run builds and tools in the repository's environment: its Docker image, as the calling user, or its Python virtual environment.
