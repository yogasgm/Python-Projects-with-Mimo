import requests

def fetch_data(option):
  url = f"https://swapi.mimo.dev/api/{option}/"

  data = []
  try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print(f"Successfully fetched {len(data)} data.")
  except requests.HTTPError as e:
    print(f"Error: {e}")
    return None
  return data


option = input("What StarWars data you'd like to explore? ").strip().lower()
data = fetch_data(option)

if data:
  for item in data:
    print(item['name'])
else:
  print("Unable to download data")