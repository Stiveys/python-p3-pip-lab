# Environment Lab

## Learning Goals

- Use pipenv to set up a virtual environment
- Install libraries using pipenv

***

## Key Vocab

- **Module**: a file containing Python definitions and statements. A module's
functions, classes, and global variables can be accessed by other modules.
- **Package**: a collection of modules that can be accessed as a group using
the package name.
- **`import`**: the Python keyword used to access data from other packages and
modules inside of the current module.
- **PyPI**: the **Py**thon **P**ackage **I**ndex. A repository of Python
packages that can be downloaded and made available to your application.
- **`pip`**: the command line tool used to download packages from PyPI. `pip`
is installed on your computer automatically when you download Python.
- **Virtual Environment**: a collection of modules, packages, and scripts that
can be activated or deactivated at any time.
- **Pipenv**: a virtual environment tool that uses `pip` to manage the modules,
packages, and scripts that you intend to use in your application.

***

## Introduction

In this lab we will create a virtual environment using pipenv with
specific versions of Python and libraries.

***

## Instructions

- Using the command `pipenv --python 3.8.13`, set up a virtual
  environment using Python 3.8.13.
- Using the `pipenv install` command install these versions of the following libraries
 `requests==2.27.1` and `pytest==7.1.3`

Run `pipenv shell` to enter the virtual environment. Then run
`pytest lib/testing_env` to run your tests.

Once all of your tests are passing, commit and push your work using `git` to
submit.

***

## Conclusion

Virtual environments allow us to have a deterministic and predictable
 runtime for our Python projects. You can apply what we learned in
 this exercise to make sure you have the right environment to
 run your Python code in for your future projects.
***

## Resources

- [Pip env](https://pipenv.pypa.io/en/latest/)
- [PYPI](https://pypi.org/).
