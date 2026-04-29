# Makefile for Sonic AI

.PHONY: setup test lint

setup:
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

test:
	. venv/bin/activate && pytest validation/

lint:
	. venv/bin/activate && flake8 .