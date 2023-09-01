# read binary file test

f = open("binary_test.txt", "rb")

read_line_num = 0

while True:
    #print(read_line_num)
    read_line_num+=1

    data = f.readline()

    next_led_data = [x for x in data]

    print(next_led_data)

    if (next_led_data == []):
        f.close()
        break