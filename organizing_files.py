import os
import numpy as np
import shutil
import re
from glob import glob1


nazwa_folderu=''
pattern='location:'
for txtFile in glob1("G:/Python/_resources/Pliki", "*.txt"):
    #nazwa_folderu=''
    with open(("G:/Python/_resources/Pliki/"+txtFile), "r") as plik:
        line = plik.readlines()
        for s in line:
            #print(s)
            #print ((type('location:dir2')))
            match = re.search(pattern, s)
            if match:
                temp=s.split(":")
                nazwa_folderu=temp[-1]
                nazwa_folderu=nazwa_folderu[0:4]
                print(nazwa_folderu)
    if(os.path.isdir("G:/Python/_resources/Pliki/"+nazwa_folderu)==False):
        os.mkdir(("G:/Python/_resources/Pliki/"+(nazwa_folderu)))
    shutil.move(("G:/Python/_resources/Pliki/"+txtFile), ("G:/Python/_resources/Pliki/"+nazwa_folderu))

    #print ("Plik text: "+txtFile)

