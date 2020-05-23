fmt:
	isort -y && black .

install:
	python setup.py install
