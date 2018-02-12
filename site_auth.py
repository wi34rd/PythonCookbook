import http.cookiejar
import os.path
import requests


cookies_filename = 'cookies.txt'
session = requests.Session()
session.cookies = http.cookiejar.LWPCookieJar(cookies_filename)

if os.path.exists(cookies_filename):
    session.cookies.load()

responce = session.get('<нужный URL>')

if responce.url == '':
    data = {
        'username': '<username>',
        'password': '<password>'
    }
    session.post('<страница авторизации>', data=data)
    # иногда авторизовать может и нужная страница, тогда следующая строка кода не нужна
    responce = session.get('<нужный URL>')

session.cookies.save()
