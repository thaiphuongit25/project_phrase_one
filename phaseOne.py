# - Project: Quản lý bán hàng
# Thông tin: Nhà sản xuất, danh mục sản phẩm, sản phẩm
# + Nhà sản xuất: Số thứ tự, Tên nhà sản xuất, địa chỉ, phone: owner = [{ 'id': 1, 'name': 'Sam sung', 'address': 'viet nam', 'phone': '0120677773'}]
# + Danh mục:  Số thư tự, Tên danh mục, miêu tả: ví dụ: categories = [{'id': 1, 'name': 'Thời trang', 'description': 'Thời trang cho tre em'}]
# + Sản phẩm: Số thứ tự, Tên sản phẩm, giá, miêu tả, số lượng hàng còn, nhà sản xuất nào, danh mục nào, ảnh: 
# products = [{'id': 1, 'name': 'giay nam', 'description': ' giay cho gioi tre', 'price': 200000, 'owner_id': 1, 'category_id': 1}]
owner = []
categories = []
products = []

k = 'o'
i = 1
print ('Start enter list owner')
while k == 'o':
    id = i
    name = input('Name of owner: ')
    address = input('Address of owner: ')
    phone = input('Phone of owner: ')
    obj = {'id': id, 'name': name, 'address': address, 'phone': phone}
    owner.append(obj)
    k = input('Enter o to continue add owner or press any key to exit')
    i += 1
print(owner)

k = 'c'
i = 1
print('Start enter list of category ')
while k == 'c':
    id = i
    name = input('Name of category: ')
    description = input('Description of category: ')
    obj = {'id': id, 'name': name, 'description': description}
    categories.append(obj)
    k = input('Enter c to continue add owner or press any key to exit')
    i += 1
print(categories)

k = 'p'
i = 1

def list_id(own):
    atr = []
    for item in own:
        atr.append(item['id'])
    return atr

id_owner = list_id(owner)
id_category = list_id(categories)
print('Start enter list of product ')
while k == 'p':
    id = i
    name = input('Name of product: ')
    description = input('Description of product: ')
    price = input('Price of product')
    s1 = 'Id of owner as',id_owner
    s2 = 'Id of category as',id_category
    owner_id = int(input(s1))
    category_id = int(input(s2))
    obj = {'id': id, 'name': name, 'description': description, 'price': price, 'owner_id': owner_id, 'category_id': category_id}
    products.append(obj)
    k = input('Enter p to continue add owner or press any key to exit')
    i += 1
print(products)
