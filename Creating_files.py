import numpy as np
import os
import random
import string

lista_slow=[('dir'+str(i)) for i in range(5)]

def random_word_generator():
    alphabet=string.ascii_letters
    slowo=''
    for i in range(random.randint(1, 20)):
        slowo+=random.choice(alphabet)
    return slowo

def random_files_generator():
    nazwa_pliku=random_word_generator()
    zdanie=''
    max_linijka=random.randint(4,50)
    linijka_location=random.randint(0,max_linijka)
    for i in range(max_linijka):
        if i!=linijka_location:
            zdanie+=" "+random_word_generator()
        else:
            zdanie+=" "+"location:"+random.choice(lista_slow)

    with open(("G:/Python/_resources/Pliki/"+random_word_generator()+".txt"), "w") as plik:
        plik.writelines([s + "\n" for s in zdanie.split()])

a=int(random.randint(5, 15))
for i in range(a):
    random_files_generator()
