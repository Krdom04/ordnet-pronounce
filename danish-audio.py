from bs4 import BeautifulSoup
import requests
import webbrowser
import re


def remove_numbers(s):
    return re.sub(r'\d', '', s)

URL = "https://ordnet.dk/ddo/ordbog?query="
URL_end = ""

while True:
    word = input("Enter the danish word: ")
    main_url = URL + word + URL_end

    req = requests.get(main_url)
    soup = BeautifulSoup(req.content, "html.parser")
    print(soup.prettify())

    word_found = soup.find('div', class_="definitionBoxTop").find('span', class_="match").text
    pron_box = soup.find('div', class_="definitionBox details")
    ipa = pron_box.find('span', class_="lydskrift").text.replace("[", '').replace("]", '')
    audio = pron_box.find('audio').find('a')['href']
    word_found = remove_numbers(word_found)
    print(word_found)
    print(ipa)
    print(main_url)
    webbrowser.open(audio)