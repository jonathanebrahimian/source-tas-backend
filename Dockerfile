FROM python:3.9

ENV PYTHONUNBUFFERED=1

# WORKDIR specifies the code directory
WORKDIR /code

# COPY copies the requirements file for pip into the directory
COPY requirements.txt /code/

# installs all libraries specified in the requirements file through pip
RUN pip install -r requirements.txt

# copies the rest of the backend folder into the code directory
COPY . /code/

# exposes port 8000
EXPOSE 8000