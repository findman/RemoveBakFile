# 移除备份文件

```
"""Usage:
  removeBakFile.py [-s] [-e]
  removeBakFile.py dir <dir> [<exts>] [-s] [-e]
  removeBakFile.py <exts> [-s] [-e]


Options:
  -h --help     Show this screen
  -s            silent remove
  -e            remove empty folder
  dir           dir, if none use current dir
  exts          bakfile ext. if none default 'bak'. more ext:'bak,bak2,...'
"""
```

项目打包时经常要移除一些系统生成的备份文件，索性自己写了一个简单备份文件移除工，同时判断空文件夹并移除。