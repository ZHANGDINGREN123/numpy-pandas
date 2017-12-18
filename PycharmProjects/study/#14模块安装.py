text = "This is first text.\nThis is next line.\nThis is last line"
my_file = open('myfile.txt', 'w')
my_file.write(text)
my_file.close()
print(text)