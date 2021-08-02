from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_path():
	response = client.get('/')
	assert response.status_code == 201
	assert response.json() == {"message": "I'm alive"}