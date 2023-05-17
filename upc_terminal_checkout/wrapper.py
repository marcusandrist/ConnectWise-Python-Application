from config import base_URL, headers
from requests import get, post, patch
from requests.exceptions import RequestException
from typing import Dict, List, AnyStr, Optional


# helper functions
# Returns a list of all configurations that match the type "target"
def config_filter(data: List[Dict], target: AnyStr):
    filtered_data = [item for item in data if item["type"]["name"] == target]
    return filtered_data


# Structured vanilla http requests


# Runs a get on any endpoint
def endpoint_get(endpoint: AnyStr) -> Dict:
    # Query String paramater added for max-size results (1,000)
    return get(base_URL + endpoint + "?pageSize=1000", headers=headers).json()


# Accepts an endpoint (format /xxx/xxx) and a dictionary as a json payload
def endpoint_post(endpoint: AnyStr, payload: Dict) -> Dict:
    try:
        # Make request to api and possibly have error code
        response = post(base_URL + endpoint, headers=headers, json=payload)
        response.raise_for_status()

        return response.json()
    
    # Show error stack
    except RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"JSON processing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


# Runs a patch on any endpoint
def endpoint_patch(endpoint: AnyStr, payload: Dict) -> Optional[Dict]:
    try:
        # Make request to api and possibly have error code
        response = patch(base_URL + endpoint, headers=headers, json=payload)
        response.raise_for_status()

        return response.json()
    
    # Show error stack
    except RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"JSON processing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


# More heavily parameterized https request & processor methods live here


# Returns all the configurations of of type Key
def fetch_keys() -> List[Dict]:
    return config_filter(endpoint_get("/company/configurations"), "Key")
