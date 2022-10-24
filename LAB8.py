# LAB 8 -1
# 1.
a = [10,20,30]
print(a[3])
# IndexError: List index out of range

n = int('20%')
print(n)
# ValueError: invalid literal for int() with base 10: '20%'

a = 100 + '200'
print(a)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 2.
try:
    a = [10,20,30]
    print(a[3])
except Exception as e:
    print("error:", e)

# LAB 8-2

try:
    print(10*(30/0))
except ZeroDivisionError:
    print('오류 : 0으로 나눔을 시도했습니다.')

try:
    x = int(input('정수 x를 입력하세요:'))
except ValueError:
    print("오류 : 입력 값이 정수나 실수가 아닙니다.")

try:
    import sys
    f = open('myfile.txt')
    s = f.readline()
except Exception as e:
    print('error: ', e)

# LAB 8-3
# 1
a = [1,2,3,4,5]
n = int(input("a의 요쇼를 하나 선택하시오: "))
for i in a:
    if n == i:
        print("{}은(는) {} 번째 요소입니다.".format(n, a[n]))
# 2
try:
    a = [1,2,3,4,5]
    n = int(input("a의 요쇼를 하나 선택하시오: "))
except ValueError:
    print("오류: 입력 값이 정수나 실수가 아님")
else:
    for i in a:
        if n == i:
            print("{}은(는) {} 번째 요소입니다.".format(n, a[n]))


# LAB 8-4
f = open('hello.txt', 'w')
f.write('Hello World!')
f.close()

f = open('numbers.txt', 'w')
f.write('100\n200\n300\n400')
f.close()

f = open('we_will_rock.txt', 'w')
f.write("Buddy, you're a boy, make a big noise\nPlaying in the street, gonna be a big man someday\nyou got mud on your face, you big disgrace\nKicking your can all over the place, singin'\nWe will, will rock you\nWe will, we will rock you")

# LAB 8-5
# 1.
f = open('numbers.txt','r')
s =f.read()
print(s)
f.close()

# 2.
f= open('we_will_rock.txt','r')
s = f.readline().rstrip()
print(s)
s = f.readline().rstrip()
print(s)
s = f.readline().rstrip()
print(s)
s = f.readline().rstrip()
print(s)
s = f.readline().rstrip()
print(s)
s = f.readline().rstrip()
print(s)
f.close()

# LAB 8-6
# 1.
fname = input('입력할 파일의 이름 : ')
f = open(fname,'r')
s =f.read()
print(s.upper())
f.close()

# 2.
fname = input('입력할 파일의 이름 : ')
for line in reversed(open(fname).readlines()):
    print(line.rstrip())
