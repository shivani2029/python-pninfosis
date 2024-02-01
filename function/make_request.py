import requests

url = "https://dog.ceo/api/breeds/image/random"

# img_url = "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg"

response = requests.get(url)
print(response.headers.get("Content-Type"))

# with open("image.jpg","wb") as file:
#     file.write(response.content)
j_data = response.json()
str_data = response.text
print("string data",str_data)
print("json_data:",j_data)