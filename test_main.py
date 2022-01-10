from fastapi.testclient import TestClient
import main


# testing
client = TestClient(main.app)

def test_get_account():
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() ==  123


def test_get_account(): 
    response = client.get("/32") # items not in database will still result in response code 200 and return None
    assert response.status_code == 200
    assert response.json() ==  None

