import requests
url_photo=input("enter web photo:")
reponse=requests.get(url_photo)

if reponse.status_code==200:
    with open("my_downloads_image.png,jpeg","wb")as file:
        file.write(reponse.content)
    print("sucess telecharger")
else:
    print("impossible")