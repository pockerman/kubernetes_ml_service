from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.service import train_service_router

DEBUG: bool = True
VERSION: str = "0.0.1"
VERSION_STR: str = "v1"
BASE_URL: str = f"/api/{VERSION_STR}"

ORIGINS: List[str] = ["http://localhost"]
ALLOW_METHODS: List[str] = ["*"]
ALLOW_HEADERS: List[str] = ["*"]

# the mir-engine application
# instance
app = FastAPI(
    title="k8s 101 service gateway",
    debug=DEBUG,
    version=VERSION,
    #]openapi_url=get_api_config().OPENAPI_URL,
    #docs_url=None,
    #redoc_url=None,
)

# CORS handling: https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)


app.include_router(info_service_router, prefix=BASE_URL)

