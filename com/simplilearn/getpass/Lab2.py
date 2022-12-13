import getpass

securityQuestion=getpass.getpass(prompt='your fav book ?')
if securityQuestion.upper()=='JAVA':
    print("matched - COrrect")
else:
    print("Inncorrect")