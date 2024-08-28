n = int(input("Nhập số bài kiểm tra"))
score = []

for i in range(n):
    diem = float(input("Nhập điểm kiểm tra"))
    score.append(diem)
score.sort()
print(score)


while len(score) > 1 and score[0] == score[1]:
    score.remove(score[0])
if len(score) > 0:
    score.pop(0)
print(score)

sum = 0
for k in range(len(score)):
    if score[k] > 8:
        sum = sum + 1
print("Số điểm trên 8",sum)

    