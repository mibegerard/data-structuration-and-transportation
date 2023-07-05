import requests

BASE_URL = "https://api.github.com"

headers = {
    'accept': 'application/vnd.github+json',
    "Authorization": "Bearer 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",
    'X-GitHub-Api-Version': "2022-11-28"
}

repos = requests.get(f"{BASE_URL}/user/repos", headers=headers)

print(len(repos.json()))
