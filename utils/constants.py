"""
Author: Zhenwei Jiang
Finished Time: 13-8-2023
Function: Some initialization data and some parameters (You can modify them as you please)
"""

SEPARATOR = '@@@@'.encode()

SIZE_SEP = len(SEPARATOR)

SIZE_BYTE = 2**10

SEP_RECV = '@'.encode()

SIZE_SEP_RECV = len(SEP_RECV)

SIZE_BYTE_RECV = 10

NUM_FRAME = 8

FIN = '$_$'.encode()

SIZE_FIN = len(FIN)

# urls = {'girl': 'https://cn.bing.com/images/search?q=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&qs=n&form=QBIR&sp=-1&lq=0&pq=mei%27n%C3%BC%27tu%27p&sc=10-11&cvid=76CBF67C92E9422F9F7F2E41A814B108&ghsh=0&ghacc=0&first=1&cw=1249&ch=954',
#         'face': 'https://cn.bing.com/images/search?q=%e4%ba%ba%e8%84%b8%e5%9b%be%e5%83%8f&qpvt=%e4%ba%ba%e8%84%b8%e5%9b%be%e5%83%8f&form=IGRE&first=1',
#         'baby': 'https://cn.bing.com/images/search?q=%E5%B0%8F%E5%AD%A9%E5%9B%BE%E7%89%87&qpvt=%e5%b0%8f%e5%ad%a9%e5%9b%be%e7%89%87&form=IGRE&first=1&cw=1249&ch=954'}

urls = {'baby': 'https://cn.bing.com/images/search?q=%E5%B0%8F%E5%AD%A9%E5%9B%BE%E7%89%87&qpvt=%e5%b0%8f%e5%ad%a9%e5%9b%be%e7%89%87&form=IGRE&first=1&cw=1249&ch=954'}

DATA_PATH = 'F:/FDOCAS/data'

RES_PATH = 'F:/FDOCAS/result'

FACE_DETECTOR = r"../demo/haarcascade_frontalface_alt.xml"
EYE_DETECTOR = r"../demo/haarcascade_eye.xml"

LOG_PATH = 'F:/FDOCAS/log'
