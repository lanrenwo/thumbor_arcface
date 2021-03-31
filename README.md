# thumbor_arcface
Thumbor ArcFace can recognize side faces and higher recognition rate, solve the problem of low recognition rate of OpenCV.

[中文文档](https://github.com/lanrenwo/thumbor_arcface/blob/master/README-osc.md)

# Environment
- Thumbor >= 7.0.0
- ArcFace SDK >= 3.0

# Installation
```bash
pip install thumbor_arcface
```
# Enable detector
- Add `thumbor_arcface` to your `thumbor.conf`.
```
DETECTORS = [
    'thumbor_arcface',
    'thumbor.detectors.feature_detector',
]
```
- At the end of your `thumbor.conf`, add ArcFace's `ARC_APP_ID` and `ARC_SDK_KEY`, Remember to modify the value.
```
########### ArcFace #########
ARC_APP_ID = ''
ARC_SDK_KEY = ''
ARC_FACE_SCALE = 32
ARC_FACE_MAX_NUM = 10
```
# Thanks
- [ArcSoft SDK](https://ai.arcsoft.com.cn/)
- [ArcFace-python](https://github.com/tensorflower/ArcFace-python)
- [thumbor_rekognition](https://github.com/yu-liang-kono/thumbor_rekognition)