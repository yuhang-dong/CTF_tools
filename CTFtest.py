# _*_ coding:UTF-8 _*_
# main.py



'''
CTF密码题的一个小工具
md5加密、摩斯密码加解密、凯撒密码加解密和爆破、栅栏密码的解密和爆破、简单替换密码
爆破
'''



import source.md5_moudle
import source.b64_moudle
from source.morse_moudle import Morse
import source.caesar
import source.Railfence
import urllib.request


def begin():
    print('''
----------------------------------------------------------
        1、MD5加密                  10、栅栏解密
        2、MD5在线解密网址          11、栅栏爆破
        3、Base64加密               12、字符串反转
        4、Base64解密               13、URL编码
        5、Morse加密                14、URL解码
        6、Morse解密
        7、Caesar加密
        8、Caesar解密
        9、Caesar爆破
-----------------------------------------------------------
    ''')
    a = input('选择：')
    return int(a)

def URLDecode():
    a = input("URL:")
    b = urllib.request.quote(a,encoding='UTF-8')
    print(b)

def URLEncode():
    a = input("url:")
    b = urllib.request.unquote(a,encoding='UTF-8')
    print(b)


def fanzhuan():
    a = input('需要反转的字符串:')
    b = a[::-1]
    print(b)

def md5():
    a = input('需要加密的字符串:')
    b = md5_moudle.md5_encode(a)
    print("MD5('%s'):%s" % (a, b))


def md5_net():
    print('''
    如下在线解密网站：
            1、http://www.dmd5.com/
            2、http://www.xmd5.org/
            3、http://pmd5.com/
            4、http://www.cmd5.com/
    ''')


def b64de():
    string = input('需解密的字符串：')
    a = b64_moudle.b64decode(string)
    print(a)


def b64en():
    string = input('需加密字符串：')
    a = b64_moudle.b64encode(string)
    print(a)


def morse_en():
    a = Morse()
    b = a.morse_en()
    for i in b:
        print(i, end=' ')


def morse_de():
    a = Morse()
    b = a.morse_de()
    for i in b:
        print(i, end='')


def caesar_en():
    a = input('String=')
    key = input('key=')
    b = caesar.caesar_encode(a, key)
    print(b)


def caesar_de():
    a = input('String=')
    key = input('key=')
    b = caesar.caesar_decode(a, key)
    print(b)


def caesar_brute():
    a = input('String=')
    caesar.caesar_brute(a)


def raildecode():
    string = input('String=')
    key = input('key=')
    Railfence.Rail_decode(string, key)


def railbrute():
    string = input('String=')
    Railfence.Rail_brute(string)


def main():
    while True:
        a = begin()
        if a == 1:
            md5()
        elif a == 2:
            md5_net()
        elif a == 3:
            b64en()
        elif a == 4:
            b64de()
        elif a == 5:
            morse_en()
        elif a == 6:
            morse_de()
        elif a == 7:
            caesar_en()
        elif a == 8:
            caesar_de()
        elif a == 9:
            caesar_brute()
        elif a == 10:
            raildecode()
        elif a == 11:
            railbrute()
        elif a == 12:
            fanzhuan()
        elif a == 13:
            URLDecode()
        elif a == 14:
            URLEncode()

        b = input('\n继续？(T/F)').upper()
        if b == 'F':
            break


if __name__ == '__main__':
    main()
