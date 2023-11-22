from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Dict
from loguru import logger

info_service_router = APIRouter(prefix="/info", tags=["info"])

SERVICES = ['service_1', 'service_2']
VERSION_STR: str = "v1"
BASE_URL: str = f"/api/{VERSION_STR}"
SERVICE_NAME = "info"

# the names should correspond to Kubernetes services
SERVICE_TO_HOST_MAP={'service_1': "http://ml-service1",
                     'service_2': "http://ml-service2"}


@info_service_router.on_event("startup")
async def on_startup() -> None:
    """Actions on starting up the service

    Returns
    -------

    """

    # make checks

    logger.info(f"Start-up for {SERVICE_NAME} service...")
    logger.info("Done...")


@info_service_router.get("/",
                    response_model=Dict[str, str])
def root() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Hello from Kubernetes 101 service"})


@info_service_router.get(
    "/services",
    summary="Returns a list of the available models",
    response_model=List[str],
)
async def get_services() -> JSONResponse:
    """

    Parameters
    ----------
    Returns
    -------

    JSONResponse with a list of the available service
    """

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=["predict", "train", "deploy", "dataset"])