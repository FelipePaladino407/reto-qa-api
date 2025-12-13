FEATURE: Operacion Grinch

      Bla bla bla, basicamente lo de "Home Alone"

  SCENARIO:
    GIVEN Estoy en IMBd
    WHEN Busco "Home Alone"
    THEN Me aparece como primera opcion "Home Alone 1990".
    WHEN Hago click en la pelicula vista.
    THEN Me redirije a la pagina en donde se encuentra.
    WHEN Estoy en la pagina de la pelicula
    THEN Veo que aparece el director "Chris Columbus"
    AND La pelicula tiene una calificacion superior a 7.0
