from testtools import TestCase
from testtools.matchers import Equals
import fixtures
import os

from opsftmongo import mng

TRUE_STRING = ['True', '1']

class BaseTestCase(TestCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()
        if os.environ.get('OS_STDOUT_CAPTURE') in TRUE_STRING:
            stdout = self.useFixture(fixtures.StringStream('stdout')).stream
            self.useFixture(fixtures.MonkeyPatch('sys.stdout', stdout))
        if os.environ.get('OS_STDERR_CAPTURE') in TRUE_STRING:
            stderr = self.useFixture(fixtures.StringStream('stderr')).stream
            self.useFixture(fixtures.MonkeyPatch('sys.stderr', stderr))
    
    def test_user_model(self):
       result = mng.index()
       self.assertThat(175, Equals(result))
