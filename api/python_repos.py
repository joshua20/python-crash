import requests

#make an api call and check the response

url="https://api.github.com/search/repositories"
url +="?q=language:python+sort:stars:>10000"

headers={"Accept": "application/vnd.github.v3+json"}
r=requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#convert the response object to a dictionary

response_dict=r.json()

#process  the results

print(response_dict.keys())
