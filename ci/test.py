from hi import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hi siri!'
    assert response.status_code == 200
