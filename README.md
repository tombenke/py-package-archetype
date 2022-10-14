py-package-archetype
====================

[![Quality Check Status](https://github.com/tombenke/py-package-archetype/workflows/Quality%20Check/badge.svg)](https://github.com/tombenke/py-package-archetype)
[![Release Status](https://github.com/tombenke/py-package-archetype/workflows/Release/badge.svg)](https://github.com/tombenke/py-package-archetype)
![Coverage](./coverage.svg)

## About

py-package-archetype-description

## How to create a new actor from this repo

This repository holds the minimal boilerplate code that is needed to create a new Python package by executing the steps listed below.

Keep this repository up-to-date and create the new packages using it, instead of always recreating them manually, from scratch.

__NOTE: Please, do NOT forget to remove this block from the README, and write the right documentation for the newly created actor!__

### Prerequisites

You will need the following tools installed on your machine:
- bash
- git
- Python 3.10
- sed
- [Task](https://taskfile.dev/)

### Steps

1. clone this repo into a new folder, with the name of the new actor, for example:

```bash
    git clone git@github.com:tombenke/py-package-archetype.git my-py-package
```

2. Step into the newly cloned folder:

```bash
    cd my-py-package
```
3. Edit the substitute patterns in the `.kickoff.sed` file:

original:

```sed
s/py-package-archetype-description/py-package-archetype-description/g
s/py-package-archetype-author/py-package-archetype-author/g
s/py-package-archetype-network/py-package-archetype-network/g
s/py-package-archetype/py-package-archetype/g
s/tombenke@gmail.com/tombenke@gmail.com/g
s/tombenke/tombenke/g

```

modified:

```sed
s/py-package-archetype-description/My new python package./g
s/py-package-archetype-author/Han Solo/g
s/py-package-archetype-network/my-py-package-network/g
s/py-package-archetype/my-py-package/g
s/tombenke@gmail.com/hansolo@tatooine.space/g
s/tombenke/hansolo/g

```

3. Execute the substitution with the basedir of the project:

```bash
    ./.kickoff.sh .
```

4. Replace the existing local git repo, that belong to the archetype with a new one.

Remove the `.git` subfolder:

```bash
    rm .git -fr
```

Init with an empty repo, and add some content to it:
```bash
    git init
    git add README.md
    git commit -m "Add README.md"
```

5. Create a Python virtual environment in the local folder:

```bash
    task venv-create
```

6. Activate the newly created virtual environment:

```bash
    . venv/bin/activate
```

7. Install the dependencies:

```bash
    task install-dev-editable
```

8. Edit the content of the README.md file:

- Remove the current, archetype related block.
- Add the new content on the actor.

9. Run tests and docs generation:

```bash
    task
```

10. Build the package, and try to run it:

```bash
    task build
    dist/cli --help
```

11. Create a new github repository, then commit and push the new project to it,
then add a new repository secret under the __Settings/Secrets/Actions__ section
with the name of `PYPI_API_TOKEN` with a valid token of yours,
that you can use for publishing to the [PyPI registry](https://pypi.org/).

List the tasks are available during the work:
```bash
task list

task: Available tasks for this project:
* build: 		Build
* clean: 		Clean temporary files and folders
* coverage: 		Test coverage
* dc-down: 		Clean up docker containers
* dc-logs: 		Get all docker container logs
* dc-logsf: 		Get all docker container logs and follow
* dc-stop: 		Stop docker containers
* dc-up: 		Start docker containers
* dc-upd: 		Start docker containers in the background
* default: 		Executes all the tests then build the binary.
* docs: 		Generate module documentation into the docs/ folder
* format: 		Autoformat the source files
* install: 		Install the package and its dependencies
* install-dev: 		Install the package and its dependencies for development
* install-dev-editable: Install the package and its dependencies for development with editablility
* install-git-hooks: 	Install git hooks
* lint: 		Run python linter
* pre-commit: 		Runs the QA tasks from a git pre-commit hook
* publish-package: 	Publish the package to PyPI
* test: 		Run all the tests.
* test-verbose: 	Run all the go tests.
* venv-create: 		Create a new Python Virtual Environment under the local folder
```

## License
The scripts and documentation in this project are released under the [MIT License](LICENSE)

