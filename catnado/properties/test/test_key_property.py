from google.appengine.ext import db

from catnado.properties.key_property import KeyProperty
from catnado.testing.testcase import SimpleAppEngineTestCase


class SimpleEntity(db.Model):
  friend_key = KeyProperty()


class KeyPropertyAssignmentTest(SimpleAppEngineTestCase):

  def setUp(self):
    super(KeyPropertyAssignmentTest, self).setUp()
    self.one_sock = SimpleEntity()
    self.one_sock_key = self.one_sock.put()

  def test_set_with_key(self):
    two_sock = SimpleEntity(friend_key=self.one_sock_key)
    two_sock.put()
    self.assertEqual(two_sock.friend_key, self.one_sock_key)

  def test_set_with_entity(self):
    two_sock = SimpleEntity(friend_key=self.one_sock)
    two_sock.put()
    self.assertEqual(two_sock.friend_key, self.one_sock_key)
