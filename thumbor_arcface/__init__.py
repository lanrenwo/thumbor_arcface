#!/usr/bin/env python
import cv2
import numpy as np

from os import path 
from sys import path as sysPath
curr_path = path.dirname(path.abspath(__file__))
sysPath.insert(0, "{}".format(curr_path))

from arcface.engine import *
from thumbor.config import Config
from thumbor.detectors import BaseDetector
from thumbor.point import FocalPoint
from thumbor.utils import logger


Config.define(
    'ARC_APP_ID', None, 'ArcFace APPID'
)
Config.define(
    'ARC_SDK_KEY', None,'ArcFace SDKKey'
)
Config.define(
    'ARC_FACE_SCALE', 32,'ArcFace detectFaceScaleVal'
)
Config.define(
    'ARC_FACE_MAX_NUM', 10, 'ArcFace detectFaceMaxNum'
)

class Detector(BaseDetector):
    def __init__(self, context, index, detectors):
        super(Detector, self).__init__(context, index, detectors)
        self.active()

    async def detect(self):
        faces = self.detect_faces()
        if not faces:
            return await self.next()

        for i in range(0, faces.faceNum):
            fr = faces.faceRect[i]
            self.context.request.focal_points.append(
                FocalPoint.from_square(
                    fr.left, fr.top, fr.right-fr.left, fr.bottom-fr.top, origin="Face Detection"
                )
            )
        return

    def detect_faces(self):
        face_engine = ArcFace()
        mask = ASF_FACE_DETECT | ASF_FACERECOGNITION
        res = face_engine.ASFInitEngine(ASF_DETECT_MODE_IMAGE, ASF_OP_0_ONLY, self.context.config.ARC_FACE_SCALE, self.context.config.ARC_FACE_MAX_NUM, mask)
        if (res != MOK):
            logger.warning("ASFInitEngine fail: {}".format(res))
            return []

        img = cv2.cvtColor(np.asarray(self.context.modules.engine.image), cv2.COLOR_RGB2BGR)
        res,faces = face_engine.ASFDetectFaces(img)
        if faces.faceNum < 1:
            return []
        return faces

    def active(self):
        res = ASFOnlineActivation(str.encode(self.context.config.ARC_APP_ID), str.encode(self.context.config.ARC_SDK_KEY))
        if (MOK != res and MERR_ASF_ALREADY_ACTIVATED != res):
            logger.warning("ASFActivation fail: {}".format(res))
        else:
            logger.warning("ASFActivation sucess: {}".format(res))

        res,activeFileInfo = ASFGetActiveFileInfo()

        if (res != MOK):
            logger.warning("ASFGetActiveFileInfo fail: {}".format(res))
        else:
            logger.warning(activeFileInfo)
