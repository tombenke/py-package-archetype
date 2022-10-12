from setuptools import find_packages, setup
import pathlib
import os

# Package metadata
# ----------------

NAME = "py-package-archetype"
DESCRIPTION = "py-package-archetype-description."

# Get the long description from the README file
HERE = pathlib.Path(__file__).parent.resolve()
# LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")
LONG_DESCRIPTION = """
For further information, please visit the [project's homepage](https://github.com/tombenke/py-package-archetype).
"""

URL = "https://github.com/tombenke/py-package-archetype"
EMAIL = "tombenke@gmail.com"
AUTHOR = "py-package-archetype-author"
LICENSE = "MIT"
REQUIRES_PYTHON = ">=3.8"

# What packages are required for this module to be executed?
REQUIRED = [
]

DEV_REQUIREMENTS = [
    "build",
    "coverage",
    "coverage-badge",
    "black",
    "pylint",
    "pdoc",
    "pydeps",
]

setup(
    name=NAME,
    version=os.getenv("VERSION", "1.0.0"),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    license=LICENSE,
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=REQUIRED,
    extras_require={"dev": DEV_REQUIREMENTS},
    entry_points={
        "console_scripts": [],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
