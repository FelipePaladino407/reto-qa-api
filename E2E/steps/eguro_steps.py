from behave import given, when, then
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_title_page import ImdbTitlePage

@given('estoy en la pagina principal de Imdb')
def step_impl(context):
    context.page.goto('https://www.imdb.com', wait_until="domcontentloaded")
    context.home_page = ImdbHomePage(context.page)

@when('busco la pelicula "{movie_name}"')
def step_impl(context, movie_name):
    context.home_page.search_movie(movie_name)
    context.title_page = ImdbTitlePage(context.page)  

@when('entro a la pagina de la pelicula')
def step_impl(context):
    # Por si las moscas, un assert (auqneu ya deberia de haber entrado con el primer click):
    assert "/title/" in context.page.url

@then('Veo que aparece el director "{director_name}"')
def step_impl(context, director_name):
    director = context.title_page.get_director()
    assert director_name.lower() in director.lower(), (
        f"Se esperaba {director_name}, pero fue {director}"
    )

@then('La pelicula tiene una calificacion superior a {min_rating}')
def step_impl(context, min_rating):
    rating = context.title_page.get_rating()
    assert rating > float(min_rating), f"La calificación ({rating}) es menor que {min_rating}"

@then('guardo una captura de pantalla')
def step_impl(context):
    context.page.screenshot(path="evidencia_imdb.png", full_page=True)


