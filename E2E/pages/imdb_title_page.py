from playwright.sync_api import Page

class ImdbTitlePage:
    def __init__(self, page: Page):
        self.page = page

        # EL BLOQUE DE CREDITOS INICIAL: ahi esta el director:
        self.principal_credit = 'li[data-testid="title-pc-principal-credit"]'

        # Rating (uuuu):
        self.rating_value = '[data-testid="hero-rating-bar__aggregate-rating__score"] span'

    def get_director(self) -> str:
        self.page.wait_for_selector(self.principal_credit, timeout=15000)

        # Busca dentro del bloque el primer link a /name/ (director):
        credit = self.page.locator(self.principal_credit).first
        director_link = credit.locator('a[href^="/name/"]').first
        return director_link.inner_text().strip()

    def get_rating(self) -> float:
        self.page.wait_for_selector(self.rating_value, timeout=15000)

        # Score:
        text = self.page.locator(self.rating_value).first.inner_text().strip()
        return float(text.replace(",", "."))

