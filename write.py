f=open("one.txt","w")
f.write("hello!\n")
f.write("welcome to python file\n")
f.write("lerning is fun!\n")
f.close()

f=open("two.txt","w")
f.write("new content only\n")
f.close()

f=open("two.txt","a")
f.write("this line is addad at the end.\n")
f.close()

f=open("two.txt","w")
lines=[
    "python programing\n"
    "file handing\n"
    "error handing\n"
    "exception handing\n"
]
f.writelines(lines)
f.close()




