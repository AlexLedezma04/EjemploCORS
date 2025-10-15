## FastAPI - Middleware de Validación de User-Agent y CORS

Este trabajo es un ejemplo básico de una API desarrollada con **FastAPI**, que incluye:

* Middleware para bloquear peticiones desde navegadores móviles.
* Configuración de **CORS** para desarrollo local.
* Endpoints simples de prueba.

---

### Requisitos

* Python 3.8+
* Entorno virtual creado y activado 
* `uvicorn`, `fastapi` y dependencias ya instaladas

---

### Cómo correr la app

Desde la raíz del proyecto, ejecuta:

```bash
uvicorn app:app --reload
```

---

### Rutas disponibles

#### `GET /`

**Descripción:** Ruta raíz de prueba
**Respuesta:**

```text
"abrir"
```

---

#### `GET /api/personas`

**Descripción:** Devuelve un objeto JSON con datos de una persona de prueba
**Respuesta esperada:**

```json
{
  "id": "123123123",
  "Nombre": "Ejemplo API",
  "Telefono": 69696969
}
```

**Nota:** Esta ruta bloquea peticiones si el `User-Agent` contiene la palabra `"Mobile"`.

---

### Middleware de validación

Este middleware analiza el `User-Agent` de cada petición. Si detecta que proviene de un navegador móvil (contiene `"Mobile"`), se bloquea con un `401 Unauthorized`.

---

### CORS

Se permite el acceso solamente desde los siguientes orígenes:

* `http://localhost`
* `http://localhost:8080`

Esto facilita el testing desde el front en local.

---

### Comandos curl de prueba

Acceso autorizado:

```bash
curl -i -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" http://localhost:8000/api/personas
```

Acceso NO autorizado (dispositivo móvil simulado):

```bash
curl -i -H "User-Agent: Mobile Safari" http://localhost:8000/api/personas
```
