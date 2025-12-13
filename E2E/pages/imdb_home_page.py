from playwright.sync_api import Page

class ImdbHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = 'input[name="q"]'
        self.search_button = 'button[type="submit"]'

    def search_movie(self, movie_name: str):
        self.page.fill(self.search_box, movie_name)
        self.page.click(self.search_button)
        self.page.wait_for_function()
    
