FROM python:3.12

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip 
#copy to code directory
COPY . /code 

#set permissions

RUN chmod +x /code/src
RUN pip install --no-cache-dir --upgrade -r code/src/requirements.txt

EXPOSE 8005

# Set PYTHONPATH environment variable
ARG PYTHONPATH_ARG
ENV PYTHONPATH="/code/src:${PYTHONPATH_ARG}"

# Change directory to /code/src to install the package
WORKDIR /code/src
# Install the package in editable mode
RUN pip install -e .
RUN python prediction_model/training_pipeline.py

WORKDIR /code
CMD ["python","main.py"]