file_path = ('D://Thomas//Allgemeines//Technik-Projekte//KiraKiraKasa//ByteFiles//test_file.txt')
write_path = ('D://Thomas//Allgemeines//Technik-Projekte//KiraKiraKasa//ByteFiles//test_read_file.txt')


file_content = ''
with open(file_path, "rb") as f:
    byte = f.read()
    
    

    #while byte != b"":
        # byte = f.read()
        #file_content += str(byte, 'utf-8')
#print(byte.decode("utf-8"))

for single_byte in byte:
    #file_content += str(byte, 'utf-8')
    #print(file_content)
    break

#with open(write_path, "w") as f:
    #f.write(file_content)
decoded_input = list(bytearray(byte))
str1 = ""
for ele in decoded_input:
    str1 += str(ele) + " "

with open(write_path, "w") as f:
    f.write(str1)

#print(byte)
#print(file_content)
#print('something')
#print(b'hello')
#print(b'\x01'.decode('unicode_escape'))
#print(list(bytearray(byte)))


int_values = [x for x in byte]
print(int_values)