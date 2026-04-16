import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .graph import build_company_graph

app = FastAPI(
    title="Ariadne Corporate Graph API",
    description="Moteur de Graphe d'Actionnariat et Filiales",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert directement la page web d'interface graphe
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Ariadne API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Ariadne", "version": "1.0.0"}

@app.get("/api/v1/graph/{siren}", response_model=ResultContract)
def get_graph(siren: str):
    return build_company_graph(siren)
