import requests
import json

# Define the API endpoint URL
URL = "https://ms-api-gateway-qa.azurewebsites.net/offers/v1/offers"

# Define headers, including Accept to specify expected content type
HEADERS = {
    'Accept': 'application/json',
    'countryCode': 'BG',
    'Content-Type': 'application/json' # Content-Type is less common for GET but included as per request
}

def get_offers_data(url, headers):
    """
    Sends a GET request to the specified URL with custom headers
    and handles the response.
    """
    try:
        # Send the GET request with headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200-299)
        if response.status_code == 200:
            print(f"Request successful! Status Code: {response.status_code}")
            # Parse and print the JSON response
            try:
                json_response = response.json()
                print("Response JSON data:")
                # Use json.dumps for pretty printing the JSON output
                print(json.dumps(json_response, indent=4))
            except ValueError:
                print("Response content is not in JSON format.")
                print("Response text:", response.text)
        else:
            print(f"Request failed. Status Code: {response.status_code}")
            print("Response body:", response.text)

    except requests.exceptions.RequestException as e:
        # Handle exceptions like connection errors, timeouts, etc.
        print(f"An error occurred during the request: {e}")

if __name__ == "__main__":
    print(f"Attempting to fetch data from: {URL}")
    get_offers_data(URL, HEADERS)
