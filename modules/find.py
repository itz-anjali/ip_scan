import requests


website = "https://www.dais.edu.in/"  # set url a/c to you 
pages_to_check = ["admin", "login", "secret", "dashboard"]

for page in pages_to_check:
    url = website + page
    r = requests.get(url)
    
    if r.status_code == 200:
        print(f"[+] FOUND! {url} found it (200)!")
    else:
        print(f"[-] {url} not found (404).")