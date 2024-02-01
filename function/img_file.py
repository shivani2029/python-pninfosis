f=open("./function/santa.jpg", "rb")
data=f.read()
f.close()

with open("D:copy_santa.jpg", "wb") as img_file:
    img_file.write(data)