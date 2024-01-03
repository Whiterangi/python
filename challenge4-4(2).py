DNA=input("염기서열을 입력하세요: ")
count={
    "a" : 0,
    "t" : 0,
    "g" : 0,
    "c" : 0
}

for dna in DNA:
    count[dna] +=1
    
for key in count:
    print(f"{key}의 개수: {count[key]}")