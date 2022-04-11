from re import S

file = open("Data.txt","r")
with file as l:
    g = l.read()
x=int(input("ป้อนตัวเลขเดือนที่ต้องการ:"))
k=[1,2,3,4,5,6,7,8,9,10,11,12]
if x in k :
         #No support
    if x == k :
        text_file = open("Data.txt", "r")
        lines = l.readlines()
        print(lines)
        print(len(lines))
        text_file.close()
        print(g)
    else :
        print("No data")
else :
    print('data incorrect pleace Enter again.')

#ไฟล์txt.ต้องตั้งตัวแปร ว่าข้อมูลของเดือนไหน
'''
print('Welcome to marcuscode\'s game')
level = input('Enter level (1 - 4): ')

if level == '1':
    print('Easy')
elif level == '2':
    print('Medium')
elif level == '3':
    print('Hard')
elif level == '4':
    print('Expert')
else:
    print('Invalid level selected')'''