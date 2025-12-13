from playwright.sync_api import Page

class ImdbTitlePage:
    def __init__(self, page: Page):
        self.page = page
        self.director_selector = 'span[itemprop="director`"]'
        self.rating_director = 'span[itemprop="ratingValue"]'

    def get_director(self):
        return self.page.inner_text(self.director_selector)

    def get_rating(self):
        return float(self.page.inner_text(self.rating_director))
