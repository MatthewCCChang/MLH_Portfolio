import unittest
import os
os.environ["TESTING"] = "true"

from app import app

class AppTestCase(unittest.TestCase):
	def setUp(self):
		self.client = app.test_client()

	def test_home(self):
		response = self.client.get("/")
		assert response.status_code == 200
		html = response.get_data(as_text=True)
		assert "<title>MLH Fellows</title>" in html

		# Check for headers
		assert "Vuong Ho" in html
		assert "Matthew Chang" in html
		assert "Hobbies" in html

	def test_MatthewChang(self):
		response = self.client.get("/MatthewChang")
		assert response.status_code == 200
		html = response.get_data(as_text=True)
		assert "<title>Matthew Chang</title>" in html

		assert "University of California, Irvine" in html


	def test_VuongHo(self):
		response = self.client.get("/VuongHo")
		assert response.status_code == 200
		html = response.get_data(as_text=True)
		assert "<title>Vuong Ho</title>" in html

		assert "University of Rochester" in html


	def test_hobbies(self):
		response = self.client.get("/Hobbies")
		assert response.status_code == 200
		html = response.get_data(as_text=True)
		assert "<title>Hobbies</title>" in html

		# Check if both hobby section is there
		assert "Matthew's Hobbies" in html
		assert "Vuong's Hobbies" in html

	def test_timeline(self):
		response = self.client.get("/api/timeline_post")
		assert response.status_code == 200
		assert response.is_json
		json = response.get_json()
		assert "timeline_posts" in json
		assert len(json["timeline_posts"]) == 0