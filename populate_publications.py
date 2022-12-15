import requests #Requires pip install requests
import json

#This file deals with the SerpAPI request and saves those to a temp file

URL = "https://serpapi.com/search.json?engine=google_scholar_author"

scholar_id = "0OupgU0AAAAJ" #MKhamis Author ID
api_key = "90241054b897df69d69b36eff0e50d29064f3e85f5784131f02fcf0e81ab484f" #SerpAPI private key
num_results = "100"
sort = "pubdate" #Get most recent publications

query_URL = URL + "&author_id=" + scholar_id + "&api_key=" + api_key + "&num=" + num_results + "&sort=" + sort

r = requests.get(url = query_URL)

data = r.json()

out_file = open("temp.json", "w")

json.dump(data['articles'], out_file, indent=2)

out_file.close()
