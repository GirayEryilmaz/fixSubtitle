import sys

with open(sys.argv[1], encoding="Windows-1252") as f:
    text =  f.read()

transTable = str(text).maketrans("þÞýÝðÐ", "şŞıIğĞ")
text = text.translate(transTable)

with open(sys.argv[2], 'w') as of:
    of.write(text)
