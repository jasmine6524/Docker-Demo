import os
import cv2
# import base64
# from infer_with_openvino_onnx import *
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from gevent import pywsgi

app = Flask(__name__)


# def get_img():
#     img_str = request.form['image']  # 获取图像数据,对应客户端的img_str
#     img_byte = base64.b64decode(img_str)  # img_byte是字节型数据，二进制编码。b64decode对字节型b64编码数据进行解码。bytes->bytes
#     image = np.fromstring(img_byte, np.uint8)
#     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#     # random_name = '{}.jpg'.format(uuid.uuid4().hex)
#     # save_path = os.path.join('caches', secure_filename(random_name))
#     # cv2.imwrite(save_path, image)
#     # return save_path
#     return image


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return "hello docker"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    # server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    # server.serve_forever()
    # app.run(debug=True)