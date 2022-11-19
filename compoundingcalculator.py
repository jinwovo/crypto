import math
import inquirer

start = int(input("초기금 : "))
per = int(input("이율 : ")) / 100
choose = input("일 / 월 / 년 : ")

while choose != "일" or choose != "월" or choose != "년":
    if choose == '일':
        date = int(input("일 수 :"))
        break
    elif choose == '월':
        date = int(input("월 수 :"))
        break
    elif choose == '년':
        date = int(input("년 수 :"))
        break
    else:
        print("제대로 된 값을 입력해주세요.")
        continue

for i in range(date):
    m = start * ((1 + per) ** i)
    print(str(i)+"일 : "+str(round(m)))
