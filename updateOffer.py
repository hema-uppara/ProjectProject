import requests
import json

# Define the API endpoint URL
API_URL = "https://ms-api-gateway-qa.azurewebsites.net/offers/v1/offers/2054126/submit"
payload = {
    "offerID": 2054126,
    "status": "LoadedToCampaign",
    "dateTimeCreated": "2025-12-12T07:08:42.853Z",
    "dateTimeUpdated": "2025-12-18T07:10:54.401Z",
    "countryCode": "BG",
    "offerType": "CONDITIONAL",
    "campaignName": "%$@%@%@%$@%$@@@",
    "offerMechanics": "JBJHGJFGFHGFGFFFFFFFFFFFFFFFHGFHDYT!YEE!%^$!%$^%!$%^!$^%!$%^@!@DGHCHCHC    ",
    "productType": "CR",
    "versionNumber": "22",
    "offerName": "BG %$@%@%@%$@%$@@@ JBJHGJFGFHGFGFFFFFFFFFFFFFFFHGFHDYT!YEE!%^$!%$^%!$%^!$^%!$%^@!@DGHCHCHC     CR 22",
    "offerCode": "Surpise live offer",
    "rewardEngineExcluded": True,
    "deactivationAllowed": False,
    "displayOrder": 0,
    "expirationDays": 1,
    "initiallyActive": True,
    "numberOfAssign": 10,
    "numberOfUsage": 1,
    "offerRewardRule": {
        "ruleType": "FREE_PRODUCT",
        "productCode": "CG0000000927",
        "rewardValue": 1
    },
    "offerAchievementRule": [
        {
            "label": "stamp limitations",
            "achievementRuleType": "PRODUCT_PURCHASE",
            "requiredTransactions": 1,
            "requiredQuantity": 1,
            "includeProducts": [
                "CG0000000877"
            ]
        }
    ],
    "offerTitle": [
        {
            "language": "bg",
            "text": "Error Validations"
        }
    ],
    "offerDescription": [
        {
            "language": "bg",
            "text": "\u003cp\u003e\u003cspan\u003eError Validations\u003c/span\u003e\u003c/p\u003e"
        }
    ],
    "customText": [
        {
            "language": "bg",
            "text": "Error Validations"
        }
    ],
    "offerBackground": "0486440c-06b3-5502-8a52-30baec795efe",
    "assignableFrom": "2025-12-13T00:00:00+02:00",
    "assignableTo": "2025-12-20T23:30:00+02:00",
    "assign": {
        "counter": 0,
        "consumers": []
    },
    "external": {
        "adobeCampaign": {
            "exportedAt": "2025-12-05T07:10:49.874Z",
            "lastProblem": {
                "occurredAt": "0001-01-01T00:00:00Z",
                "description": ""
            }
        },
        "lod": {
            "lastProblem": {
                "occurredAt": "0001-01-01T00:00:00Z",
                "description": ""
            },
            "exportedAt": "2025-12-05T07:10:49.874Z",
            "lod_checks": 0,
            "method": "real_time_offer"
        }
    }
}
headers = {
    'Accept': 'application/json',
    'countryCode': 'BG',
    'Content-Type': 'application/json'
}
def update_offer(API_URL, data, headers_data):
    """
    Sends a update request to the specified URL with JSON data and headers.
    """
    print(f"Attempting to PUT data to: {API_URL}")
    try:
        response = requests.put(API_URL, json=data, headers=headers_data)
        print(f"Status Code: {response.status_code}")
        print("Response Body (JSON):")
        try:
            response_json = response.json()
            print(json.dumps(response_json, indent=4))
        except ValueError:
            print("Response body is not in JSON format or is empty.")
            print(f"Raw response text: {response.text}")

        if response.status_code == 201:
            print("\nAPI Test Result: SUCCESS - Offer created successfully.")
    
        elif response.status_code == 200:
            print("\nAPI Test Result: SUCCESS - Request processed successfully (might not be a creation).")
            
        else:
            print(f"\nAPI Test Result: FAILURE - Unexpected status code {response.status_code}.")

    except requests.exceptions.RequestException as e:
        print(f"\nAPI Test Result: ERROR - A request error occurred: {e}")
if __name__ == "__main__":
    update_offer(API_URL, payload, headers)
