# number, string, boolean, array = [1, 2, 3]
# nhap danh sach sinh vien gom ten, diem toan, diem ly, diem hoa
name = ['nam', 'tuan', 'phuong']
subject = ['toan', 'ly', 'hoa']
score = [7, 8, 9]
# object hash as = {key: value}
example = {"name": "nam", "toan": 7, "ly": 8, "hoa": 9}
# array of hash
atr = [{"name": "nam", "toan": 7, "ly": 8, "hoa": 9}, {"name": "tuan", "toan": 7, "ly": 9, "hoa": 9}]
# in ra thong tin hoc sinh
# for item in atr:
#     print('name: ' + item['name'] + ', toan: ' + str(item['toan']) + ', ly: ' + str(item['ly']) + ', hoa: ' + str(item['hoa']) )

# nhap vao danh sach hoc sinh, gom cac truong, ten, toan, van
# input 
a = []
key = 'k'
while key == 'k':
    name = input('please enter name: ')
    toan = int(input('please enter score toan: '))
    van = int(input('please enter score van: '))
    a.append({'name': name, 'toan': toan, 'van': van})
    print('Please enter key = k to continue or press anything to exit')
    key = input()

for item in a:
    print('name: ' + item['name'] + ', toan: ' + str(item['toan']) + ', van: ' + str(item['van']))

