from serpapi.google_search import GoogleSearch
from serpapi.serp_api_client import *
params = {
  "engine": "google",
  "q": "Coffee",
  "api_key": "d3301d7caa6f31e3941a71456064b9f5d39fa76714f79e43538a8a73d0f1f499"
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]
print(search)
print("\n")
print(results)
print("\n")
print(organic_results)