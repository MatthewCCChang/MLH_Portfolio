import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
	def setUp(self):
		test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
		
		test_db.connect()
		test_db.create_tables(MODELS)

	def tearDown(self):
		test_db.drop_tables(MODELS)
		test_db.close()

	def test_timeline_post(self):
		first_post = TimelinePost.create(name='Matthew Chang', email='matthewchang@gmail.com', content='Hello world, Matthew!')
		assert first_post.id == 1
		second_post = TimelinePost.create(name='Vuong Ho', email='vuongho@gmail.com', content='Hello world, Vuong!')
		assert second_post.id == 2

		get_first_post = TimelinePost.get_by_id(1)

		assert get_first_post.name == 'Matthew Chang'
		assert get_first_post.email == 'matthewchang@gmail.com'

		get_second_post = TimelinePost.get_by_id(2)
		assert get_second_post.name == 'Vuong Ho'
		assert get_second_post.email == 'vuongho@gmail.com'