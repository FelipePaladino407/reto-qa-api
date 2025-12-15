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

    #def has_actor(self, actor_name: str) -> bool:
     #   cast_section = '[data-testid="title-cast"]'

      #  try:    
       #     self.page.wait_for_selector(cast_section, timeout=8000)
        #except:
         #   return False

        #actors = self.page.locator(f'{cast_section} a[href^="/name/"]')
        #count = actors.count()
        #for i in range(count):
         #   name = actors.nth(i).inner_text().strip()
          #  if actor_name.lower() in name.lower():
           #     return True
        #return False
    
    def has_actor(self, actor_name: str) -> bool:
        xpath = (
            f'//section[@data-testid="title-cast"]'
            f'//a[starts-with(@href,"/name/") and contains('
            f'translate(normalize-space(.), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"),'
            f'"{actor_name.lower()}")]'
        )

        return self.page.locator(xpath).count() > 0
    
