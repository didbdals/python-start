Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(1+1)
2
>>> print(2+2)
4
>>> print(2-2)
0
>>> age = 19
>>> print(age)
19
>>> my name = yumin
SyntaxError: invalid syntax
>>> print('apple')
apple
>>> print("apple")
apple
>>> print("apple')
      
SyntaxError: EOL while scanning string literal
>>> print("apple'")
apple'
>>> print('he said, "Hello!"')
he said, "Hello!"
>>> print("I'm a boy')
      
SyntaxError: EOL while scanning string literal
>>> letters = ['a','b','c','d','e']
>>> print(letters)
['a', 'b', 'c', 'd', 'e']
>>> participants =['박승희','권가현','김다선']
>>> print(participants)
['박승희', '권가현', '김다선']
>>> print(participants[1])
권가현
>>> print(participants[0])
박승희
>>> print(participants[3])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(participants[3])
IndexError: list index out of range
>>> fruits = ('수박','딸기','참외')
>>> participants.append('김형진')
>>> print(participants)
['박승희', '권가현', '김다선', '김형진']
>>> participants.remove('김다선')
>>> print('김다선')
김다선
>>> print(participants)
['박승희', '권가현', '김형진']
>>> fruits.append('메론')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fruits.append('메론')
AttributeError: 'tuple' object has no attribute 'append'
>>> participants.append('양유민')
>>> print(participants)
['박승희', '권가현', '김형진', '양유민']
>>> numbers = {1,2,3,4,5}
>>> {1,2,3,4,5} = {3,4,2,1,5}
SyntaxError: cannot assign to set display
>>> print(numbers)
{1, 2, 3, 4, 5}
>>> numbers = {1,1,2,2,3,3,4,4,5,5,5}
>>> pritn(numbers)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    pritn(numbers)
NameError: name 'pritn' is not defined
>>> print(numbers)
{1, 2, 3, 4, 5}
>>> print(numbers[2])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(numbers[2])
TypeError: 'set' object is not subscriptable
>>> numbers.add(6)
>>> print(numbers)
{1, 2, 3, 4, 5, 6}
>>> numbers.remove(5)
>>> print(numbers)
{1, 2, 3, 4, 6}
>>> capitals = {'한국':'서울','일본':'도쿄','중국':'베이징'}
>>> print(capitals[한국])
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(capitals[한국])
NameError: name '한국' is not defined
>>> print(capitals['한국'])
서울
>>> print(capitals['일본'])
도쿄
>>> print(capitals['중국'])
베이징
>>> coffee = {'아메리카노':4000, '카페 라떼':5000, '에스프레소':4000}
>>> print(coffee)
{'아메리카노': 4000, '카페 라떼': 5000, '에스프레소': 4000}
>>> print(coffee['아메리카노'])
4000
>>> a = 4
>>> b = 5
>>> print(a+b)
9
>>> x = 1
>>> x = x+1
>>> print(x)
2
>>> x =  x +2
>>> print(x)
4
>>> 같다는게 아니라
SyntaxError: invalid syntax
>>> number = input()
123456
>>> print(number)
123456
>>> number = 1234
>>> print(number)
1234
>>> print(coffee['카페 라떼'])
5000
>>> number = input()
1234234234234
>>> 12312424124
12312424124
>>> print(1+1)
2
>>> print(1-1)
0
>>> print(1*1)
1
>>> print(1/1)
1.0
>>> print(2**3)
8
>>> print(3**3)
27
>>> print(12334//21)
587
>>> print(7//3)
2
>>> plrint(63%3)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    plrint(63%3)
NameError: name 'plrint' is not defined
>>> print(63%3)
0
>>> print("Hello world"[7])
o
>>> print('a'+'b'0)
SyntaxError: invalid syntax
>>> print('a'+'b')
ab
>>> peinr("a"*2)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    peinr("a"*2)
NameError: name 'peinr' is not defined
>>> print("a"*2)
aa
>>> print("abc"*9)
abcabcabcabcabcabcabcabcabc
>>> numbers = [1,2,3,4,5,7,8]
>>> numbers.append('a')
>>> print(numbers)
[1, 2, 3, 4, 5, 7, 8, 'a']
>>> numbers.remove('a')
>>> print(numbers)
[1, 2, 3, 4, 5, 7, 8]
>>> print(numbers[7])
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    print(numbers[7])
IndexError: list index out of range
>>> print(numbers[6])
8
>>> del numbers[5]
>>> print(numbers)
[1, 2, 3, 4, 5, 8]
>>> numbers.append(4)
>>> print(numbers)
[1, 2, 3, 4, 5, 8, 4]
>>> numbers.append('a')
>>> print(numbers)
[1, 2, 3, 4, 5, 8, 4, 'a']
>>> numbers[6] = 9
>>> print(numbers)
[1, 2, 3, 4, 5, 8, 9, 'a']
>>> del number[4]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    del number[4]
TypeError: 'str' object doesn't support item deletion
>>> print(coffee)
{'아메리카노': 4000, '카페 라떼': 5000, '에스프레소': 4000}
>>> coffee['생과일주스']=6000
>>> print(coffee)
{'아메리카노': 4000, '카페 라떼': 5000, '에스프레소': 4000, '생과일주스': 6000}
>>> coffee['카페 라떼']=6000
>>> print(coffee)
{'아메리카노': 4000, '카페 라떼': 6000, '에스프레소': 4000, '생과일주스': 6000}
>>> coffee['카페 라떼'] = 6000원
SyntaxError: invalid syntax
>>> coffee['카페 라떼']='6000원'
>>> print(coffee[1])
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    print(coffee[1])
KeyError: 1
>>> print(coffee)
{'아메리카노': 4000, '카페 라떼': '6000원', '에스프레소': 4000, '생과일주스': 6000}
>>> print(coffee['카페 라떼'])
6000원
>>> print(coffee['생과일주스'])
6000
>>> 
==================== RESTART: C:/Users/lonel/Desktop/워크샵.py ====================
Hello!
HI!
Annyeonghaseyo!
>>> 
================= RESTART: C:/Users/lonel/Desktop/condition.py =================
>>> 
================= RESTART: C:/Users/lonel/Desktop/condition.py =================
홀수입니다.
>>> 
================= RESTART: C:/Users/lonel/Desktop/condition.py =================
홀수입니다.
>>> 
================= RESTART: C:/Users/lonel/Desktop/condition.py =================
>>> 
================= RESTART: C:/Users/lonel/Desktop/condition.py =================
프로그램이 끝났습니다.
>>> 
================= RESTART: C:/Users/lonel/Desktop/condition.py =================
>>> 
================= RESTART: C:/Users/lonel/Desktop/condition.py =================
홀수입니다.
>>> 
==================== RESTART: C:/Users/lonel/Desktop/반복문.py ====================
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!Traceback (most recent call last):
  File "C:/Users/lonel/Desktop/반복문.py", line 5, in <module>
    print("Hello!")
KeyboardInterrupt
>>> 
==================== RESTART: C:/Users/lonel/Desktop/반복문.py ====================
>>> 
==================== RESTART: C:/Users/lonel/Desktop/반복문.py ====================
10
9
8
7
6
5
4
3
2
1
>>> 
==================== RESTART: C:/Users/lonel/Desktop/반복문.py ====================
10
9
8
7
6
5
4
3
2
1
>>> 
==================== RESTART: C:/Users/lonel/Desktop/반복문.py ====================
10
20
30
9
18
27
8
16
24
7
14
21
6
12
18
5
10
15
4
8
12
3
6
9
2
4
6
1
2
3
>>> 
==================== RESTART: C:/Users/lonel/Desktop/반복문.py ====================
355687428096000
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
Traceback (most recent call last):
  File "C:/Users/lonel/Desktop/함수.py", line 11, in <module>
    print(factorial(21))
  File "C:/Users/lonel/Desktop/함수.py", line 8, in factorial
    count = coumt -1
NameError: name 'coumt' is not defined
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
Traceback (most recent call last):
  File "C:/Users/lonel/Desktop/함수.py", line 10, in <module>
    print(factorial(21))
  File "C:/Users/lonel/Desktop/함수.py", line 7, in factorial
    count = coumt -1
NameError: name 'coumt' is not defined
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
51090942171709440000
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
Traceback (most recent call last):
  File "C:/Users/lonel/Desktop/함수.py", line 10, in <module>
    print(factorial(21,9))
TypeError: factorial() takes 1 positional argument but 2 were given
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
Traceback (most recent call last):
  File "C:/Users/lonel/Desktop/함수.py", line 10, in <module>
    print(factorial(21 , 9))
TypeError: factorial() takes 1 positional argument but 2 were given
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
3
2
1
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
1 1 1
1 2 2
1 3 3
1 4 4
1 5 5
1 6 6
1 7 7
1 8 8
1 9 9
2 1 2
2 2 4
2 3 6
2 4 8
2 5 10
2 6 12
2 7 14
2 8 16
2 9 18
3 1 3
3 2 6
3 3 9
3 4 12
3 5 15
3 6 18
3 7 21
3 8 24
3 9 27
4 1 4
4 2 8
4 3 12
4 4 16
4 5 20
4 6 24
4 7 28
4 8 32
4 9 36
5 1 5
5 2 10
5 3 15
5 4 20
5 5 25
5 6 30
5 7 35
5 8 40
5 9 45
6 1 6
6 2 12
6 3 18
6 4 24
6 5 30
6 6 36
6 7 42
6 8 48
6 9 54
7 1 7
7 2 14
7 3 21
7 4 28
7 5 35
7 6 42
7 7 49
7 8 56
7 9 63
8 1 8
8 2 16
8 3 24
8 4 32
8 5 40
8 6 48
8 7 56
8 8 64
8 9 72
9 1 9
9 2 18
9 3 27
9 4 36
9 5 45
9 6 54
9 7 63
9 8 72
9 9 81
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
2 1 2
2 2 4
2 3 6
2 4 8
2 5 10
2 6 12
2 7 14
2 8 16
2 9 18
3 1 3
3 2 6
3 3 9
3 4 12
3 5 15
3 6 18
3 7 21
3 8 24
3 9 27
4 1 4
4 2 8
4 3 12
4 4 16
4 5 20
4 6 24
4 7 28
4 8 32
4 9 36
5 1 5
5 2 10
5 3 15
5 4 20
5 5 25
5 6 30
5 7 35
5 8 40
5 9 45
6 1 6
6 2 12
6 3 18
6 4 24
6 5 30
6 6 36
6 7 42
6 8 48
6 9 54
7 1 7
7 2 14
7 3 21
7 4 28
7 5 35
7 6 42
7 7 49
7 8 56
7 9 63
8 1 8
8 2 16
8 3 24
8 4 32
8 5 40
8 6 48
8 7 56
8 8 64
8 9 72
9 1 9
9 2 18
9 3 27
9 4 36
9 5 45
9 6 54
9 7 63
9 8 72
9 9 81
10 1 10
10 2 20
10 3 30
10 4 40
10 5 50
10 6 60
10 7 70
10 8 80
10 9 90
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4
2 2 4Traceback (most recent call last):
  File "C:/Users/lonel/Desktop/함수.py", line 7, in <module>
    print(i, j, i*j)
KeyboardInterrupt
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
2 2 4
2 3 6
2 4 8
2 5 10
2 6 12
2 7 14
2 8 16
2 9 18
2 10 20
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
Traceback (most recent call last):
  File "C:/Users/lonel/Desktop/함수.py", line 4, in <module>
    while j < 10:
NameError: name 'j' is not defined
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
Traceback (most recent call last):
  File "C:/Users/lonel/Desktop/함수.py", line 4, in <module>
    while j < 10:
NameError: name 'j' is not defined
>>> 
===================== RESTART: C:/Users/lonel/Desktop/함수.py ====================
1 2 2
1 3 3
1 4 4
1 5 5
1 6 6
1 7 7
1 8 8
1 9 9
1 10 10
2 2 4
2 3 6
2 4 8
2 5 10
2 6 12
2 7 14
2 8 16
2 9 18
2 10 20
3 2 6
3 3 9
3 4 12
3 5 15
3 6 18
3 7 21
3 8 24
3 9 27
3 10 30
4 2 8
4 3 12
4 4 16
4 5 20
4 6 24
4 7 28
4 8 32
4 9 36
4 10 40
5 2 10
5 3 15
5 4 20
5 5 25
5 6 30
5 7 35
5 8 40
5 9 45
5 10 50
6 2 12
6 3 18
6 4 24
6 5 30
6 6 36
6 7 42
6 8 48
6 9 54
6 10 60
7 2 14
7 3 21
7 4 28
7 5 35
7 6 42
7 7 49
7 8 56
7 9 63
7 10 70
8 2 16
8 3 24
8 4 32
8 5 40
8 6 48
8 7 56
8 8 64
8 9 72
8 10 80
9 2 18
9 3 27
9 4 36
9 5 45
9 6 54
9 7 63
9 8 72
9 9 81
9 10 90
>>> 