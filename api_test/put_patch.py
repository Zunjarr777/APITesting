import requests

'''
put     update/replace
        if record does not exist, it will create
{
    'Name': 'Zunjarr'
    'Phone': 9876543210
    'Address': 'Pune'
}

patch   update/modify
{
    'Address': 'Mumbai'
}
'''

# PUT

payload = {
            "name": "API",
            "job": "API Testing"
        }
resp = requests.put("https://reqres.in/api/users/2", data=payload)
print(resp)
print(resp.status_code)
print(resp.json())
assert resp.json()['job'] == 'API Testing', 'Wrong job name'


# PATCH

payload = {
            "job": "UI Testing"
        }
resp = requests.put("https://reqres.in/api/users/2", data=payload)
print(resp)
print(resp.status_code)
print(resp.json())
assert resp.json()['job'] == 'UI Testing', 'Wrong job name'
