def get_file_content(file_name):
    with open(file_name,'r') as f:
        content = f.read()
    return content

def caesar_cipher(content , shift):
    result = ""
    
    for character in content:
        snum = ord(character) - shift
        if (snum < 32):
            snum += 95
        result += chr(snum)
    return result

content = get_file_content("text_files/file_063d.txt")
print(caesar_cipher (content, 34))

    
