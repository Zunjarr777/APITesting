import requests

# GET

resp = requests.get("https://reqres.in/api/users?page=2")
print(resp)
print(resp.url)

code = resp.status_code
# assert code == 200, "Failed response"
# print(resp.text)
# print(resp.content)
print(f'JSON Response is: \n', resp.json())
print(resp.json()['data'])
print(resp.json()['data'][0])
print(resp.json()['data'][0]['email'])
assert resp.json()['data'][0]['email'] == 'michael.lawson@reqres.in'
# assert resp.json()['data'][0]['email'] == 'michael.lawson@reqres.com'
# assert (resp.json()['data'][0]['email']).endswith('gmail.com'), 'Wrong email format'

# print(resp.headers)
# print(resp.cookies)
# print(resp.encoding)
print(resp.url)

json_response = resp.json()
print(json_response['total'])

payload = {
    "name": "morpheus",
    "job": "leader"
}
resp = requests.post("https://reqres.in/api/users", data=payload)
print(resp)
print(resp.status_code)
print(resp.json())
assert resp.json()['job'] == 'leader', 'Wrong job name'

resp = requests.post("https://reqres.in/api/users", timeout=1)
print(resp)
print(resp.status_code)
