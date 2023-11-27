# pull the official docker image
FROM python:3.10

# set the working directory inside the container
WORKDIR /service

# copy the functionality

COPY ./service    /service/service
COPY ./api.py             /service/api.py
COPY ./start_uvicorn.sh   /service/start_uvicorn.sh
COPY ./requirements.txt   /service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /service/requirements.txt

EXPOSE 8001

# run the API
CMD ["bash", "/service/start_uvicorn.sh"]