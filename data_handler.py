
import os
import struct
import csv
from hash_function import hash_function
from punt_play import PuntPlay

FILE_NAME = "info.dat"
NUM_RECORDS = 750
RECORD_FORMAT = "50s50s50s50s50s50s"  
RECORD_SIZE = struct.calcsize(RECORD_FORMAT)

def inicializar_archivo():
    """Verifica si el archivo existe, si no, lo crea con 750 registros vacíos."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "wb") as f:
            empty_record = struct.pack(RECORD_FORMAT, b"", b"", b"", b"", b"", b"")
            for _ in range(NUM_RECORDS):
                f.write(empty_record)

def cargar_datos(nombre_archivo):
    """Carga datos desde el archivo CSV ingresado por el usuario y almacena en la tabla hash."""
    if not os.path.exists(nombre_archivo):
        print(f"No se encontró el archivo: {nombre_archivo}")
        return

    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')  # Usa punto y coma como separador
        next(reader, None)  # Saltar encabezado si existe
        for row in reader:
            if len(row) < 9:  # Verifica que la fila tenga al menos 9 columnas
                print(f"Error: fila con formato incorrecto -> {row}")
                continue  # Saltar la fila y continuar con la siguiente

            # Extraer solo las columnas necesarias
            game_id = row[3]  # Columna D
            teams = row[4]    # Columna E
            yards = row[5]    # Columna F
            qtr = row[6]      # Columna G
            date = row[7]     # Columna H
            time = row[8]     # Columna I

            # Crear objeto PuntPlay y almacenar en el archivo hash
            punt_play = PuntPlay(game_id, teams, yards, int(qtr), date, time)
            almacenar_registro(punt_play)

def almacenar_registro(punt_play: PuntPlay):
    """Almacena un registro en el archivo hash, manejando colisiones si es necesario."""
    key = hash_function(punt_play.date, punt_play.qtr, punt_play.teams)
    packed_data = struct.pack(RECORD_FORMAT,
                              punt_play.game_id.encode(),
                              punt_play.teams.encode(),
                              punt_play.yards.encode(),
                              str(punt_play.qtr).encode(),
                              punt_play.date.encode(),
                              punt_play.time.encode())
    
    with open(FILE_NAME, "r+b") as f:
        f.seek(key * RECORD_SIZE)
        existing_data = f.read(RECORD_SIZE)
        
        if not any(existing_data):  # Si el registro está vacío, escribir directamente
            f.seek(key * RECORD_SIZE)
            f.write(packed_data)
        else:  # Colisión
            collision_file = f"{key}-col.dat"
            with open(collision_file, "ab") as cf:
                cf.write(packed_data)

def buscar_datos(key: int):
    """Busca un registro en el archivo hash y en los archivos de colisión."""
    if key < 0 or key >= NUM_RECORDS:
        print("Llave fuera de rango.")
        return
    
    with open(FILE_NAME, "rb") as f:
        f.seek(key * RECORD_SIZE)
        data = f.read(RECORD_SIZE)
        
        if any(data):
            record = struct.unpack(RECORD_FORMAT, data)
            clean_record = [field.decode('utf-8').strip("\x00") for field in record]
            
            # Extraer solo el equipo local (después del '@')
            teams = clean_record[1]  # Posición del campo teams
            home_team = teams.split('@')[-1] if '@' in teams else teams  # Obtiene solo el equipo local
            
            # Mostrar el resultado con solo el equipo local
            clean_record[1] = home_team  # Reemplaza el campo completo con solo el equipo local
            print(f"Registro encontrado en info.dat:", clean_record)
        else:
            print("Registro vacío en info.dat.")

    # Verificar archivo de colisiones
    collision_file = f"{key}-col.dat"
    if os.path.exists(collision_file):
        print(f"Existen colisiones en {collision_file}, mostrando registros adicionales:")
        with open(collision_file, "rb") as cf:
            while chunk := cf.read(RECORD_SIZE):
                record = struct.unpack(RECORD_FORMAT, chunk)
                clean_record = [field.decode('utf-8').strip("\x00") for field in record]
                
                # Extraer solo el equipo local
                teams = clean_record[1]
                home_team = teams.split('@')[-1] if '@' in teams else teams
                
                clean_record[1] = home_team  # Reemplaza el campo completo con solo el equipo local
                print(clean_record)
    else:
        print("No existen colisiones.")

def listar_llaves():
    """Lista las llaves que contienen datos en info.dat y en archivos de colisión."""
    llaves_encontradas = []

    with open(FILE_NAME, "rb") as f:
        for key in range(NUM_RECORDS):
            f.seek(key * RECORD_SIZE)
            data = f.read(RECORD_SIZE)
            
            if any(data):  # Si hay algún dato en la posición, se considera ocupada
                llaves_encontradas.append(key)

    print(f"Llaves con datos en info.dat: {llaves_encontradas}")

    llaves_colision = []
    for file in os.listdir():
        if file.endswith("-col.dat"):
            llave = file.split("-")[0]  # Extrae la llave del nombre del archivo
            llaves_colision.append(int(llave))

    print(f"Llaves con colisiones: {sorted(llaves_colision)}")