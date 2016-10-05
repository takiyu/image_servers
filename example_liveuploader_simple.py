#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import log_initializer

import cv2
from logging import getLogger, DEBUG, WARNING
import multiprocessing
import time
try:
    import Queue  # python2
except:
    import queue as Queue  # python3

import imgliveuploader

# logging
log_initializer.setFmt()
log_initializer.setRootLevel(WARNING)
logger = getLogger(__name__)
logger.setLevel(DEBUG)
imgliveuploader.logger.setLevel(DEBUG)


if __name__ == '__main__':
    logger.info('Start')

    request_queue = multiprocessing.Queue()
    response_queue = multiprocessing.Queue()

    imgliveuploader.start(request_queue, response_queue, stop_page=True,
                          port=5000)

    while True:
        try:
            # wait for image uploading
            img = request_queue.get(block=False)

            # show image
            cv2.imshow('img', img)

            # must be response
            res_message = 'message ' + str(time.time())
            response_queue.put({'img': img, 'msg': res_message})
        except Queue.Empty:
            pass

        cv2.waitKey(1)
