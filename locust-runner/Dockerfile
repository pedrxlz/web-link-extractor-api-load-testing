FROM python:3.8-slim

RUN pip install locust

COPY run_locust_tests.py /mnt/locust/

WORKDIR /mnt/locust

CMD ["python", "run_locust_tests.py"]