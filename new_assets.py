def no_template_found(template_name): print(f'no "{template_name}" template found'); raise SystemExit()

class htmltemplates:

    def gettemplate(template_name):
        gottentemplate = getattr(htmltemplates, template_name, no_template_found)
        return gottentemplate

    empty = ''



    basic = '''<!DOCTYPE html>

<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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

</html>'''


    basic_css = '''<!DOCTYPE html>

<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/css/[CSS_PATH].css">
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

</html>'''



    basic_scripted = '''<!DOCTYPE html>

<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        Page Title
    </title>
    <script>
        console.log('Hello world');
    </script>
</head>

<body>
    <h1>
        This is a Heading
    </h1>
    <p>
        This is a paragraph.
    </p>
</body>

</html>'''


    basic_css_scripted = '''<!DOCTYPE html>

<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/css/[CSS_PATH].css">
    <title>
        Page Title
    </title>
    <script>
        console.log('Hello world');
    </script>
</head>

<body>
    <h1>
        This is a Heading
    </h1>
    <p>
        This is a paragraph.
    </p>
</body>

</html>'''

    basic_scripted_css = basic_css_scripted