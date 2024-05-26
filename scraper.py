from bs4 import BeautifulSoup
import requests

def scrape_date(date):
    # generate URL
    baseUrl = 'https://www.billboard.com/charts/hot-100/' + date + '/'
    print(baseUrl)
    
    # send scrape request
    response = requests.get(baseUrl)
    
    # begin scraping
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # grab correct selectors
    songs = soup.select("li ul li h3")
    
    # generate list of songs and return it
    song_list = [song.getText().strip() for song in songs]
    
    return song_list