import numpy as np
from fastapi import APIRouter, status, HTTPException, Body
from fastapi.responses import JSONResponse
from typing import List, Dict, Union
from loguru import logger
import pickle
from pathlib import Path

from .predict_request_schema import PredictRequestData
from .config import MODEL_DIR

serve_service_router = APIRouter(prefix="/serve", tags=["info"])

SERVICES = ['service_1', 'service_2']
VERSION_STR: str = "v1"
BASE_URL: str = f"/api/{VERSION_STR}"
SERVICE_NAME = "serve"

# the names should correspond to Kubernetes services
SERVICE_TO_HOST_MAP={'service_1': "http://ml-service1",
                     'service_2': "http://ml-service2"}

# this should be provided by a model registry
iris_logreg_model_filename = Path('./artifacts/iris_logreg_model.sav')

target_name = {0: 'setosa', 1: 'versicolor', 2:  'virginica'}


@serve_service_router.on_event("startup")
async def on_startup() -> None:
    """Actions on starting up the service

    Returns
    -------

    """

    # make checks

    logger.info(f"Start-up for {SERVICE_NAME} service...")
    logger.info("Done...")


@serve_service_router.get("/",
                    response_model=Dict[str, str])
def root() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Hello from Kubernetes 101 service"})

@serve_service_router.get("/models")
async def get_models(deployed: bool=True) -> JSONResponse:
    """Returns all the models the serve service handles.
    If the deployed flag is true it only returns the deployed models.
    Typically, we wany to use a model registry here

    :param deployed:
    :return:
    """

    pass



@serve_service_router.post(
    "/predict",
    summary="Returns a list of the available models",
    response_model=Dict[str, Union[str, float]],
)
async def get_prediction(request_data:PredictRequestData = Body(...)) -> JSONResponse:
    """

    Parameters
    ----------
    Returns
    -------

    JSONResponse with a list of the available service
    """

    # load the model
    model = pickle.load(open(MODEL_DIR / iris_logreg_model_filename, 'rb'))

    input_data = np.asarray([request_data.sepal_length,
                             request_data.sepal_width]).reshape(1, -1)
    # get the class label
    prediction = model.predict(input_data)[0]

    class_name = target_name[prediction]

    probability = model.predict_proba(input_data)[0][prediction]
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"class": class_name, "probability": probability})