from playwright.sync_api import page

def before_scenario(context, scenenario):
    #"Segun la pagina 'medium.com', esto es para inicializar playwright antes de cualquier test"
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False) 
    context.page = context.browser.new_page()

# Y ahora para despues de each scenario:
def after_scenario(context, scenenario):
    context.page.close()
    context.browser.close()
    context.playwright.stop()
