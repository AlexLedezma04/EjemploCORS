from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from fastapi import FastAPI

app = FastAPI()

# Dominios Definidos
origins = [
    "http://localhost",
    "http://localhost:8080",
]

#Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def verificar_agente_usuario(request: Request, call_next):
    user_agent = request.headers.get("User-Agent", "")
    if user_agent.find("Mobile") == -1:
        response = await call_next(request)
        return response
    else:
        return JSONResponse(content={
            "message": "Error"
        }, status_code=401)
    
@app.get("/")
def main():
    return "abrir"


@app.get("/api/personas")
def personas():
    return JSONResponse(content={
        
            "id": "123123123",
            "Nombre": "Ejemplo API",
            "Telefono": 69696969,
            
        }, status_code=200)

# Comandos para probar la funcionalidad del ejercicio

# uvicorn app:app --reload (Inicia el servidor)

# curl -i http://localhost:8000/

# curl -i -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" http://localhost:8000/api/personasersonas (AUtorizado)

# curl -i -H "User-Agent: Mobile Safari" http://localhost:8000/api/personas (No Autorizado)
