def add(x,y) :
    return x + y

def substract(x,y) :
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("덧셈/뺄셈/곱셈/나눗셈을 선택하세요.")

choice = int(input("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 : "))

num1 = int(input("첫 번째 숫자 : ")
num2 = int(input("두 번째 숫자 : ")

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=",substract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))

else :
    print("잘못된 선택")

print("곱셈, 나눗셈 추가")
