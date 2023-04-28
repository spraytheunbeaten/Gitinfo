import requests
import json
import time
import os

print("------------------------------GitHub Account Info------------------------------ \n")
print("By SpRaY1337 \n")

username = input("Enter any GitHub username: ")
url = f'https://api.github.com/users/{username}'

print("Please wait...")

os.system("clear")


response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    name = data['name']
    bio = data['bio']
    followers = data['followers']
    following = data['following']
    public_repos = data['public_repos']
    
    print("--------------------------")
    print(f"Username: {username}")
    if name:
        print(f"Name: {name}")
    if bio:
        print(f"Bio: {bio}")
    print(f"Number of Followers: {followers}")
    print(f"Number of Following: {following}")
    print(f"Number of Public Repositories: {public_repos}")
    print("--------------------------")
    
    print("Repositories:")
    repo_url = f"https://api.github.com/users/{username}/repos"
    repo_response = requests.get(repo_url)
    
    if repo_response.status_code == 200:
        repo_data = json.loads(repo_response.text)
        for repo in repo_data:
            print(f"Name: {repo['name']}")
            print(f"Description: {repo['description']}")
            print(f"Language: {repo['language']}")
            print(f"URL: {repo['html_url']}")
            print("--------------------------")
    else:
        print("Failed to fetch repositories.")
else:
    print('Error Code:', response.status_code)
