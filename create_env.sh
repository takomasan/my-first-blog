#!/bin/sh
pipenv --three

pipenv install pip
pipenv install Django~=2.2.4

source $(pipenv --venv)/bin/activate
django-admin startproject mysite .