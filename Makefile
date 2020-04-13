install-dev:
	@pip install -r requirements.txt
	@pre-commit install

install:
	@python setup.py install

publish:
	@python setup.py sdist bdist_wheel
	@twine upload dist/*