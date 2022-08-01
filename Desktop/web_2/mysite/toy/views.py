# from django.shortcuts import render

# def gugu(req , num) :

#     result =[]
#     result = list(map(lambda i : f"{num}*{i} = {num*i}", range(1,10)))
  
#     return render(req,'toy/guguscreen.html' ,{"result":result})


# import requests
# def naver(req):
#     res = requests.get("https://naver.com/")
#     return HttpResponse(res.text)

# Create your views here.



from django.http import HttpResponse
from django.shortcuts import render

def gugu(req, num):

    # classical
    mul_table = []
    for i in range(1, 10):
        mul_text = f"{num} * {i} = {num * i}"
        mul_table.append(mul_text)
    print(1, mul_table)

    # list comprehension
    mul_table = [f"{num} * {i} = {num * i}" for i in range(1, 10)]
    print(2, "<br>".join(mul_table))

    # map + functinal
    mul_table = list(map(lambda i: f"{num} * {i} = {num * i}", range(1, 10)))
    print(3, "\n".join(mul_table))

    return render(req, 'toy/gugu.html', {'mul_table': mul_table})

# import requests
# def naver(req):
#     res = requests.get("https://naver.com/")
#     return HttpResponse(res.text)