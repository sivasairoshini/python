#Name:T.S.S.Roshini
#Program:Date Extraction and Reformatting
import re
text = "My dates are 14/09/2026, 25/12/2025 and 01/01/2026."
pattern = r"(\d{2})/(\d{2})/(\d{4})"
dates = re.findall(pattern, text)
print("Dates:", dates)
result = re.sub(pattern, r"\3-\2-\1", text)
print("Converted:", result)
#output
#Dates: [('14', '09', '2026'), ('25', '12', '2025'), ('01', '01', '2026')]
#Converted: My dates are 2026-09-14, 2025-12-25 and 2026-01-01.