import random

# file_name = 'f1.txt'
# file = open(file_name, mode='w')
#
# try:
#     for i in range(1, 11):
#         file.write('Text ' + str(i) + '\n')
# finally:
#     file.close()
#
# 
# file_name = 'f2.txt'
# with open(file_name, 'w') as file:
#     for n in range(0, 100):
#         file.write(str(random.randint(1, 10000)) + '\n')
#
# with open('f2.txt', 'r') as file:
#     content = file.read()
#     print(content)
# print('-----------------------------------------------------------')
# print('')
# with open('f1.txt', 'r') as file:
#     content = file.read()
#     print(content)

with open('f1.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()
