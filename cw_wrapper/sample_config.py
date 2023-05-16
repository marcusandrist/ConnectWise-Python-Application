# Implementation required for functionality of wrapper

# companyID+publickey:privatekey (Encoded in base-64)
auth_key = "this should be alphanumeric 4isDF3425FVFSD="
# client_id required by CWM as an organizer for API integration calls
client_id = "numbers-num-num-num-biggestnumber"
# base_URL, located in NA + would change if CWM server was hosted
base_URL = "https://na.myconnectwise.net/v4_6_release/apis/3.0"

# easy headers
headers = {
    "Authorization": f"Basic {auth_key}",
    "ClientID": client_id,
}
