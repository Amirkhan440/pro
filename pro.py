import os, platform
os.system("cd $HOME/")
#os.system("termux-setup-storage")
os.system("xdg-open https://www.facebook.com/groups/660205018582939")

try:
    import requests
except ImportError:
    os.system("pip install requests")

rana=platform.architecture()[0]
if rana=="32bit":
    __import__("pro32").my_tool_security()
elif rana=="64bit":
    __import__("pro").my_tool_security()
