import base64
import inspect
import unittest
import json
import cv2
import requests
import time
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

plt.switch_backend('agg')

TF_ENDPOINT = "http://localhost:8501/v1/models/half_plus_three:regress"
token = " "
headers = {'Content-type': 'application/json', 'X-Language': 'en-us',
           'Accept': 'application/json', 'X-Auth-Token': token}


class TestTfServing(unittest.TestCase):
    def setUp(self):
        self.test_img = './00001.jpg'
        self.test_times = 1

    def test_veh_per_get(self):
        print("\n in func: {}".format(inspect.stack()[0][3]))
        res = requests.get("{}/v1/models/vehPer_v1".format(TF_ENDPOINT))
        # print(res.text)

    def test_lane_post(self):
        print("\n in func: {}".format(inspect.stack()[0][3]))
        img_buf_once = cv2.imread(self.test_img)
        img_buf_once = cv2.cvtColor(img_buf_once, cv2.COLOR_RGB2GRAY)
        resized_image = cv2.resize(img_buf_once, (512, 288))
        image_buf = np.reshape(resized_image, (1, 288, 512, 1))
        # with open(self.test_img,"rb") as imageFile:
        #     image_buf=base64.b64encode(imageFile.read())

        for _ in range(self.test_times):
            start_time = time.time()
            post_data = json.dumps({"inputs": {"Placeholder:0": image_buf.tolist()}})
            # post_data = json.dumps({"inputs": {"image": image_buf}})
            # print(post_data)
            print("pack-{}, use time: {} ms".format(image_buf.shape,
                                                    (time.time() - start_time) * 1000))
            res = requests.post(
                "{}/v1/models/lane_v1:predict".format(TF_ENDPOINT),
                data=post_data
                # verify=False, headers=headers
            )
            # print(res.text)
            print("lane\n", dict(res.json()).keys())
            print("use time: {} ms".format((time.time() - start_time) * 1000))

if __name__ == '__main__':
    test_tf_serving=test_tf_restapi.TestTfServing()
    test_tf_serving.setUp()
    test_tf_serving.test_veh_per_get()
    test_tf_serving.test_lane_post()
