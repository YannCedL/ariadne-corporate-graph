"""
FastAPI REST server for Ariadne Corporate Graph Engine.
"""

from fastapi import FastAPI
from genesis_core import ResultContract
from .graph import build_company_graph

app = FastAPI(
    title="Ariadne Corporate Graph API",
    description="Corporate Ownership & Subsidiary Graph OSINT Engine",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Ariadne", "version": "1.0.0"}

@app.get("/api/v1/graph/{siren}", response_model=ResultContract)
def get_graph(siren: str):
    return build_company_graph(siren)
