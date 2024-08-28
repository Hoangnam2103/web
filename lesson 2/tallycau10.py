n = int(input("Nhap so giay :"))
gio = n//3600
phut = (n - gio * 3600)//60
giay = (n - gio * 3600 - phut*60)

print(gio,"gio",phut,"phut",giay,"giay")
