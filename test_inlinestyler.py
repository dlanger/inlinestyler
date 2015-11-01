from inlinestyler.utils import inline_css

def test_no_markup():
    inlined = inline_css("Hello World!")
    expected = u'<html><body><p>Hello World!</p></body></html>\n'

    assert expected == inlined

def test_respects_encoding_argument():
    inlined = inline_css(u"Hello World!", encoding='utf-16')
    expected = u'<html><body><p>Hello World!</p></body></html>\n'.encode('utf-16')

    assert expected == inlined

def test_inline_css_in_head():

    document = """
    <html>
        <head>
            <style>
                .emphasis {
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            Hello <span class="emphasis">World</span>!
        </body>
    </html>
    """

    expected = """<html>
<head></head>
<body>
            Hello <span class="emphasis" style="font-weight: bold">World</span>!
        </body>
</html>
"""
    inlined = inline_css(document)
    assert expected == inlined
