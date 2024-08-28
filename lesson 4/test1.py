matkhau = "mindxdream"
password = input("Nhap mat khau :")
while (password == matkhau):
    print("Mat khau dung")
    break
while (password != matkhau):
    print("Mật khẩu không chính xác")
    password = input("Nhap lai :")
    break
