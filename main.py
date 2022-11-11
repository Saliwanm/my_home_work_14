file = open("input_file.txt", 'r', encoding="utf-8")
my_list = file.readlines()
file_test = open('output_file.txt', 'w')
file_test.close()
for ml in my_list:
    temp = ''
    for m in ml:
        if m.isalpha() or m.isdigit() or m == '@' or m == '.' or m == '_' or m == '-':
            temp += m
    new_list1 = temp.split('@')
    new_list2 = new_list1[1].split('.')
    if len(new_list2) > 2:
        new_list2[0], new_list2[1] = new_list2[1], new_list2[0]
        new_list2[1], new_list2[-1] = new_list2[-1], new_list2[1]
    result = '.'.join(new_list2)
    result2 = new_list1[0] + '@' + result + '\n'
    file_out = open('output_file.txt', 'a')
    file_out.write(result2)
    file_out.close()
    file.close()
