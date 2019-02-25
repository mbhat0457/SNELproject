f = open("C:/Users/mbhat0457/Desktop/text_files/file_2715.txt", "r")
text = f.read()


key = '''`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'''

result = ""
for t in text:
    n = key.find(t)
    pos = n + 32
    result += chr(pos)
print (result)

