fmt:
	poetry run isort vktoken/
	poetry run black vktoken/

lint:
	poetry run flake8 vktoken/
