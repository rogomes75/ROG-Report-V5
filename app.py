```python

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

import uvicorn

import os

import logging

# Configure logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = FastAPI(title="ROG Pool Service API")

@app.get("/")

def root():

return {

"message": "🏊‍♂️ ROG Pool Service - Sistema de Gestão de Piscinas",

"status": "success",

"version": "3.0",

"platform": "render",

"mongodb": "will_be_added_next",

"features": [

"Client Management (Coming Soon)",

"Service Reports (Coming Soon)",

"Photo Upload Support (Coming Soon)",

"Status Tracking (Coming Soon)"

]

}

@app.get("/health")

def health():

return {

"status": "healthy",

"service": "rog-pool-service",

"version": "3.0",

"port": os.environ.get("PORT", "8000"),

"platform": "render"

}

@app.get("/api/")

def api_root():

return {

"message": "ROG Pool Service API v3.0",

"platform": "render",

"status": "basic_version_working",

"endpoints": ["/", "/health", "/api/", "/html"]

}

@app.get("/html", response_class=HTMLResponse)

def html_interface():

return """

<!DOCTYPE html>

<html>

<head>

<title>ROG Pool Service - Sistema de Gestão</title>

<meta charset="UTF-8">

<style>

body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }

.container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }

h1 { color: #2c3e50; text-align: center; }

.status { padding: 15px; border-radius: 5px; margin: 20px 0; text-align: center; background: #d4edda; color: #155724; }

.endpoint { background: #e3f2fd; padding: 10px; margin: 5px 0; border-radius: 5px; }

.endpoint a { text-decoration: none; color: #1976d2; font-weight: bold; }

</style>

</head>

<body>

<div class="container">

<h1>🏊‍♂️ ROG Pool Service</h1>

<h2>Sistema de Gestão de Piscinas v3.0</h2>


<div class="status">

<h3>✅ RENDER DEPLOY SUCCESSFUL!</h3>

<p>Plataforma: <strong>Render</strong> | Versão: <strong>3.0</strong></p>

</div>


<h3>🔗 API Endpoints:</h3>

<div class="endpoint">

<a href="/">🏠 Homepage</a> - Informações do sistema

</div>

<div class="endpoint">

<a href="/health">🏥 Health Check</a> - Status detalhado

</div>

<div class="endpoint">

<a href="/api/">🔗 API Root</a> - Informações da API

</div>


<h3>📋 Próximas Funcionalidades:</h3>

<ul>

<li>⏳ Integração MongoDB</li>

<li>⏳ Gestão de Clientes</li>

<li>⏳ Relatórios de Serviço</li>

<li>⏳ Upload de Fotos</li>

<li>⏳ Sistema de Autenticação</li>

</ul>


<h3>🎉 Status Atual:</h3>

<p><strong>✅ Base do sistema funcionando perfeitamente no Render!</strong></p>

<p>MongoDB será adicionado na próxima etapa.</p>

</div>

</body>

</html>

"""

# Start server

if __name__ == "__main__":

port = int(os.environ.get("PORT", 8000))

logger.info(f"🚀 Starting ROG Pool Service on port {port}")

uvicorn.run(app, host="0.0.0.0", port=port)

# Auto-start in production

try:

port = int(os.environ.get("PORT", 8000))

if port != 8000:

logger.info(f"🚀 Auto-starting on Render port {port}")

uvicorn.run(app, host="0.0.0.0", port=port)

except:

pass

```
