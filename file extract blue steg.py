def get_file_content(file_name):
    with open(file_name,'r') as f:
        content = f.read()
    return content

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



result = ""
for n in range(18000):
    file_name = get_file_name(n)
    content = get_file_content("text_files/" + file_name)
    result += content[0]

print (result)




    
