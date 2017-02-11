import unittest
import subprocess
import sputr

class SimpleTestResult(unittest.TestResult):

    def stopTest(self, test):
        self.log_status(self.testsRun, len(self.failures), len(self.errors), len(self.skipped))

class SimpleTestRunner():

    def color(value):
        return '\x1b[%sm' % value
    colors = {
        'red': color('0;31;40'),
        'green': color('0;32;40'),
        'yellow': color('0;33;40'),
        'purple': color('0;35;50'),
        'cyan': color('0;36;40'),
        'end': color('0'),
    }

    status_messages = {
        0: '{purple}%s {green}%s {red}%s {yellow}%s {cyan}%s{end}',
        1: '{purple}%s total, {green}%s ran, {red}%s failed, {yellow}%s error, {cyan}%s skipped{end}',
        2: '{purple}%s will be run.\n{green}%s have been run.\n{red}%s have failed.\n{yellow}%s have returned an error.\n{cyan}%s have been skipped.{end}',
    }
    result_messages = {
        'failures': '{red}%s\n%s{end}',
        'errors': '{yellow}%s\n%s{end}',
    }

    def __init__(self, verbosity=1, failfast=False, buffer=False):
        self.verbosity = verbosity
        self.failfast = failfast
        self.buffer = buffer

    def log(self, message=''):
        print(message)

    def num_status_lines(self):
        return 5 if self.verbosity == 2 else 1

    def log_status(self, *args):
        subprocess.call(['tput', 'cuu', str(self.num_status_lines()), '&&', 'tput', 'el'])
        self.log(self.status_messages[self.verbosity] % ((self.test_count,) + args))

    def run(self, suite):
        if not self.color:
            for name, value in self.colors.items():
                self.colors[name] = ''
        for level, message in self.status_messages.items():
            self.status_messages[level] = message.format(**self.colors)
        for level, message in self.result_messages.items():
            self.result_messages[level] = message.format(**self.colors)

        if hasattr(suite, 'countTestCases'):
            self.test_count = suite.countTestCases()
        else:
            self.test_count = 1
        result = SimpleTestResult()
        result.failfast = self.failfast
        result.buffer = self.buffer
        result.log_status = self.log_status

        self.log('\n' * (self.num_status_lines() - 1))
        suite.run(result)

        if self.verbosity > 0:
            for type in ['failures', 'errors']:
                if len(getattr(result, type)) > 0:
                    self.log(type.upper() + '\n')
                    for incident in getattr(result, type):
                        self.log(self.result_messages[type] % (incident[0].id(), incident[1]))

        return result

