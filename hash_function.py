def hash_function(fecha: str, cuarto: int, equipo: str) -> int:
    date_value = sum(ord(c) for c in fecha if c.isdigit())
    team_value = sum(ord(c) for c in equipo)
    return (date_value + cuarto + team_value) % 750


#Se utiliza un Hash basico de suma de caracteres para facilitar la aplicacion de la misma, aplica una operacion modular par ajusatrlo a 750 registros,
#Usa el cuarto del partido y Suma los valores ASCII del nombre del equipo.

