from app.models import Post,User
from app import db

def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_post = Review(user_id=i,title='love',author="barack",description='This movie is the best thing since sliced bread',user = self.user_James )
def tearDown(self):
        Post.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_review.user_id,1)
        self.assertEquals(self.new_review.title,'love')
        self.assertEquals(self.new_review.author,'barack')
        self.assertEquals(self.new_review.description,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_review.user,self.user_James)        
def test_save_post(self):
    self.new_post.save_post()
    self.assertTrue(len(Post.query.all())>0)  
  