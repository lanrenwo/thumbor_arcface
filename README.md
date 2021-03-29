# thumbor_arcface
Thumbor ArcFace can recognize side faces, higher recognition rate.

# Environment
- Thumbor >= 7.0.0
- ArcFace >= 3.0

# Installation
```bash
pip install thumbor_arcface
```

## Enable detector
1. Add `thumbor_arcface` to your `thumbor.conf`.

```
DETECTORS = [
    'thumbor_arcface',
    'thumbor.detectors.feature_detector',
]
```
2. Add ArcFace's `ARC_APP_ID` and `ARC_SDK_KEY`  to your `thumbor.conf`.
```
########### ArcFace #########
ARC_APP_ID = ''
ARC_SDK_KEY = ''
```

## Thanks
- [ArcFace-python](https://github.com/tensorflower/ArcFace-python)
- [thumbor_rekognition](https://github.com/yu-liang-kono/thumbor_rekognition)