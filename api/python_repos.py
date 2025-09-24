import requests
import plotly.express as px
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


print(f"total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

#explore information about the repositories

repo_dicts=response_dict['items']
print(f"repositories returned: {len(repo_dicts)}")

#examine the first repository
repo_dict=repo_dicts[0]

print(f"\nKeys: {len(repo_dict)}")

for key in sorted(repo_dict.keys()):
    print(key)

#process repositry information
repo_names,stars=[],[]

for repo_dict in repo_dicts:

    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
print(repo_names)
print(stars)
#make visualization
labels={'x':"repositories", "y":"stars"}
title="Most-starred projects on Github"
fig=px.bar(x=repo_names, y=stars,labels=labels,title=title)
fig.write_html("repo_names.html")
