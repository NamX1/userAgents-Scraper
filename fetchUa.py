import requests
from bs4 import BeautifulSoup

def save_file(ua):
    with open("./ua.txt", 'a') as file:
        file.write(ua + "\n")

def fetch_user_agents():
    browsers = ['Firefox', 'Chrome']

    for browser in browsers:
        url = f'http://www.useragentstring.com/pages/useragentstring.php?name={browser}'
        response = requests.get(url)

        if response.status_code == 200:
            print(f"Fetching user agents for {browser}: {response.status_code}")
            soup = BeautifulSoup(response.content, "html.parser")
            div = soup.find('div', {'id': 'liste'})
            links = div.findAll('a')

            for link in links:
                user_agent = link.text
                save_file(user_agent)
        else:
            print(f"Unable to fetch user agents for {browser}: {response.status_code}")

if __name__ == "__main__":
    fetch_user_agents()
    print("User agents have been fetched and saved to ua.txt.")
