test:
	# Run security baseline
	ran:
	# Start monitoring system
	python -m guard

ci: test
	coverage run --source=guard tests/
	coverage report

format:
	python -m black .
	python -m isort .

lint:
	python -m flake8
	python -m mypy

build:
	poetry build