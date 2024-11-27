import requests

base_url = "https://yougile.com/api-v2"


def get_company_id():
    main_info = {
        'login': 'email',  # Укажите свой email
        'password': 'password',  # Укажите свой пароль
        'name': "SkyProTesting_55"  # Укажите название своей компании
    }
    resp = requests.post(base_url + '/auth/companies', json=main_info)
    companyID = resp.json()["content"][0]["id"]
    return companyID


def get_token():
    companyID = get_company_id()

    token_data = {
        'login': 'email',  # Укажите свой email
        'password': 'password',  # Укажите свой пароль
        'companyId': companyID
    }

    resp = requests.post(base_url + '/auth/keys', json=token_data)
    key = resp.json()['key']
    return key


key = get_token()
print(key)