'''let's me easily create new html webpages'''
import argparse
from pathlib import Path
from new_assets import htmltemplates



def removeitems(list: list, items: list | tuple):
    out = []
    for i in list:
        if i not in items: out.append(i)
    return out



CANOVERWRITE = False
CANAPPEND = True


#<link rel="icon" type="image/png" href="">

cssbase = '''body {
    background-color: white;
}'''



templates = removeitems(list(vars(htmltemplates).keys()), ('__module__', 'gettemplate', 'no_template_found', '__dict__', '__weakref__', '__doc__'))
#choices.extend(('--types', '--bases', '--templates'))


parser = argparse.ArgumentParser()

parser.add_argument('nameorpath')
parser.add_argument('type', choices=templates)
#parser.add_argument('usescss', choices=('y', 'n'))

args = parser.parse_args()

fname = str(args.nameorpath).replace('\\', '/').split('/')

if fname in ('--types', '--bases', '--templates'):
    print('the available html bases/templates are:')
    for base in templates: print(base)

btype = str(args.type)

#css = str(args.usescss) == 'y'


verifying = True
while verifying:
    if '.' in fname: fname.remove('.')
    elif './' in fname: fname.remove('./')
    else: verifying = False


filename = fname.pop(-1).removesuffix('.html')

path = fname; del fname


prevpath = ''
for f in path:
    if not Path(prevpath + f).exists(): print(f"error: {prevpath + f} doesn\'t exist"); raise SystemExit()
    prevpath += f + '/'


fullpath = prevpath + filename + '.html'

writingmode = 'xt'
existserror = 0
if Path(fullpath).exists():
    if CANOVERWRITE:
        owask = input(f'{fullpath} already exists, overwrite it?(y/n)\n> ')
        if owask in ('y', 'yes'): writingmode = 'wt'
        else: existserror += 1
    else: existserror += 1
    if CANAPPEND and writingmode != 'wt':
        appask = input(f'{fullpath} already exists, append to it?(y/n)\n> ')
        if appask in ('y', 'yes'): writingmode = 'at'
        else: existserror += 1
    else: existserror += 1
    if existserror >= 2:
        if not CANOVERWRITE and not CANAPPEND: print(f"error: {fullpath} already exists")
        raise SystemExit()

css = '_css' in btype

with open (fullpath, writingmode) as htmlfile:
    towrite = ''
    if btype in (None, ''): towrite = htmltemplates.gettemplate('basic')
    else:
        if btype in templates:
            if css: towrite = str(htmltemplates.gettemplate(btype)).replace('[CSS_PATH]', filename)
            else: towrite = htmltemplates.gettemplate(btype)
        else: print('that isn\' an available html base/template!')
    if writingmode == 'wt': htmlfile.write(towrite)
    elif writingmode == 'at': htmlfile.write('\n\n\n\n\n' + towrite)
    else: htmlfile.write(towrite)
if writingmode == 'wt': print('file overwritten!')
elif writingmode == 'at': print('file appended to!')
else: print('new file created!')


if css:
    with open('./css/' + filename + '.css', writingmode) as cssfile:
        if writingmode == 'wt': cssfile.write(cssbase)
        elif writingmode == 'at': cssfile.write('\n\n\n\n\n' + cssbase)
        else: cssfile.write(cssbase)