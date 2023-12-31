import requests
from bs4 import BeautifulSoup

recipes_dict = {}

for i in range(1, 20):
    url = f"https://eda.ru/recepty?page={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a', href=True)

    for link in links:
        div_tag = link.find('div')
        if div_tag:
            picture_tag = div_tag.find('picture')
            if picture_tag:
                img_tag = picture_tag.find('img', alt=True)
                if img_tag:
                    recipe_name = img_tag['alt']
                    recipe_link = link['href']
                    if recipe_name not in recipes_dict:
                        recipes_dict[recipe_name] = "https://eda.ru" + recipe_link

with open("recipes.txt", "w", encoding='utf-8') as f:
    for key, value in recipes_dict.items():
        f.write(f"{key}: {value} \n")
