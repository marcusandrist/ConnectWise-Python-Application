from config import auth_key, client_id, base_URL
from requests import get

# Headers required by CWM for http request
headers = {
    "Authorization": f"Basic {auth_key}",
    "ClientID": client_id,
}


def sample_get():
    return get(
        base_URL,
        headers=headers,
    )

# Check response
if __name__ == "__main__":
    res = sample_get()
    if res.status_code != 200:
        print(f"---Error {res.status_code}--- \n\n {res.text}")
    else:
        print("success")
        print(res.json())
