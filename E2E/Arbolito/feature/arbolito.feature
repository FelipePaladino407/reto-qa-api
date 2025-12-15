Feature: Armando el arbolito
  Simular la compra de decoraciones navideñas

  Scenario: Buscar decoraciones y agregar 2 productos al carrito
    Given estoy en la tienda online "https://www.christmascentral.com/"
    When busco "christmas decorations"
    And agrego 2 productos distintos al carrito
    And voy al carrito
    Then veo 2 items en el carrito
    And el subtotal es la suma de los items
    And guardo una captura del carrito

