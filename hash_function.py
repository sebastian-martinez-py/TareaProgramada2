def hash_function(fecha: str, cuarto: int, equipo: str) -> int:
    date_value = sum(ord(c) for c in fecha if c.isdigit())
    team_value = sum(ord(c) for c in equipo)
    return (date_value + cuarto + team_value) % 750


 #
   #Función hash personalizada basada en los datos de la jugada.
    # Convierte la fecha en un número.
   #- Usa el cuarto del partido.
    # Suma los valores ASCII del nombre del equipo.
   #- Aplica una operación modular para ajustarlo a 750 registros.
#