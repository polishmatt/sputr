import os
from tests import SputrTest

start_dir = os.path.join(os.path.dirname(__file__), 'fixtures')

class DiscoverTest(SputrTest):
    def assert_suite_matches_pattern(self, pattern, tests):
        suite = self.sputr.discover(start_dir=start_dir, pattern=pattern)
        unexpected = []

        for test in self.sputr.list_tests(suite):
            name = test.id()[test.id().rfind('.') + 1:]
            if name in tests:
                tests.remove(name)
            else:
                unexpected.append(test.id())

        failures = []
        if len(tests) > 0:
            failures.append('Missing expected tests: ' + str(tests))
        if len(unexpected) > 0:
            failures.append('Found unexpected tests: ' + str(unexpected))
            
        if len(failures) > 0:
            self.fail("\n".join(failures))

    def test_all(self):
        self.assert_suite_matches_pattern('', [
            'test_exact_name',
            'test_exact',
            'test_most_exact',
            'test_exact_dir',
            'test_all',
        ])

    def test_exact_name(self):
        self.assert_suite_matches_pattern('test_exact_name', [
            'test_exact_name'
        ])

    def test_exact_file(self):
        self.assert_suite_matches_pattern('test_exact.py', [
            'test_exact_name',
            'test_exact',
            'test_most_exact',
        ])

    def test_exact_one_file(self):
        self.assert_suite_matches_pattern('tests/fixtures/exact/test_exact.py', [
            'test_most_exact',
        ])

    def test_exact_dir(self):
        self.assert_suite_matches_pattern('tests/fixtures/exact', [
            'test_most_exact',
            'test_exact_dir',
        ])

