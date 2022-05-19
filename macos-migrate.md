## Send Notification on Macos

- Now, I use this example code: https://gist.github.com/MarcAlx/f7a51a245c7c0450dbd4f4203b9916e0
  It has a little problem: cannot set icon
- Or this pip package:https://github.com/knowsuchagency/klaxon

## Python Pip Package Installatin Problems

```bash
# pip install libnotify
brew install libnotify
brew install cairo
pip3 install gobject
brew install gobject-introspection
pip3 install pygobject
```

- Package cairo was not found in the pkg-config search path. Perhaps you should add the directory containing `cairo.pc' to the PKG_CONFIG_PATH environment variable No package 'cairo' found
  https://cloud.tencent.com/developer/ask/sof/79335
- mac Package gobject-introspection-1.0 was not found in the pkg-config search path.
  https://tutorials.technology/solved_errors/osx-gobject-introspection-1_0-found.html

## Auto-Start when login

SystemPreferences -> Users&Groups -> loginItems -> Write and select an bash script file

```bash
source ~/.zshrc
workon an2linux
cd /Users/lic/gitRepos/AN2Linux
python3 an2linuxserver.py &
```

> 可通过 ps -ef 和 kill -9 停止运行(与Linux一致，但Mac上没有Linux的systemctl/service)

## Other Links

- [Mac上设置(Python)定时任务](https://blog.csdn.net/tim_shadow/article/details/52776070)
- [介绍一个最省心的 Python 日志框架](https://mp.weixin.qq.com/s/IPtbDoOjQkOnuNnF6OOVWg)
- [Python: Convert List [Array] to String](https://codeigo.com/python/convert-list-to-string#:~:text=The%20fastest%20way%20to%20convert%20a%20list%20%28array%29,inside%20the%20list%20and%20uses%20spaces%20as%20separators.)
