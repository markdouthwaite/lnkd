#!/usr/bin/env bash


# install poetry and point to it.
pip3 install poetry==1.0.5
source $HOME/.poetry/env

# install project dependencies
poetry install

# install pre-commits
pre-commit install
