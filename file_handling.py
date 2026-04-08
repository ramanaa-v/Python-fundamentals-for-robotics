file = open('example.txt', 'w')
file.write('Hello, world')
file.close()

file = open('example.txt', 'a')
file.write('\nAdding a second line.')
file.close()

file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
