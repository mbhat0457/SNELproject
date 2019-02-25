import random
num_chars = 18000

result = ""
for r in range(num_chars):
    n = random.randrange(32, 127)
    result += chr(n)
print (result)


def get_char_counts(text):
    counts = [0] * 127
    for c in text:
        n = ord(c)
        counts[n] += 1
    return counts[32:]

def chi_test(counts):
    chi = 0
    expected = sum(counts)/len(counts)
    for observed in counts:
        chi += ((((observed) - (expected))**2)/expected)
    return chi

def get_file_name(num):

    num = hex(num)
    num = num [2:]
    if len(num) == 1:
        num = "000" + num
    if len(num) == 2:
        num = "00" + num
    if len(num) == 3:
        num = "0" + num
    return "file_" + num + ".txt"
    

def get_file_content(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    return content
threshold = 140

for n in range(18000):
    file_name = get_file_name(n)
    text = get_file_content("text_files/" + file_name)
    counts = get_char_counts(text)
    x_sq = chi_test(counts)
    if x_sq > threshold:
        print(file_name, x_sq)
    


    
