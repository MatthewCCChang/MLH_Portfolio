import unittest
import os
os.environ["TESTING"] = "true"

from app import app

class AppTestCase(unittest.TestCase):
	def setUp(self):
		self.client = app.test_client()

	# def test_home(self):
	# 	response = self.client.get("/")
	# 	assert response.status_code == 200
	# 	html = response.get_data(as_text=True)
	# 	assert "<title>MLH Fellows</title>" in html

	# 	# Check for headers
	# 	assert "Vuong Ho" in html
	# 	assert "Matthew Chang" in html
	# 	assert "Hobbies" in html

	# def test_MatthewChang(self):
	# 	response = self.client.get("/MatthewChang")
	# 	assert response.status_code == 200
	# 	html = response.get_data(as_text=True)
	# 	assert "<title>Matthew Chang</title>" in html

	# 	assert "University of California, Irvine" in html


	# def test_VuongHo(self):
	# 	response = self.client.get("/VuongHo")
	# 	assert response.status_code == 200
	# 	html = response.get_data(as_text=True)
	# 	assert "<title>Vuong Ho</title>" in html

	# 	assert "University of Rochester" in html


	# def test_hobbies(self):
	# 	response = self.client.get("/Hobbies")
	# 	assert response.status_code == 200
	# 	html = response.get_data(as_text=True)
	# 	assert "<title>Hobbies</title>" in html

	# 	# Check if both hobby section is there
	# 	assert "Matthew's Hobbies" in html
	# 	assert "Vuong's Hobbies" in html

	# def test_timeline(self):
	# 	response = self.client.get("/api/timeline_post")
	# 	assert response.status_code == 200
	# 	assert response.is_json
	# 	json = response.get_json()
	# 	assert "timeline_posts" in json
	# 	assert len(json["timeline_posts"]) == 0

	# 	# Tests for adding posts
	# 	response = self.client.post("/api/timeline_post",
	# 														data={
	# 															"name": "Matthew Chang",
	# 															"email": "matthewchang@gmail.com",
	# 															"content": "Hello world, Matthew!"
	# 														})
	# 	print(response.status_code)
	# 	assert response.status_code == 200
	# 	assert response.is_json
	# 	json = response.get_json()
	# 	assert json["id"] == 1

	# 	# Test for posts is on db after adding post
	# 	response = self.client.get("/api/timeline_post")
	# 	assert response.status_code == 200
	# 	assert response.is_json
	# 	json = response.get_json()
	# 	assert "timeline_posts" in json
	# 	assert len(json["timeline_posts"]) == 1
	# 	assert json["timeline_posts"][0]["name"] == "Matthew Chang"
	# 	assert json["timeline_posts"][0]["email"] == "matthewchang@gmail.com"
	# 	assert json["timeline_posts"][0]["content"] == "Hello world, Matthew!"

	# def test_malformed_timeline_post(self):
	# 	# POST request missing name
	# 	response = self.client.post("/api/timeline_post", data={
	# 		"email": "john@example.com",
	# 		"content": "Hello World, I'm John!"
	# 	})
	# 	print(response)
	# 	assert response.status_code == 400
	# 	html = response.get_data(as_text=True)
	# 	assert "Invalid name" in html

	# 	# POST request with empty content
	# 	response = self.client.post("/api/timeline_post", data={
	# 		"name": "John Doe",
	# 		"email": "john@example.com",
	# 		"content": ""
	# 	})
	# 	assert response.status_code == 400
	# 	html = response.get_data(as_text=True)
	# 	assert "Invalid content" in html

	# 	# POST request with malformed email
	# 	response = self.client.post("/api/timeline_post", data={
	# 		"name": "John Doe",
	# 		"email": "not-an-email",
	# 		"content": "Hello World, I'm John!"
	# 	})
	# 	assert response.status_code == 400
	# 	html = response.get_data(as_text=True)
	# 	assert "Invalid email" in html

	def test_health(self):
		response = self.client.post('/health')
		# print(response)
		assert response.status_code == 200
