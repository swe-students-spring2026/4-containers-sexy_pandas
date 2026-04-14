"""Unit tests for Flask web app routes."""
import pytest
from app import app as flask_app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


# test index page


# test history


# test result


# test classify


# test guide
class TestGuide:
    """Tests for GET /guide"""

    def test_guide_page_status(self, client):
        """test page status"""
        res = client.get("/guide")
        assert res.status_code == 200
        assert b"Garbage Classification Guide" in res.data

    def test_guide_content_categories(self, client):
        """test for 4 cactegories"""
        res = client.get("/guide")
        html_content = res.data.decode("utf-8")

        assert "Recyclable" in html_content
        assert "Hazardous" in html_content
        assert "Food / Kitchen" in html_content
        assert "Other / General" in html_content


# test no found
class TestNotFound:
    """Test unknown routes."""

    def test_unknown_route_returns_404(self, client):
        """Unknown route should return 404."""
        res = client.get("/nonexistent")
        assert res.status_code == 404
