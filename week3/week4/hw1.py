stuff = input("โปรดกรอกชื่อสินค้าและราคาสินค้า : ")
name, price = stuff.split(',')
a = []

while True :
    stuff = input("โปรดกรอกชื่อสินค้าและราคาสินค้า : ")
    name, price = stuff.split(',')
    if stuff != '0,0':
        a.append((name, price))
        print(a)
    else:
        break
if stuff == '0,0':
    print("ขอบคุณสำหรับการใช้งานโปรแกรมของเรา")

prices = []

for product in a:
    name, price = product
    prices.append(int(price))
    print("Product name", name, "Product price is : ", price)

summary = lambda x : sum(x)
print("ผลรวมของราคาสินค้าคือ", summary(prices))