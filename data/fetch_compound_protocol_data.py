import requests
import json

def fetch_compound_data():
    url = "https://api.llama.fi/protocol/compound-v2"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open("data/compound_protocol_data.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Protocol data saved to data/compound_protocol_data.json")
    else:
        print(f" Failed to fetch data: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    fetch_compound_data()
