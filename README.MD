# 📘 Horarios API

API en **FastAPI** que procesa un PDF con materias de la UFPS y devuelve un JSON organizado por **salones SA4\*\***.

---

## 🚀 Instalación local

```bash
# Clonar repositorio
git clone https://github.com/Andres-GPT/horarios-api.git
cd horarios-api

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la API en local
uvicorn app.main:app --reload
```

La API estará disponible en:

```
http://127.0.0.1:8000
```

y la documentación interactiva en:

```
http://127.0.0.1:8000/docs
```

---

## 📂 Estructura del proyecto

```
horarios-api/
├── app/
│   ├── main.py          # API principal con FastAPI
│   ├── services.py      # Funciones para extraer/parsear PDF
├── requirements.txt     # Dependencias del proyecto
├── Dockerfile           # Imagen para despliegue en Cloud Run
├── .dockerignore        # Archivos a excluir en Docker
├── .gitignore           # Archivos ignorados en Git
├── start.bat            # Script para iniciar servicio en Cloud Run
├── stop.bat             # Script para detener servicio en Cloud Run
└── README.md            # Documentación del proyecto
```

---

## 📖 Ejemplo de uso

Enviar un PDF al endpoint:

```bash
curl -X POST "http://127.0.0.1:8000/procesar-pdf" \
  -F "file=@Horarios.pdf"
```

Respuesta JSON (ejemplo):

```json
{
  "SA401": {
    "Lunes": [
      {
        "codigo": "1154104A",
        "nombre": "FUNDAMENTOS DE PROGRAMACION",
        "hora": "06:00-08:00"
      }
    ]
  }
}
```

---

## 📌 Notas

- Solo se procesan materias con código que inicia en `115`.
- Solo se consideran salones que inician en `SA4`.
