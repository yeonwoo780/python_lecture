

## 식별자 이름 규칙

1. 영문자와 숫자, 밑줄 문자 _로 이루어진다.
2. 중간에 공백이 들어가면 안 된다.
3. 첫 글자는 반드시 영문자나 밑줄 문자 _로 시작해야 한다.
4. 대문자와 소문자는 구분된다. 따라서 Count와 count는 서로 다른 식별자이다.
5. 식별자의 길이에 제한은 없다.
6. 키워드는 식별자로 사용할 수 없다.

##### 키워드keyword 혹은 예약어reserved word

[![image-20210415111004908](https://user-images.githubusercontent.com/25717861/114803852-3525cb00-9ddb-11eb-9c22-57d0ab90ac6c.png)](https://user-images.githubusercontent.com/25717861/114803852-3525cb00-9ddb-11eb-9c22-57d0ab90ac6c.png)

rec_square.py 생성

```
width = 20
height = 40
width = 300
area = width * height
print("사각형의 면적",area)
```

변수 width = 300으로 반영이 된다.

#### 파이썬 연산자와 그 의미

[![image-20210415111625698](https://user-images.githubusercontent.com/25717861/114804278-0825e800-9ddc-11eb-94e1-cce15816bd55.png)](https://user-images.githubusercontent.com/25717861/114804278-0825e800-9ddc-11eb-94e1-cce15816bd55.png)

#### 문자열과 정수의 덧셈연산

number_and_string2.py 의 파일에서 오류 메세지를 확인하면 다음과 같다.

```
my_age = 22
my_height = '177'
my_age = my_age + 1
my_height = my_height + 1
print(my_age, my_height)
....
my_height = my_height + 1
TypeError: must be str, not int
혹은
TypeError: can only concatenate str (not "int") to str
```

문자열과 문자열 합칠수 있지만 문자열과 숫자는 서로 합칠 수 없다.

따라서 문자열 숫자로 바꾸거나 숫자를 문자로 바꿔서 서로 합칠 수는 있다.

### 자료형 data type

##### 부울형, 숫자형(정수, 실수, 복소수), 문자열, 리스트, 튜플, 집합, 딕셔너리

부울형(boolean) : True or False 즉 참 또는 거짓으로 결과가 나오는 형태

```
True or False
```

숫자형

```
#정수
2 
#실수
3.0
#복소수
2+3i
```

문자열

```
"Hello World"
'Hello World'
'Hello "w"orld'
```

### if 조건문

[![image-20210415133735467](https://user-images.githubusercontent.com/25717861/114814739-c606a180-9def-11eb-8ca9-61831ed647ba.png)](https://user-images.githubusercontent.com/25717861/114814739-c606a180-9def-11eb-8ca9-61831ed647ba.png)

[![image-20210415133837639](https://user-images.githubusercontent.com/25717861/114814797-e9315100-9def-11eb-88a2-66ac506c0ec2.png)](https://user-images.githubusercontent.com/25717861/114814797-e9315100-9def-11eb-88a2-66ac506c0ec2.png)

## 다양한 조건을 판단하는 elif

if와 else만으로는 다양한 조건을 판단하기 어렵다. 다음 예를 보더라도 if와 else만으로는 조건을 판단하는 데 어려움을 겪게 된다.

> "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라."

위 문장을 보면 조건을 판단하는 부분이 두 군데가 있다. 먼저 주머니에 돈이 있는지를 판단해야 하고 주머니에 돈이 없으면 다시 카드가 있는지 판단해야 한다.

if와 else만으로 위 문장을 표현하려면 다음과 같이 할 수 있다.

```
>>> pocket = ['paper', 'handphone']
>>> card = True
>>> if 'money' in pocket:
...     print("택시를 타고가라")
... else:
...     if card:
...         print("택시를 타고가라")
...     else:
...         print("걸어가라")
...
택시를 타고가라
>>>
```

언뜻 보기에도 이해하기 어렵고 산만한 느낌이 든다. 이런 복잡함을 해결하기 위해 파이썬에서는 다중 조건 판단을 가능하게 하는 elif를 사용한다.

위 예를 elif를 사용하면 다음과 같이 바꿀 수 있다.

```
>>> pocket = ['paper', 'cellphone']
>>> card = True
>>> if 'money' in pocket:
...      print("택시를 타고가라")
... elif card: 
...      print("택시를 타고가라")
... else:
...      print("걸어가라")
...
택시를 타고가라
```

즉 elif는 이전 조건문이 거짓일 때 수행된다. if, elif, else를 모두 사용할 때 기본 구조는 다음과 같다.

```
If <조건문>:
    <수행할 문장1> 
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
...
else:
   <수행할 문장1>
   <수행할 문장2>
   ... 
```

위에서 볼 수 있듯이 elif는 개수에 제한 없이 사용할 수 있다.

**[if문을 한 줄로 작성하기]**

앞의 pass를 사용한 예를 보면 if문 다음에 수행할 문장이 한 줄이고, else문 다음에 수행할 문장도 한 줄밖에 되지 않는다.

```
>>> if 'money' in pocket:
...     pass 
... else:
...     print("카드를 꺼내라")
...
```

이렇게 수행할 문장이 한 줄일 때 조금 더 간략하게 코드를 작성하는 방법이 있다.

```
>>> pocket = ['paper', 'money', 'cellphone']
>>> if 'money' in pocket: pass
... else: print("카드를 꺼내라")
...
```

if문 다음 수행할 문장을 콜론(:) 뒤에 바로 적어 주었다. else문 역시 마찬가지이다.

## 조건부 표현식

다음과 같은 코드를 보자.

```
if score >= 60:
    message = "success"
else:
    message = "failure"
```

위 코드는 score가 60 이상일 경우 message에 문자열 "success"를, 아닐 경우에는 "failure"를 대입하는 코드이다.

파이썬의 조건부 표현식(conditional expression)을 사용하면 위 코드를 다음과 같이 간단히 표현할 수 있다.

```
message = "success" if score >= 60 else "failure"
```

조건부 표현식은 다음과 같이 정의한다.

```
조건문이 참인 경우` if `조건문` else `조건문이 거짓인 경우
```

조건부 표현식은 가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.

# for문

for문의 기본 구조는 다음과 같다.

```
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
```

리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입되어 "수행할 문장1", "수행할 문장2" 등이 수행된다.

## 예제를 통해 for문 이해하기

for문은 예제를 통해서 살펴보는 것이 가장 알기 쉽다. 다음 예제를 직접 입력해 보자.

### 1. 전형적인 for문

```
>>> test_list = ['one', 'two', 'three'] 
>>> for i in test_list: 
...     print(i)
... 
one 
two 
three
```

`['one', 'two', 'three']` 리스트의 첫 번째 요소인 'one'이 먼저 i 변수에 대입된 후 `print(i)` 문장을 수행한다. 다음에 두 번째 요소 'two'가 i 변수에 대입된 후 `print(i)` 문장을 수행하고 리스트의 마지막 요소까지 이것을 반복한다.

### 2. 다양한 for문의 사용

```
>>> a = [(1,2), (3,4), (5,6)]
>>> for (first, last) in a:
...     print(first + last)
...
3
7
11
```

위 예는 a 리스트의 요솟값이 튜플이기 때문에 각각의 요소가 자동으로 (first, last) 변수에 대입된다.

> ※ 이 예는 02장에서 살펴본 튜플을 사용한 변수값 대입 방법과 매우 비슷한 경우이다. `>>> (first, last) = (1, 2)`

### 3. for문의 응용

for문의 쓰임새를 알기 위해 다음을 가정해 보자.

```
"총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오."
```

우선 학생 5명의 시험 점수를 리스트로 표현해 보았다.

```
marks = [90, 25, 67, 45, 80]
```

1번 학생은 90점이고 5번 학생은 80점이다.

이런 점수를 차례로 검사해서 합격했는지 불합격했는지 통보해 주는 프로그램을 만들어 보자. 역시 IDLE 에디터로 작성한다.

```
# marks1.py
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)
```

각각의 학생에게 번호를 붙여 주기 위해 number 변수를 사용하였다. 점수 리스트 marks에서 차례로 점수를 꺼내어 mark라는 변수에 대입하고 for문 안의 문장들을 수행한다. 우선 for문이 한 번씩 수행될 때마다 number는 1씩 증가한다.

이 프로그램을 실행하면 mark가 60 이상일 때 합격 메시지를 출력하고 60을 넘지 않을 때 불합격 메시지를 출력한다. 명령 프롬프트 창을 열어 실행해 보자.

```
C:\doit>python marks1.py
1번 학생은 합격입니다.
2번 학생은 불합격입니다.
3번 학생은 합격입니다.
4번 학생은 불합격입니다.
5번 학생은 합격입니다.
```

### while 반복문

[![image-20210415141634645](https://user-images.githubusercontent.com/25717861/114825553-5699ad80-9e01-11eb-8079-4952d34f6bb2.png)](https://user-images.githubusercontent.com/25717861/114825553-5699ad80-9e01-11eb-8079-4952d34f6bb2.png)

### break와 continue

반복문을 제어하는 키워드

• 반복 실행을 종료 -> break • 반복문 루프 내의 나머지 실행부 를 건너뛰고 계속해서

•반복 루프를 실행 -> continue continue는 반복 실행을 종료하지 않음

break

[![image-20210415152318859](https://user-images.githubusercontent.com/25717861/114823455-87c4ae80-9dfe-11eb-871e-0e12a96f0560.png)](https://user-images.githubusercontent.com/25717861/114823455-87c4ae80-9dfe-11eb-871e-0e12a96f0560.png)

continue

[![image-20210415152406620](https://user-images.githubusercontent.com/25717861/114823550-a32fb980-9dfe-11eb-9ecd-53912cd17094.png)](https://user-images.githubusercontent.com/25717861/114823550-a32fb980-9dfe-11eb-9ecd-53912cd17094.png)





## 함수



![image-20210415160109218](https://user-images.githubusercontent.com/25717861/114827573-d1fc5e80-9e03-11eb-990c-c8bd11e78719.png)



return문이 없는 간단한 코드로 함수를 정의하고 호출하기

print_star_func.py 을 생성후 다음과 같이 코딩 한다.

```python
def print_star(): # 별표 출력을 위한 함수 정의
	print('************************')
print_star() # 별표 출력을 위한 함수 호출
```



결과값

```cmd
************************
```



#### 함수와 매개변수

![image-20210415165425063](https://user-images.githubusercontent.com/25717861/114834159-41298100-9e0b-11eb-96d3-0a8a5d79dddb.png)



#### 매개변수를 가진 별표 출력 함수와 인자를 이용한 호출

print_star_param.py을 생성후 다음과 같이 코딩

```python
# 별표 출력을 매개변수 n번만큼 반복하는 프로그램
def print_star(n):
    for _ in range(n):
    print('************************')
print_star(4) # 별표 출력을 위해 4라는 인자 값을 준다.
```

```cmd
************************
************************
************************
************************
```



sum_func.py을 생성후 다음과 같이 코딩

```python
# 별표 출력을 매개변수 n번만큼 반복하는 프로그램
def print_sum(a, b): # 두 개의 매개변수를 가진 함수
    result = a + b
    print(a, '과', b, '의 합은', result, '입니다.')
print_sum(10, 20)
print_sum(100, 200)
```

결과값

```cmd
10 과 20 의 합은 30 입니다.
100 과 200 의 합은 300 입니다.
```





#### 매개변수를 활용한 2차 방정식의 근 구하기



![image-20210415165846842](https://user-images.githubusercontent.com/25717861/114834772-dc225b00-9e0b-11eb-829d-0418db3dd32e.png)



root_ex1.py 생성후 다음과 같이 코딩한다.

```python
a = 1
b = 2
c = -8
# ( a * x^2 ) + ( b * x ) + c = 0
r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print('해는', r1, '또는', r2)
```







root_ex2.py

```python
a = 1
b = 2
c = -8
# 근의 공식으로 해를 한 번 더 구한다.(반복되는 코드)
r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print('해는', r1, '또는', r2)
a = 2
b = -6
c = -8
# 근의 공식으로 해를 한 번 더 구한다.(반복되는 코드)
r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print('해는', r1, '또는', r2)
```





root_ex3.py

```python
def print_root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print('해는', r1, '또는', r2)
# 계수 값이 다른 2차 방정식의 해를 구함
print_root(1, 2, -8)
print_root(2, -6, -8)
```





### 반환문 return

![image-20210415170103024](https://user-images.githubusercontent.com/25717861/114835081-2c012200-9e0c-11eb-9eff-c2e01f73eecc.png)



sum_with_return1.py 

```python
def get_sum(a, b): # 두 수의 합을 반환하는 함수
    result = a + b
    return result # return 문을 사용하여 result를 반환
    n1 = get_sum(10, 20)
    print('10과 20의 합 =', n1)
n2 = get_sum(100, 200)
print('100과 200의 합 =', n2)
```







## 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?

입력값이 여러 개일 때 그 입력값을 모두 더해 주는 함수를 생각해 보자. 하지만 몇 개가 입력될지 모를 때는 어떻게 해야 할까? 아마도 난감할 것이다. 파이썬은 이런 문제를 해결하기 위해 다음과 같은 방법을 제공한다.

```
def 함수이름(*매개변수): 
    <수행할 문장>
    ...
```

일반적으로 볼 수 있는 함수 형태에서 괄호 안의 매개변수 부분이 `*매개변수`로 바뀌었다.

**여러 개의 입력값을 받는 함수 만들기**

다음 예를 통해 여러 개의 입력값을 모두 더하는 함수를 직접 만들어 보자. 예를 들어 `add_many(1, 2)`이면 3을, `add_many(1,2,3)`이면 6을, `add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)`이면 55를 돌려주는 함수를 만들어 보자.

```
>>> def add_many(*args): 
...     result = 0 
...     for i in args: 
...         result = result + i 
...     return result 
... 
>>>
```

위에서 만든 add_many 함수는 입력값이 몇 개이든 상관이 없다. `*args`처럼 매개변수 이름 앞에 `*`을 붙이면 입력값을 전부 모아서 튜플로 만들어 주기 때문이다. 만약 `add_many(1, 2, 3)`처럼 이 함수를 쓰면 args는 `(1, 2, 3)`이 되고, `add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)`처럼 쓰면 args는 `(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)`이 된다. 여기에서 `*args`는 임의로 정한 변수 이름이다. `*pey`, `*python`처럼 아무 이름이나 써도 된다.

> ※ args는 매개변수를 뜻하는 영어 단어 arguments의 약자이며 관례적으로 자주 사용한다.

실제로 이 함수를 직접 실행해 보자.

```
>>> result = add_many(1,2,3)
>>> print(result)
6
>>> result = add_many(1,2,3,4,5,6,7,8,9,10)
>>> print(result)
55
```

`add_many(1,2,3)`으로 함수를 호출하면 6을 돌려주고, `add_many(1, 2, 3, 4, 5, 6, 7, 8, 9,10)`을 대입하면 55를 돌려준다.

여러 개의 입력을 처리할 때 `def add_many(*args)`처럼 함수의 매개변수로 `*args`만 사용할 수 있는 것은 아니다.

다음 예를 보자.

```
>>> def add_mul(choice, *args): 
...     if choice == "add": 
...         result = 0 
...         for i in args: 
...             result = result + i 
...     elif choice == "mul": 
...         result = 1 
...         for i in args: 
...             result = result * i 
...     return result 
... 
>>>
```

add_mul 함수는 여러 개의 입력값을 의미하는 `*args` 매개변수 앞에 choice 매개변수가 추가되어 있다.

이 함수는 다음과 같이 사용할 수 있다.

```
>>> result = add_mul('add', 1,2,3,4,5)
>>> print(result)
15
>>> result = add_mul('mul', 1,2,3,4,5)
>>> print(result)
120
```

매개변수 choice에 'add'가 입력된 경우 `*args`에 입력되는 모든 값을 더해서 15를 돌려주고, 'mul'이 입력된 경우 `*args`에 입력되는 모든 값을 곱해서 120을 돌려준다.





**키워드 파라미터 kwargs**

이번에는 키워드 파라미터에 대해 알아보자. 키워드 파라미터를 사용할 때는 매개변수 앞에 별 두 개(`**`)를 붙인다. 역시 이것도 예제로 알아보자. 먼저 다음과 같은 함수를 작성한다.

```
>>> def print_kwargs(**kwargs):
...     print(kwargs)
...
```

print_kwargs 함수는 매개변수 kwargs를 출력하는 함수이다. 이제 이 함수를 다음과 같이 사용해 보자.

```
>>> print_kwargs(a=1)
{'a': 1}
>>> print_kwargs(name='foo', age=3)
{'age': 3, 'name': 'foo'}
```

입력값 `a=1` 또는 `name='foo', age=3`이 모두 딕셔너리로 만들어져서 출력된다는 것을 확인할 수 있다. 즉 `**kwargs`처럼 매개변수 이름 앞에 `**`을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 `key=value` 형태의 결괏값이 그 딕셔너리에 저장된다.

> ※ 여기에서 kwargs는 keyword arguments의 약자이며 args와 마찬가지로 관례적으로 사용한다.