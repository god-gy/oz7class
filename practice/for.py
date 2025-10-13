#1. 1부터 10까지 출력하기
# for문을 이용해서 1부터 10까지의 숫자를 한 줄씩 출력하세요.

# for i in range(1, 11):
#     print(i)

#2. 문자열 순회하기
# 문자열 "Python"의 각 문자를 한 줄씩 출력하세요.

# for char in "Python":
#     print(char)

#3. 리스트 합계 구하기
# 리스트 numbers = [3, 5, 7, 9]의 합계를 for문으로 구해서 출력하세요.

# numbers = [3, 5, 7, 9]
# total = 0
# for num in numbers:
#     total += num
# print(total)

#4. 구구단 3단 출력하기
# for문을 사용해서 구구단 3단을 출력하세요.

# for i in range(1, 10):
#     print(f"3 x {i} = {3 * i}")

#5. 리스트 안의 문자열 출력
# 리스트 fruits = ["apple", "banana", "cherry"]의 각 요소를 “과일명 : ___” 형식으로 출력하세요.

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(f"과일명 : {fruit}")

#6. 1부터 100까지의 합 구하기
# for문을 사용하여 1부터 100까지의 합을 구하세요.

# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

#7. 짝수만 출력하기
# 1부터 20까지의 숫자 중 짝수만 출력하세요.

# for i in range(1, 21) :
#     if i%2 ==0 :
#         print(i, end=' ')

#8. 별 찍기 (삼각형)
# 다음과 같은 모양의 별을 출력하세요.
# *
# **
# ***
# ****
# *****

# for i in range(1, 6) :
#     print('*' * i)

#9. enumerate() 사용하기
# 리스트 menu = ["라면", "김밥", "떡볶이"]의 각 항목을 번호와 함께 출력하세요.

# for i, item in enumerate(["라면", "김밥", "떡볶이"], start=1) :
#     print(f"{i}. {item}")

#10. 구구단 전체 출력하기
# 중첩 for문을 이용해서 2단부터 9단까지 출력하세요.

# for i in range(2, 10) :
#     for j in range(1, 10) :
#         print(f"{i} x {j} = {i*j}")
#     print()

#보너스: 도전 문제
# 1부터 50까지 중 3의 배수이면서 5의 배수인 수를 모두 출력하고, 그 개수도 세어 출력하세요.

count = 0
for i in range(1, 51) :
    if i % 3 == 0 and i % 5 == 0 :
        print(i, end=' ')
        count += 1
print(f"\n총 개수: {count}")