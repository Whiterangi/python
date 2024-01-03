import datetime
now=datetime.datetime.now()
hour=now.hour

str_input=input("입력: ")
if (str_input=="안녕") or (str_input=="안녕하세요") :
    print("안녕하세요")
elif (str_input=="지금 몇 시야?") or (str_input=="지금 몇 시예요?"):
    print("지금은 " + str(hour) + "시 입니다.")
else:
    print(str_input)
