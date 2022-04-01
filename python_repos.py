import requests

# Wykonanie rzadania API i zachowanie otrzymanej odpowiedzi
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")

# Umieszczenie odpowiedzi API w zmiennej
response_dict = r.json()
print(f"Calkowita liczba repozytoriow: {response_dict['total_count']}")

# Przetworzenie informacji o repozytoriach
repo_dicts = response_dict['items']
print(f"Liczba zwroconych repozytoriow: {len(repo_dicts)}")

print("\nWybrane informacje o kazdym repozytorium:")

for repo_dict in repo_dicts:
    print("\nWybrane informacje o pierwszym repozytorium:")
    print(f"Nazwa: {repo_dict['name']}")
    print(f"Wlasciciel: {repo_dict['owner']['login']}")
    print(f"Gwiazdki: {repo_dict['stargazers_count']}")
    print(f"Repozytororium: {repo_dict['html_url']}")
    print(f"Utworzone: {repo_dict['created_at']}")
    print(f"Uaktualnione: {repo_dict['updated_at']}")
    print(f"Opis: {repo_dict['description']}")
