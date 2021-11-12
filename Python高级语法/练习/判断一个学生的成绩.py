score = eval(input('请输入你的成绩:'))

if score<60:
    print("不及格")
elif 60 <= score < 70:
    print('还可以')
elif 70 <= score < 80:
    print('比上一个强点')
elif 80 <= score < 90:
    print('比上上一个强点')
elif 90 <= score <= 100:
    print('比上上上一个强点')