#FROM python:3.11
#RUN mkdir docker_py
#COPY docker_py.py docker_py
#WORKDIR docker_py
#CMD ["python3", "docker_py.py"]
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD ["python", "app.py"]