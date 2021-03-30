# thumbor_arcface
Thumbor ArcFace可识别侧面，并且识别率更高，从而解决OpenCV识别率不高的问题。

# 环境
- Thumbor >= 7.0.0
- ArcFace SDK >= 3.0

# 安装
```bash
pip install thumbor_arcface
```
# 开启插件
- 将 `thumbor_arcface` 添加至 `thumbor.conf`.
```
DETECTORS = [
    'thumbor_arcface',
    'thumbor.detectors.feature_detector',
]
```
- 在`thumbor.conf`的文件末尾, 添加以下配置，记住一定要修改值。
```
########### ArcFace #########
ARC_APP_ID = ''
ARC_SDK_KEY = ''
```
# 感谢
- [ArcSoft SDK](https://ai.arcsoft.com.cn/)
- [ArcFace-python](https://github.com/tensorflower/ArcFace-python)
- [thumbor_rekognition](https://github.com/yu-liang-kono/thumbor_rekognition)