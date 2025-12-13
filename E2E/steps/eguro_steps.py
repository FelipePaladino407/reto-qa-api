from behave import given, when, then
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_title_page import ImdbTitlePage

@given('estoy en la pagina principal de Imdb')
def step_impl(context):
    context.page.goto('https://www.imdb.com')
    context.home_page = ImdbHomePage(context.page)  # Creo instancia de la pagina pricinial uuu

@when('busco la pelicula "{movie_name}"')
def step_impl(context, movie_name):
    context.home_page.search_movie(movie_name)  # Usao el método de la página principal

@when('entro a la pagina de la pelicula')
def step_impl(context):
    context.title_page = ImdbTitlePage(context.page)  # Creo la instancia de la pagina del coso este

@then('veo que aparece el director "{director_name}"')
def step_impl(context, director_name):
    director = context.title_page.get_director()  # Obtener el director
    assert director_name.lower() in director.lower(), f"Se esperaba que el director fuera {director_name}, pero fue {director}"

@then('la pelicula tiene una calificacion superior a {min_rating}')
def step_impl(context, min_rating):
    rating = context.title_page.get_rating()  # Obtener la calificación
    assert rating > float(min_rating), f"La calificación ({rating}) es menor que {min_rating}"


