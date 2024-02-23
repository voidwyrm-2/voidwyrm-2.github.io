'''let's me easily create new html webpages'''
import argparse
from pathlib import Path


htmlbases = {
    'basic': '''<!DOCTYPE html>

<html>
    <head>
        <title>
            Page Title
        </title>
    </head>
    <body>
        <h1>
            This is a Heading
        </h1>
        <p>
            This is a paragraph.
        </p>
    </body>
</html>''',

    'basiclabeled': '''<!DOCTYPE html>

<html>
    <head>
        <title>
        Page Title
        </title>
    </head>
    <body>
        <label>
            This is a label
        </label>
    </body>
</html>''',

    'basicscripted': '''<!DOCTYPE html>

<html>
    <head>
        <title>
        Page Title
        </title>
    </head>
    <body>
        <label>
            This is a label
        </label>
    </body>
</html>'''
}


choices = list(htmlbases.keys())
#choices.extend(('--types', '--bases', '--templates'))


parser = argparse.ArgumentParser()

parser.add_argument('nameorpath')
parser.add_argument('type', choices=choices)

args = parser.parse_args()

inp = str(args.nameorpath).replace('\\', '/').split('/')

if inp in ('--types', '--bases', '--templates'):
    print('the available html bases/templates are:')
    for base in htmlbases.keys(): print(base)

btype = str(args.type)


verifying = True
while verifying:
    if '.' in inp: inp.remove('.')
    elif './' in inp: inp.remove('./')
    else: verifying = False


filename = inp.pop(-1).removesuffix('.html')

path = inp; del inp


prevpath = ''
for f in path:
    if not Path(prevpath + f).exists(): print(f"error: {prevpath + f} doesn\'t exist"); raise SystemExit()
    prevpath += f + '/'


fullpath = prevpath + filename + '.html'

if Path(fullpath).exists(): print(f"error: {fullpath} already exists"); raise SystemExit()


with open (fullpath, 'xt') as newfile:
    towrite = ''
    if btype in (None, ''): towrite = htmlbases['basic']
    else:
        if btype in htmlbases.keys(): towrite = htmlbases[btype]
        else: print('that isn\' an available html base/template!')
    newfile.write(towrite)
print('new file created!')