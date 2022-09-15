from time import sleep 
import speech_recognition as sr
#import cv2
#image = cv2.imread('/home/ahnaf/Pictures/thanks.png')
#image = cv2.resize(image, (187, 180))
from PIL import Image
im = Image.open(r"/home/ahnaf/Pictures/thanks.png")
im2 = Image.open(r"/home/ahnaf/Pictures/hello.jpg")
im3 = Image.open(r"/home/ahnaf/Pictures/help.png")
im4 = Image.open(r"/home/ahnaf/Pictures/yes.jpg")
import psutil 
voice = False
r = sr.Recognizer()
while True:  
    with sr.Microphone() as source:                                            
        voice = False
        while(voice == False):
            print("Speak:")
            audio = r.listen(source)
            try:
                speechString = r.recognize_google(audio)
                print(speechString)
                voice = True
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
        if speechString == "thanks":
            im.show()
            #cv2.imshow("Sign", image)
            sleep(5)
            #cv2.destroyAllWindows()
            for proc in psutil.process_iter():
                if proc.name() == "display":
                    proc.kill()
        if speechString == "hello":
            im2.show()
            #cv2.imshow("Sign", image)
            sleep(5)
            #cv2.destroyAllWindows()
            for proc in psutil.process_iter():
                if proc.name() == "display":
                    proc.kill()
        if speechString == "help":
            im3.show()
            #cv2.imshow("Sign", image)
            sleep(5)
            #cv2.destroyAllWindows()
            for proc in psutil.process_iter():
                if proc.name() == "display":
                    proc.kill()
        if speechString == "yes":
            im4.show()
            #cv2.imshow("Sign", image)
            sleep(5)
            #cv2.destroyAllWindows()
            for proc in psutil.process_iter():
                if proc.name() == "display":
                    proc.kill()
        if speechString == "exit":
            print("...")
            sleep(1)
            print("...")
            sleep(1)
            print("Goodbye")
            exit()