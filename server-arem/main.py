from fastapi import FastAPI
from controllers import url_controller

app = FastAPI(title="Arem URL Shortener")

# Registrar rutas
app.include_router(url_controller.router)

# Ruta raíz de prueba
@app.get("/")
def read_root():
    return {"message": "Backend Arem listo!"}