FROM openvino/ubuntu20_runtime:latest
USER root
RUN pip3 install --upgrade pip \
  && pip3 install flask \
  && pip3 install opencv-python \
  && pip3 install numpy
RUN mkdir /app
RUN mkdir /app/res
WORKDIR /app
COPY ./example /app/example
COPY run.sh ./
RUN chmod +x run.sh
RUN chmod -R 777 /app
CMD ["./run.sh"]
