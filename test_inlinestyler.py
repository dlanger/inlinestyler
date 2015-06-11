from inlinestyler.utils import inline_css

def test_no_markup():
    inlined = inline_css("Hello World!")
    expected = u'<html>\n  <body>\n    <p>Hello World!</p>\n  </body>\n</html>\n'

    assert expected == inlined

def test_non_utf8_encoding_adds_headers():
    inlined = inline_css("Hello World!", encoding='utf-16')
    expected = u"<?xml version='1.0' encoding='utf-16'?>\n<html>\n  <body>\n    <p>Hello World!</p>\n  </body>\n</html>\n"

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
  <head/>
  <body>
            Hello <span class="emphasis" style="font-weight: bold">World</span>!
        </body>
</html>
"""

    assert expected == inline_css(document)
