from playwright.sync_api import Page

class ImdbHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = 'input[name="q"]'
        self.search_button = 'button[type="submit"]'
        self.first_title_result = (
            'section[data-testid="find-results-section-title"] a[href^="/title/"]'
        )

    def search_movie(self, movie_name: str):
        self.page.fill(self.search_box, movie_name)
        self.page.keyboard.press("Enter")

        # Esperar a que cargue la página de resultados:
        self.page.wait_for_load_state("domcontentloaded")

        # Esperar a que existan resultados de títulos:
        self.page.wait_for_selector(self.first_title_result, timeout=15000)

        # Click al primer título:
        self.page.locator(self.first_title_result).first.click()

        # Esperar a que cargue el título (URL contiene /title/):
        self.page.wait_for_url("**/title/**", timeout=15000)
    
