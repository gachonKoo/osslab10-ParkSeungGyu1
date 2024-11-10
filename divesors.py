import sys

# 명령줄 인수로 받은 숫자를 정수로 변환
number = int(sys.argv[1])

# 1부터 number까지 반복
for i in range(1, number + 1):
    if number % i == 0:  # 나머지가 0이면 약수
        print(i, end=" ")
print()
