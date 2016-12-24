PYTHON = python
TEST_RUNNER = unittest
TEST_FLAGS = -v


test:
	$(PYTHON) -m $(TEST_RUNNER) $(TEST_FLAGS)

doc:
	pandoc -o docs/README.rst README.md

clean:
	$(PYTHON) setup.py clean --all
	rm -f -r docs/*

pypi:
	$(PYTHON) setup.py sdist upload

