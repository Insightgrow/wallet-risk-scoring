import requests

url = "https://api.llama.fi/protocols"
response = requests.get(url)

if response.status_code == 200:
    protocols = response.json()
    print("🔎 Matching protocols that mention 'compound':\n")
    for protocol in protocols:
        if "compound" in protocol["slug"].lower():
            print(f"Name: {protocol['name']}, Slug: {protocol['slug']}")
else:
    print("Failed to fetch protocol list.")
