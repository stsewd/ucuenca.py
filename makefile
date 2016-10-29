PYTHON = python
TEST_RUNNER = unittest
FLAGS = -v

test:
	$(PYTHON) -m $(TEST_RUNNER) $(FLAGS)
