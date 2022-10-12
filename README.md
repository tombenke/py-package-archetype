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
s/py-package-archetype/py-package-archetype/g
s/py-package-archetype-description/py-package-archetype-description/g
s/py-package-archetype-author/py-package-archetype-author/g
s/tombenke@gmail.com/tombenke@gmail.com/g
s/tombenke/tombenke/g
s/py-package-archetype-network/py-package-archetype-network/g
```

modified:

```sed
s/py-package-archetype/my-py-package/g
s/py-package-archetype/my-py-package/g
s/py-package-archetype-description/My new python package./g
s/py-package-archetype-author/Han Solo/g
s/tombenke@gmail.com/hansolo@tatooine.space/g
s/tombenke/hansolo/g
s/py-package-archetype-network/my-py-package-network/g
```

3. Execute the substitution:

```bash
    ./.kickoff.sh
```

4. Replace the existing local git repo, that belong to the archetype with a new one.

Remove the `.git` subfolder:

```bash
    rm .git -fr
```

Init with an empty repo:
```bash
    git init
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

## License
The scripts and documentation in this project are released under the [MIT License](LICENSE)

