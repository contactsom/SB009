import getpass

password=getpass.getpass(prompt='Enter Your Password ?')
if password=='admin':
    print("Login")
else:
    print("Login Failed ")