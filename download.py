import requests

from bs4 import BeautifulSoup


def photo():
    urlofphoto = input('please input link of photo : ').strip()
    nameofphoto = input(
        'please input the name that you want to save it : ').strip()
    urlofphoto = urlofphoto + ".png"
    response = requests.get(urlofphoto)
    file = open(r"C:\Users\3laam\OneDrive\Pictures\0" +
                nameofphoto+".JPEG", "wb")
    file.write(response.content)


def single_video():
    linkofvideo = input('please input link of video : ').strip()
    response_1 = requests.get(linkofvideo)
    nameofvideo = input(
        'please input the name that you want to save it : ').strip()
    nameofvideo = nameofvideo + ".mp4"
    file_1 = open(r"C:\Users\3laam\Videos\0" + nameofvideo + ".mp4", "wb")
    file_1.write(response_1.content)
    print("download completed")


def file_pdf():
    linkoffile = input('please input link of file : ').strip()
    r_2 = requests.get(linkoffile)
    nameoffile = input(
        'please input the name that you want to save it : ').strip()
    file_2 = open(r"C:\Users\3laam\Documents\0"+nameoffile+".pdf", "wb")
    file_2.write(r_2.content)


def file_zip():
    linkoffilezip = input('please input link of file : ').strip()
    nameoffilezip = input(
        'please input the name that you want to save it : ').strip()
    r_1 = requests.get(linkoffilezip)
    file_3 = open(r"C:\Users\3laam\Documents\0"+nameoffilezip+".zip", "wb")
    file_3.write(r_1.content)


def song():
    linkofsong = input('please input link of song : ').strip()
    r_3 = requests.get(linkofsong)
    nameofsong = input(
        'please input the name that you want to save it : ').strip()
    file_4 = open(r"C:\Users\3laam\Music\0"+nameofsong+".mp3", "wb")
    file_4.write(r_3.content)
    print("download completed")


while True:
    the_message = """
    welcome to our software in this program you can :
    download an image by type >= A
    download single video by type >= B
    download file pdf by type >= C
    download file ZIP by type >= D
    download file Song by type >= E
    exit the program >= N
    
    """
    print(the_message)
    user_input = input("please input the opthion : ").strip().capitalize()
    if user_input == "A":
        photo()
    elif user_input == "B":

        single_video()
        print("download completed")

    elif user_input == "C":
        file_pdf()
        print("download completed")

    elif user_input == "D":
        file_zip()
        print("download completed")

    elif user_input == "E":
        song()
        print("download completed")

    elif user_input == "N":
        print("good bye")
        exit()
    else:
        print("error input please choose(a,b,c,d,e or N)")
