#%%

#Using Github’s API, create a function that:
#• takes all repositories from your account
#• prints a short description of each repository, with its 
#  name, number of stars, main language, and url

import requests 

def get_repos(user):

    url = "https://api.github.com/users/" + user + "/repos" 
    
    user_repos = requests.get(url).json()
    
    list_repos = []
    number_of_repos = 0
    
    for repo in user_repos:
        number_of_repos += 1
        list_repos.append(repo["name"])
        list_repos.append(repo["stargazers_count"])
        list_repos.append(repo["language"])
        list_repos.append(repo["url"])
            
    length = len(list_repos)
    s = length//number_of_repos
    return [list_repos[p:p+s] for p in range(0, length, s)]

get_repos("javierfdz10")

#%%

def get_repos_2(user):
    
    url = "https://api.github.com/users/" + user + "/repos"
    
    response = requests.get(url)
    
    repos = response.json()
    
    repos_list = []
    
    for repo in repos :
        repo_to_add = {"Name":repo["name"],
                       "Stars": repo["stargazers_count"],
                       "Language":repo["language"],
                       "URL":repo["url"]}
        repos_list.append(repo_to_add)
    
    return repos_list
    
get_repos_2("javierfdz10")

#%%