test: clean
	@nosetests . --with-coverage --with-django

clean:
	@find . -name '*.pyc' -delete
	@rm -rf .coverage