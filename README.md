# thumbor_arcface
Thumbor ArcFace can recognize side faces, higher recognition rate.

# Environment
- Thumbor >= 7.0.0
- ArcFace SDK >= 3.0

# Installation
```bash
pip install thumbor_arcface
```
## Enable detector
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
```
## Thanks
- [ArcSoft SDK](https://ai.arcsoft.com.cn/)
- [ArcFace-python](https://github.com/tensorflower/ArcFace-python)
- [thumbor_rekognition](https://github.com/yu-liang-kono/thumbor_rekognition)