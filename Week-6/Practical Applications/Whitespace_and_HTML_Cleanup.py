#Name:T.S.S.Roshini
#Program:**Whitespace and HTML Cleanup
import re
def clean_text(html):
    html = re.sub(r"<.*?>", "", html)
    html = re.sub(r"\s+", " ", html)
    return html.strip()
text = "<p>Hello   <b>world</b>!</p>\n\nThis is\tPython."
print(clean_text(text))
#output
#Hello world! This is Python.