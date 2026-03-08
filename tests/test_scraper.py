import pytest
from app import app
from scrapers.static_scraper import scrape_titles

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_scrape_titles_success():
    # Test the standalone scraper function with a known static site
    url = "https://news.ycombinator.com"
    selector = ".titleline a"
    result = scrape_titles(url, selector)
    
    assert result['success'] is True
    assert 'count' in result
    assert result['count'] > 0
    assert len(result['data']) == result['count']

def test_scrape_titles_failure():
    # Test the standalone scraper function with an invalid URL
    result = scrape_titles("not_a_valid_url", "h1")
    assert result['success'] is False
    assert 'error' in result

def test_api_scrape_endpoint(client):
    # Test the API endpoint
    response = client.post('/api/scrape', json={
        "url": "https://news.ycombinator.com",
        "selector": ".titleline a"
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert 'count' in data
    assert len(data['data']) > 0

def test_api_scrape_missing_url(client):
    # Test API bad request handling
    response = client.post('/api/scrape', json={
        "selector": "h1"
    })
    
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
