from fastapi import FastAPI
from catalogue.api.routes_catalogue import router as catalogue_router
from catalogue.api.routes_seller import router as seller_router

def create_app() -> FastAPI:
    app = FastAPI(title="Carlux Catalogue Service", version="0.1.0")
    app.include_router(catalogue_router, prefix="/catalogue", tags=["catalogue"])
    app.include_router(seller_router, prefix="/seller", tags=["seller"])
    return app

app = create_app()
