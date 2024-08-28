
an = int(input("Nhập vào chiều cao của An: "))
minh = int(input("Nhập vào chiều cao của Minh: "))
lan = int(input("Nhập vào chiều cao của Lan: "))


if an > minh and an > lan:
    print("Bạn cao nhất là: An")
elif minh > an and minh > lan:
    print("Bạn cao nhất là: Minh")
else:
    print("Bạn cao nhất là: Lan")