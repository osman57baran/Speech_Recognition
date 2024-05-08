from speech_recog import speech_en
import random

seviyeler = {
    "kolay": ["dairy", "mouse", "computer"],
    "orta": ["programming", "algorithm", "developer"],
    "zor": ["neural network", "machine learning", "artificial intelligence"]
}

def play_game(level):
    zorluk=input("Hangi zorluk saviyesi(kolay,orta,zor)")
    kelime=random.choice(seviyeler[zorluk])
    print(kelime)
sozcuk=play_game("zorluk")
print(sozcuk)    

if speech_en==sozcuk:
    print("doğru")
else:
    print("yanlış")  