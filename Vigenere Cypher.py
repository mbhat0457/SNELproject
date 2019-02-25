key = "enigma"


def get_file_content(file_name):
    with open(file_name,'r') as f:
        content = f.read()
    return content


def vigenere_cipher(content , key):
    result = ""
    i = 5
    for character in content:
        snum = ord(character) - ord(key[i])
        while (snum < 32):
            snum += 95
        result += chr(snum)
        i = i + 1
        if i > 5:
            i = 0
    return result

content = get_file_content("text_files/file_30d3.txt")

decoded = vigenere_cipher (content, key)

with open("vigenere_output.txt", 'w') as f:
    f.write(decoded)
