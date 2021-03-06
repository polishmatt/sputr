# Sputr

[![Build Status](https://travis-ci.org/polishmatt/sputr.svg?branch=master)](https://travis-ci.org/polishmatt/sputr)

Simple Python Unit Test Runner

An intuitive command line and Python package interface for Python's unit testing framework with consistent behavior across Python versions.

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

## Breaking Changes

### 1.1.0

* Removed --python option ([issue #3](https://github.com/polishmatt/sputr/issues/3))
* Exit code 1 returned when no tests are run ([issue #4](https://github.com/polishmatt/sputr/issues/4))

