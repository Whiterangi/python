list_a = [1,2,3,4,1,2,3,1,4,1,2,3]
numbers = {}
for i in list_a:
    if i in numbers:
        numbers[i] +=1
    else:
        numbers[i] = 1

print(str(list_a)+"에서 사용된 숫자의 종류는"+str(len(numbers))+"개 입니다.")
print("참고: ", numbers)