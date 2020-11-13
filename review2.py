# quản lý danh sách học sinh khối 8
# viết chương trình nhập thông tin học sinh theo lớp, 
# thông tin bao gồm: lớp học, tên học sinh, điểm toán, văn, anh

# xuất ra danh sách học sinh theo lớp
# xuất ra điểm trung bình của từng học sinh, 
# của từng lớp và cả khối
# cấu trúc dữ liệu mảng:
# phân tích: khối lớp 8 có 4 lớp, gồm 8b, 8I, 8S, 8V ->cố định
# cấu trúc dữ liệu lưu: 
# define 4 mảng: classB, classI, classS, classV
classB =  [{'name': 'tuan', 'scoreMatch': 8, 'van': 9, 'anh': 8}]

for item in classB:
    avg = (int(item['scoreMatch']) + int(item['van']) + int(item['anh'])) / 3
    print('avg of', item['name'], avg)

