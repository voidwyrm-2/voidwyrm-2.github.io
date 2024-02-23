from pathlib import Path



#count = 0
def getdir(directory: str | Path, removeext = False, addbehind = '', addinfront = '', excludelist = [], extensionlist = ()):
    for e in range(len(extensionlist)):
        if type(extensionlist[e]) != str: extensionlist[e] = str(extensionlist[e])
        if not extensionlist[e].startswith('.'): extensionlist[e] = '.' + extensionlist[e]
    #global count
    #print(count)
    #count += 1
    #directory = Path(directory)
    out = []
    for item in directory.iterdir():
        if str(item) not in ('', ' '):
            if str(item) not in excludelist and str(item) not in ('', ' '):
                if item.is_dir(): out.extend(getdir(item, removeext, addbehind))
                else:
                    if str(item).endswith(extensionlist):
                        if removeext: out.append(addbehind + str(item).split('.')[0] + addinfront)
                        else: out.append(addbehind + str(item) + addinfront)
    return out
        


thisdir = Path('./')

allfiles = getdir(thisdir, True, '        <p>\n            https://voidwyrm-2.github.io/', '\n        </p>', ['css', 'assets', 'LICENSE'], ('.html', '.md'))

for f in allfiles: print(f)

'''hwc = 10

def hw():
    global hwc
    print('hello world')
    if hwc != 0:
        hwc -= 1
        hw()

hw()'''