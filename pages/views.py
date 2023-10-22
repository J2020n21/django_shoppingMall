from django.shortcuts import render

def mainpage(req):
    return render(req, 'pages/mainpage.html')

def company(req):
    return render(req, 'pages/company_info.html')

def login(req):
    return render(req, 'pages/login.html')

def signUp(req):
    return render(req, 'pages/sign_up.html')

def myPage(req):
    return render(req, 'pages/my_page.html')