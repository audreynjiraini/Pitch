import unittest
from app.models import Pitch, User, Comments
from datetime import datetime

class PitchTest(unittest.TestCase):

  def setUp(self):
      self.new_pitch = Pitch()#20, 'pickup', 'test', 'test_user tests work' , datetime.now(), 0, 0, 28)

  def test_instance(self):
      self.assertTrue(isinstance(self.new_pitch, Pitch))

  def test_save_pitch(self):
      self.new_pitch.save_pitch()
      self.assertTrue(len(Pitch.query.all())>0)

  def test_get_pitches(self):
      self.new_pitch.save_pitch()
      got_pitches = Pitch.get_pitches(1)
      self.assertTrue(len(got_pitches) == 1)

#   def test_get_pitch_comments(self):
#       self.new_pitch.save_pitch()
#       got_pitch_comments = Pitch.get_comments()
#       self.assertTrue(len(got_pitch_comments)>=0)