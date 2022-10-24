import requests

# Performing an API request and saving the received response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Putting the API response in a variable
response_dict = r.json()
print(f"Total number of repositories: {response_dict['total_count']}")

# Processing information about repositories
repo_dicts = response_dict['items']
print(f"Number of repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")

for repo_dict in repo_dicts:
    print("\nSelected information about the first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
