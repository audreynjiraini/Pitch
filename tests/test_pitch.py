import unittest
from app.models import Pitch, User, Comments
from datetime import datetime
from app import db

class PitchTest(unittest.TestCase):

    def setUp(self):
        self.user_Logan = User(username = 'Logan', password = 'logan', email = 'woganlolverine@gmail.com')
        self.new_pitch = Pitch(title = 'test', body = 'testing pitch creation',user_id =  1, category = 'promotion')#20, 'pickup', 'test', 'test_user tests work' , datetime.now(), 0, 0, 28)


    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title, 'test')
        self.assertEquals(self.new_pitch.body, 'testing pitch creation')
        self.assertEquals(self.new_pitch.user_id, 1)
        self.assertEquals(self.new_pitch.category, 'promotion')


    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)


    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(len(got_pitch is not None))