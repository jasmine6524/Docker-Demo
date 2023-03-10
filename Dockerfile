FROM openvino/ubuntu20_runtime:latest
USER jasmine
RUN apt-get update
RUN pip3 install --upgrade pip \
  && pip3 install paddlepaddle==2.4.2 -i https://pypi.tuna.tsinghua.edu.cn/simple \
  && pip3 install flask \
  && pip3 install opencv-python \
  && pip3 install numpy \
  && pip3 install openvino==2022.3.0 \
  && pip3 install onnxruntime-openvino
