import requests
import json

# Define the API endpoint URL
API_URL = "https://ms-api-gateway-qa.azurewebsites.net/offers/v1/offers"

# Define a sample payload (replace with the actual required payload)
# The specific fields and values must be provided by the API documentation
payload = {
  "offerType": "CONDITIONAL",
  "offerCode": "Surpise live offer",
  "rewardEngineExcluded": True,
  "assignableFrom": "2025-12-13T00:00:00+02:00",
  "assignableTo": "2025-12-20T23:30:00+02:00",
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
  "offerTitle": [
    {
      "language": "bg",
      "text": "Error Validations"
    }
  ],
  "offerDescription": [
    {
      "language": "bg",
      "text": "<p><span>Error Validations</span></p>"
    }
  ],
  "customText": [
    {
      "language": "bg",
      "text": "Error Validations"
    }
  ],
  "offerBackground": "0486440c-06b3-5502-8a52-30baec795efe",
  "campaignName": "%$@%@%@%$@%$@@@",
  "offerMechanics": "JBJHGJFGFHGFGFFFFFFFFFFFFFFFHGFHDYT!YEE!%^$!%$^%!$%^!$^%!$%^@!@DGHCHCHC    ",
  "productType": "CR",
  "versionNumber": "22",
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
  ]
}


# Define headers (Content-Type is important for JSON payloads)
headers = {
    'Accept': 'application/json',
    'countryCode': 'BG',
    'Content-Type': 'application/json' # Content-Type is less common for GET but included as per request
}

def create_offer_and_validate():
    """
    Sends a POST request to create an offer and validates the response.
    """
    print(f"Attempting to send POST request to: {API_URL}")
    print(f"Request Payload: {json.dumps(payload, indent=4)}")

    try:
        # Send the POST request
        response = requests.post(API_URL, json=payload, headers=headers)

        # Print the response details
        print("\n--- Response Details ---")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")

        # --- Validation Steps ---

        # 1. Validate the status code
        # A successful creation typically returns a 201 Created or 200 OK
        expected_status_code = 201 
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        print(f"\nValidation 1 Passed: Correct status code {expected_status_code} received.")

        # 2. Validate the response body content (if it returns JSON)
        try:
            response_json = response.json()
            assert "offerId" in response_json, "Response body missing expected 'offerId' field"
            assert "status" in response_json, "Response body missing expected 'status' field"
            assert "offerCode" in response_json, "offerCode in response does not match request"
            assert response_json['offerCode'] == payload['offerCode'], "offerCode in response does not match request"
            print("Validation 2 Passed: Response body contains expected fields and values.")

        except json.JSONDecodeError:
            print("Validation 2 Failed: Response body is not a valid JSON.")
        except AssertionError as e:
            print(f"Validation 2 Failed: {e}")

    except requests.exceptions.RequestException as e:
        print(f"\nAn error occurred during the request: {e}")

if __name__ == "__main__":
    create_offer_and_validate()
