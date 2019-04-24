'''
a = 5
if a > 5:
    print('5 초과')
else:
    print('5 이하')


num = int(input('숫자를 입력해주세요:'))

if num % 2 == 1:
    print('홀수입니다.')
elif num / 3 == 1:
    print('dont know')
    
else:
    print('짝수입니다.')
    
'''   
    
# 네이버 미세먼지를 조건문 코드로 작성(4개 조건)

# 짝수는 짝수 리스트에 홀수는 홀수 리스트 출력(range(1, 11))


dust = int(input('미세먼지:'))

if dust > 150:
    print('매우나쁨')
elif 80 < dust <= 150:
    print('나쁨')
elif 30 < dust <= 80:
    print('보통')
else:
    print('좋음')

