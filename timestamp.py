import time

cur_time = time.strftime('%H:%M:%S')
h = time.strftime('%H')
m = time.strftime('%M')
s = time.strftime('%S')

print('\n',cur_time,'\n')


if int(h)>=21 and int(m)>=00 and int(s)>=00:
    print('\nGood Night\n')
elif int(h)>=18 and int(m)>=00 and int(s)>=00:
    print('\nGood Evening\n')
elif int(h)>=15 and int(m)>=00 and int(s)>=00:
    print('\nGood After Noon\n')
elif int(h)>=12 and int(m)>=00 and int(s)>=00:
    print('\nGood Noon\n')
elif int(h)>=6 and int(m)>=00 and int(s)>=00:
    print('\nGood Morning\n')
else:
    print('\nError\n')
