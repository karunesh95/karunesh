import re
regex = re.compile(r'(\d+)')
A=regex.split("hello world! 123")
print A
