#Name:T.S.S.Roshini
#Program:Phone number extractor
import re
text = """
Call 555-123-4567 for support.
You can also contact (555) 987-6543.
Emergency number: 555.111.2222
"""
pattern = r"\(?(\d{3})\)?[-. ](\d{3})[-.](\d{4})"
numbers = re.findall(pattern, text)
for number in numbers:
    phone = "-".join(number)
    print(phone)
#output
#555-123-4567
#555-987-6543
#555-111-2222