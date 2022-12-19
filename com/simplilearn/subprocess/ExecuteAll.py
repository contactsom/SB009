import subprocess
import os

def executeC():
    s=subprocess.check_call("gcc HelloWorld.c -o out1;./out1", shell=True)
    print(",return code",s)


def executeCPP():
    data,temp = os.pipe()
    os.write(temp,bytes ("5 10 \n","utf-8"))
    os.close(temp)
    s = subprocess.check_output("g++ HelloWorld.cpp -o out2;./out2",stdin=data, shell=True)
    print(s.decode("utf-8"))

def executeJava():
    s = subprocess.check_output("javac HelloWorld.java;java HelloWorld ",shell=True)
    print(s.decode("utf-8"))

if __name__=="__main__":
    executeC()
    executeCPP()
    executeJava()