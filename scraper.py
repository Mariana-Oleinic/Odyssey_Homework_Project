from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def extract_movie_data_for_year(year: int) -> list:
    """Fetch the most popular movies in a given year

    Args:
        year (int): the year for which to fetch the most popular movies

    Returns:
        list: the most popular movies in the given year
    """
    url = f'https://www.google.com/search?q=popular+movies+in+{year}'
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)
            content = page.content()
            soup = BeautifulSoup(content, 'html.parser')
            movies_raw_data = soup.select('.FozYP')
            movies_text_data = [item.get_text(strip=True) for item in movies_raw_data]
            return movies_text_data
