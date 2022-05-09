# initiate dependeancies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser_redplanet = Browser('chrome', **executable_path, headless=False)
    browser_featured_image = Browser('chrome', **executable_path, headless=False)

    # Visit https://redplanetscience.com/
    url_redplanet = "https://www.redplanetscience.com/"
    browser_redplanet.visit(url_redplanet)

    time.sleep(1)

    # Scrape page into Soup
    html_redplanet = browser_redplanet.html
    soup_redplanet = bs(html_redplanet,"html.parser")

    # Scrape latest news title and paragraph
    news_container = soup_redplanet.find("div", id="news", class_="container")

    latest_news_title = news_container.find_all('div',class_="content_title")[0].text
     
    latest_news_teaser = news_container.find_all('div',class_="article_teaser_body")[0].text

    browser_redplanet.quit()

    # Visit https://spaceimages-mars.com
    url_space_images = "https://spaceimages-mars.com"
    browser_featured_image.visit(url_space_images)

    time.sleep(1)

    # Scrape into Soup
    html_space_images = browser_featured_image.html
    soup_space_images = bs(html_space_images,"html.parser")

    # Scrape the main image
    main_image_path = soup_space_images.find_all("img")[0]["src"]
    featured_image = url_space_images + main_image_path

    # Store result in dictionary

    latest_news = {
        "title": latest_news_title,
        "teaser": latest_news_teaser,
        "featured image": featured_image}


    browser_featured_image.quit()

    return latest_news