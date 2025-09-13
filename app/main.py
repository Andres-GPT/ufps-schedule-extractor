"""
main.py
--------
API en FastAPI para procesar un PDF de horarios.
Recibe un archivo PDF y devuelve un JSON con los salones SA4** y sus horarios.
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.services import extraer_tabla_pdf, parsear_materias

# Crear la aplicación FastAPI
app = FastAPI(
    title="📘 Horarios API",
    description="""
API que procesa un PDF de materias y devuelve un JSON organizado por los salones de Aula Sur (SA4**).  

### Funcionalidades
- Subir un archivo PDF.
- Extraer materias con código `115`.
- Organizar por salones (solo SA4**).
- Agrupar por días de la semana.

### Tecnologías
- **FastAPI**  
- **pdfplumber**  
""",
)


# Configurar CORS (por si luego la consumes desde un frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # puedes restringir a tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/procesar-pdf", tags=["Procesamiento de PDF"])
async def procesar_pdf(file: UploadFile = File(...)):
    """
    Sube un PDF y devuelve un JSON con las materias filtradas.

    - **file**: archivo PDF a procesar
    - Devuelve: JSON con materias, horarios y salones SA4**
    """
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="El archivo debe ser un PDF.")

    try:
        filas = extraer_tabla_pdf(file.file)
        salones = parsear_materias(filas)
        return salones
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el PDF: {e}")
