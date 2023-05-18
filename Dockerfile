FROM python:3.11
RUN mkdir docker_py
COPY docker_py.py docker_py
WORKDIR docker_py
CMD ["python3", "docker_py.py"]