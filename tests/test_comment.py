import unittest
from app.models import User, Pitch, Comments
from app import db

class CommentsTest(unittest.TestCase):
    
    def setUp(self):
        self.user_Logan = User(username = 'Logan', password='logan', email='woganlolverine@gmail.com')
    
        self.new_comment = Comments(id = 1, pitch_title = 'Comments', pitch_body = 'I like it', user_id = self.user_Logan)

    def tearDown(self):
        Review.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id, 1)

        self.assertEquals(self.new_comment.pitch_title, 'Comments')

        self.assertEquals(self.new_comment.pitch_body, 'I like it')

        self.assertEquals(self.new_comment.user_id, self.user_Logan)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all())>0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comments.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)