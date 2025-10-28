import requests
import json
hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyyntö).json()
for vastau in vastaus:
    print(vastau["show"]["genres"])

#käytetään lähinnä koko vastausken muotoilua varten
#print(json.dumps(vastaus, indent=2))