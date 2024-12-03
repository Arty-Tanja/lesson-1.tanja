import requests

base_url = "https://yougile.com/api-v2"
# получаем токен, запуская get_token.py
my_token = ''


# Позитивные тесты
def test_get_projects():
    my_headers = {
        'Authorization': f'Bearer {my_token}',
    }

    resp = requests.get(base_url + '/projects', headers=my_headers)
    body = resp.json()
    assert resp.status_code == 200
    assert len(body) > 0

    project = body["content"][0]
    users = project["users"]
    return users


def test_create_project():
    users = test_get_projects()
    my_headers = {
        'Authorization': f'Bearer {my_token}',
        'Content-Type': 'application/json'
    }

    project_data = {
        "title": "Tanya_Company",
        "users": users
    }

    resp = requests.post(base_url + '/projects', headers=my_headers, json=project_data)

    assert resp.status_code == 201
    project_id = resp.json()["id"]
    return project_id


def test_get_project_by_id():
    project_id = test_create_project()

    my_headers = {
        'Authorization': f'Bearer {my_token}'
    }

    resp = requests.get(f"{base_url}/projects/{project_id}", headers=my_headers)

    assert resp.status_code == 200


def test_update_project():
    project_id = test_create_project()

    users = test_get_projects()

    my_headers = {
        'Authorization': f'Bearer {my_token}',
        'Content-Type': 'application/json'
    }

    project_data = {
        "title": "Tanya_new_company",
        "users": users
    }

    resp = requests.put(f"{base_url}/projects/{project_id}", headers=my_headers, json=project_data)

    assert resp.status_code == 200


# Негативные тесты
def test_no_title_project():
    users = test_get_projects()
    my_headers = {
        'Authorization': f'Bearer {my_token}',
        'Content-Type': 'application/json'
    }

    project_data = {
        "users": users
    }

    resp = requests.post(base_url + '/projects', headers=my_headers, json=project_data)

    assert resp.status_code == 400


def test_no_info_project():
    my_headers = {
        'Authorization': f'Bearer {my_token}',
        'Content-Type': 'application/json'
    }

    project_data = {
    }

    resp = requests.post(base_url + '/projects', headers=my_headers, json=project_data)

    assert resp.status_code == 400

