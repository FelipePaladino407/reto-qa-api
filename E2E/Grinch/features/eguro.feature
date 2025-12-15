Feature: Operacion Grinch

      Bla bla bla, basicamente lo de "Home Alone"

  Scenario: Buscar "Home Alone" y validar diretor y rating
    Given estoy en la pagina principal de Imdb
    When busco la pelicula "Mi pobre angelito"
    And entro a la pagina de la pelicula
    Then Veo que aparece el director "Chris Columbus"
    And La pelicula tiene una calificacion superior a 7.0
    And Veo que aparece el actor "Macaulay Culkin"
