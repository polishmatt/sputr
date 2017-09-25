import subprocess
import os

from tests import SputrTest

start_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'cli')

class CLITest(SputrTest):

    def test_exit_success(self):
        with open(os.devnull, 'w') as FNULL:
            subprocess.check_call(
                ['python', '-msputr', '-s' + start_dir, 'test_success'],
                stdout=FNULL,
                stderr=subprocess.STDOUT
            )

    def test_exit_failure(self):
        try:
            with open(os.devnull, 'w') as FNULL:
                subprocess.check_call(
                    ['python', '-msputr', '-s' + start_dir, 'test_fail'],
                    stdout=FNULL,
                    stderr=subprocess.STDOUT
                )
            self.fail('received success exit code when error expected')
        except subprocess.CalledProcessError:
            pass

    def test_exit_fail_none(self):
        try:
            with open(os.devnull, 'w') as FNULL:
                subprocess.check_call(
                    ['python', '-msputr', '-s' + start_dir, 'test_none'],
                    stdout=FNULL,
                    stderr=subprocess.STDOUT
                )
            self.fail('received success exit code when error expected')
        except subprocess.CalledProcessError:
            pass

    def test_exit_success_none(self):
        with open(os.devnull, 'w') as FNULL:
            subprocess.check_call(
                ['python', '-msputr', '-s' + start_dir, '--allow-none', 'test_none'],
                stdout=FNULL,
                stderr=subprocess.STDOUT
            )

