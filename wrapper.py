from requests import post, patch, get
from typing import Dict, List
from config import headers, base_url

class Wrapper:
    def __init__(self):
        # Instance variables (authentication and headers for api, resolved from a local config file)
        self.headers = headers()
        self.base_url = base_url()

    # Functions used for testing purposes

    # datetime format "YYYY-MM-DDTHH:MM:SSZ"
    def fetch_tickets_after_date(self, datetime: str) -> List[Dict]:
        res = get(f"{self.base_url}/service/tickets?conditions=_info/dateEntered>[2023-05-03T14:24:21Z]&pageSize=1000",
                  headers=self.headers)
        if 200 <= res.status_code <= 300:
            return res.json()
        else:
            return []
        else:
            return []

    # Fully implemented functions to be called externally

    def fetch_employees(self) -> List[Dict]:
        res = get(f"{self.base_url}/system/members?pageSize=1000", headers=self.headers)
        if 200 <= res.status_code <= 300:
            # primaryEmail attribute belongs only to employees
            actual_employees = [e for e in res.json() if "bakerts" in e.get("primaryEmail", "")]
            employee_names = [d["firstName"] for d in actual_employees]
            return employee_names
        else:
            return []

    # Ticket request functions (466: checked in, 467: checked out, 468: lost)
    
    def config_create_ticket(self, tag_number: str, employee_id: int, text: str, status: int):
        config = self.fetch_config_from_tag(tag_number)
        res = post(f"{self.base_url}/service/tickets",
                   headers=self.headers,
                   json={
                       "summary": config["name"],
                       "board": {"id": 24},
                       "company": {"identifier": config["company"]["identifier"]},  # Replace with the company identifier
                       "owner": {"id": employee_id},  # Replace with the contact ID
                       "initialDescription": text,
                       "status": {"id": status},
                       "customFields": [
                           {"id": 6,
                            "value": tag_number}
                       ]
                   })
        if 200 <= res.status_code <= 300:
            return res.json()
        else:
            return res.json()

    def fetch_config_from_tag(self, tag_number: str) -> str:
        formatted_tag = f"\"{tag_number}\""
        res = get(f"{self.base_url}/company/configurations?conditions=tagNumber={formatted_tag}&pageSize=1000",
                  headers=self.headers)
        if 200 <= res.status_code <= 300:
            return res.json()[0]
        else:
            return 404

    def fetch_id_from_name(self, name: str):
        return get(f'{self.base_url}/system/members?conditions=firstName="{name.lower().capitalize()}"&columns=id,',
                   headers=self.headers).json()[0]["id"]

    def fetch_open_tickets_by_name(self, name: str):
        querified_url = f"{self.base_url}/service/tickets?conditions=summary=\"{name}\" AND status/id=466"
        return get(querified_url, headers=self.headers).json()

    def fetch_ticket_owner_by_name(self, name: str):
        querified_url = f"{self.base_url}/service/tickets?conditions=summary=\"{name}\" AND status/id=466"
        res = get(querified_url, headers=self.headers).json()
        try:
            return res[0]["owner"]["name"]
        except:
            return ""

    def close_ticket(self, ticket_id: int):
        payload = [{"op": "replace", "path": "status", "value": {"id": "467"}}]
        return patch(f"{self.base_url}/service/tickets/{ticket_id}", json=payload, headers=self.headers).json()

    def lose_ticket(self, ticket_id: int):
        payload = [{"op": "replace", "path": "status", "value": {"id": "468"}}]
        return patch(f"{self.base_url}/service/tickets/{ticket_id}", json=payload, headers=self.headers).json()
