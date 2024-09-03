FROM python:3.12

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip 

# Copy code to /code directory
COPY . /code 

# Set permissions
RUN chmod +x /code

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Install the package in editable mode
RUN pip install -e /code
# Set the PYTHONPATH environment variable
ENV PYTHONPATH="/code"

EXPOSE 8005

WORKDIR /code
# Use a single CMD instruction
CMD ["python", "main.py"]
