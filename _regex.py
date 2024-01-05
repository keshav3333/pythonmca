import re

with open(r"C:\Users\Administrator\Desktop\content.txt",'r+') as file:
    data = file.read()
    data1=re.sub('a','@',data)
    file.write(data1)

    