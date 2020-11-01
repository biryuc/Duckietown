while True:
    a = input()

    if len(a)<=10 and a[0]=='a' and a[-1]<='z' and 'a'<=a[-1]:
        print("Yes")

    else:
        print("No")

