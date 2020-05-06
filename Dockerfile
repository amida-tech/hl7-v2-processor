FROM python:3.7.3-slim

RUN pip install kafka-python
RUN pip install flask

ADD /util/* /util/
ADD hl7_processor.py.py /
ENTRYPOINT ["python","/hl7_processor.py"]
CMD []
