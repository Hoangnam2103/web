kwh = int(input("Nhap so dien :"))
sotien = 0
if kwh <= 0:
    print("Nhap sai roi")
else:
    if kwh <= 50 :
        print("so tien la ",(sotien +1700)* kwh,"dong")
    elif kwh <= 100:
        print("so tien la ",(50*1700)+ ((kwh - 50) * 1900),"dong")
    elif kwh <= 200:    
        print("so tien la ",(50*1700)+(50*1900)+((kwh-100) *2100),"dong")
    elif kwh <= 300:
        print("so tien la ",(50*1700)+ (50*1900) + (100*2100) + ((kwh - 200)*3000),"dong")

