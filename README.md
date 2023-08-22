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
# Debug
- Edit thumbor.conf:
```
STORAGE = "thumbor.storages.no_storage"
```
- if Engine fail (thumbor log):   
Because The validity period of the SDK has expired and you need to re-download the update .so file
```
2023-08-22 10:53:58 thumbor:WARNING ASFActivation sucess: 90114
2023-08-22 10:53:58 thumbor:WARNING ASF_ActiveFileInfo(startTime=b'xxx',endTime=b'xxx',platform=b'linux',sdkType=b'ArcFace',appId=b'xxxx',sdkKey=b'xxxx',sdkVersion=b'3.0.12402010101.3',fileVersion=b'2.0')
2023-08-22 10:53:58 thumbor:WARNING ASFInitEngine fail: 28678
```
# Thanks
- [ArcSoft SDK](https://ai.arcsoft.com.cn/)
- [ArcFace-python](https://github.com/tensorflower/ArcFace-python)
- [thumbor_rekognition](https://github.com/yu-liang-kono/thumbor_rekognition)
