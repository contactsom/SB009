import json

teacherData = {
        "name":"ABC",
        "email":"abc@gmail.com",
        "phone":"912345",
        "subject":["JAVA","PYTHON","C","C++"]
}

with open("file1.json","w") as f :
    json.dump(teacherData,f)