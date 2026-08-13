from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_projects():
    response = client.get("/projects")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_project():
    project = {
        "name": "Test CI Project",
        "description": "Created during automated testing",
        "repository_url": "https://github.com/test/cicd-dashboard",
    }

    response = client.post("/projects", json=project)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test CI Project"
    assert data["description"] == "Created during automated testing"
    assert data["status"] == "active"


def test_get_nonexistent_project():
    response = client.get("/projects/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Project not found"
