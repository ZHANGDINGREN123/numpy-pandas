append_text = "\nThis is appended file."
my_file = open('myfile.txt', 'a')
my_file.write(append_text)
my_file.close()
print(append_text)