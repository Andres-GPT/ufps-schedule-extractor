"""
services.py
------------
Módulo que contiene las funciones para:
1. Extraer tablas de un PDF usando pdfplumber.
2. Parsear materias filtrando solo salones SA4**.
3. Ordenar salones y días de la semana.
"""

import pdfplumber
import re


def extraer_tabla_pdf(archivo_stream):
    """
    Extrae todas las tablas de un PDF y devuelve una lista de filas.

    :param archivo_stream: archivo PDF abierto (stream)
    :return: lista de filas (listas de strings)
    """
    filas = []
    with pdfplumber.open(archivo_stream) as pdf:
        for pagina in pdf.pages:
            tabla = pagina.extract_table()
            if tabla:
                filas.extend(tabla)
    return filas


def parsear_materias(filas):
    salones = {}
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]

    for fila in filas:
        if not fila or len(fila) < 7:
            continue

        codigo = fila[0].strip()
        if not codigo.startswith("115"):  # solo materias con código 115
            continue

        codigo_prof = fila[3].strip() if fila[3] else ""  # <-- NUEVO
        nombre = fila[5].strip()

        for i, dia in enumerate(dias_semana, start=6):
            if (
                i < len(fila)
                and fila[i]
                and re.search(r"\d{2}:\d{2}-\d{2}:\d{2}", fila[i])
            ):
                partes = fila[i].split()
                hora = partes[0] if partes else ""
                salon = partes[1] if len(partes) > 1 else ""

                if not salon.startswith("SA4"):
                    continue

                if salon not in salones:
                    salones[salon] = {}

                if dia not in salones[salon]:
                    salones[salon][dia] = []

                salones[salon][dia].append(
                    {
                        "codigo": codigo,
                        "codigo_p": codigo_prof,  # <-- SE AGREGA AQUÍ
                        "nombre": nombre,
                        "hora": hora,
                    }
                )

    # Ordenar salones y días
    salones_ordenados = dict(
        sorted(
            salones.items(), key=lambda x: int(re.search(r"SA4(\d+)", x[0]).group(1))
        )
    )
    for salon, dias in salones_ordenados.items():
        salones_ordenados[salon] = {
            dia: dias[dia] for dia in dias_semana if dia in dias
        }

    return salones_ordenados
