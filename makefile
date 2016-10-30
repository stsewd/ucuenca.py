PYTHON = python
TEST_RUNNER = unittest
FLAGS = -v

test:
	$(PYTHON) -m $(TEST_RUNNER) $(FLAGS)

doc:
	pandoc -o docs/README.rst README.md

clean:
	rm -f -r docs/*
	python3 setup.py clean --all
