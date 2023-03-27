# 나이를 입력받아 10대 이하, 20대, 30대, 40대, 50대 이상을 출력하는 코드
# if, elif, else 사용

age = int(input())

if age < 20:
    print('10대 이하')
elif 20 <= age < 30:
    print('20대')
elif 30 <= age < 40:
    print('30대')
elif 40 <= age < 50:
    print('40대')
else:
    print('50대 이상')