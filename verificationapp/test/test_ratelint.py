import pytest
from rest_framework.test import APIClient
from rest_framework import status


@pytest.mark.django_db
def test_rate_limit_with_api_key():
    client = APIClient()
    url = "/api/validate/valid_id/"

    data = {"national_id": "29001011234567"}
    
    # إضافة API Key إلى الهيدر
    api_key = 
    client.credentials(HTTP_AUTHORIZATION=f"Api-Key {api_key}")

    for i in range(10):
        response = client.post(url, data, format='json')
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED]

    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS
    assert "throttled" in response.json()["detail"]
