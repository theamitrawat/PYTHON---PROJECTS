f = open('mytxtfile.txt', 'w')
f.write('I am Amit Rawat')
f.write('\nI live in palwal')
f.write('\nI am 21 years old')
f.truncate(5)
list = ['\ni am a web developer','\ni have knowledge of django']
f.writelines(list)
f.close()

with open('mytxtfile.txt', 'r') as f:
    # text = f.read()
    # print(text)
    print(f.seek(10))
    print(f.tell())

    i = 1
    while True:
        line = f.readline()
        if not line:
            break
        print(line)