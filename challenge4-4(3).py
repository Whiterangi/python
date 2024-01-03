DNA=input("염기서열을 입력하세요: ")
codon=[DNA[i:i+3] for i in range(0,len(DNA),3)]
count={} #키는 코돈의 인덱스, 값은 개수
for j in codon:
    if j in count:
        count[j]+=1
    else:
        count[j]=1

for key in count:
    print(f"{key}의 개수 : {count[key]}")