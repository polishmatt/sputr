# Sputr

Simple Python Unit Test Runner

An intuitive command line and Python package interface for Python's unit testing framework.

## Command Line Examples

### Run all tests in the current directory
`sputr`

### Run all tests in the specified directory
`sputr dirname`

### Run all tests in files that match the specified name
`sputr filename.py`

### Run all tests in a specific file
`sputr dirname/filename.py`

### Run all tests that match a pattern

\* may be used as a wildcard.

`sputr test_name`

`sputr test_name_*`

## Python Package Examples

`sputr.discover` returns a [TestSuite](https://docs.python.org/2/library/unittest.html#unittest.TestSuite).

```python
import sputr
suite = sputr.discover(start_dir='.', pattern='test_*')
unittest.TextTestRunner().run(suite)
```

`sputr.list_tests` converts a TestSuite to a list of [TestCase](https://docs.python.org/2/library/unittest.html#unittest.TestCase) objects which can be iterated over easily.

```python
for test in sputr.list_tests(suite):
    print test.id()
```

