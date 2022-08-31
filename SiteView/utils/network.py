import os

def Ping(url) :
    if(os.system('ping -c 1 -w 2 {}'.format(url))==0):
        return True
    else:
        return False

if __name__ == '__main__' :

    print(Ping('baidu.com.123'))