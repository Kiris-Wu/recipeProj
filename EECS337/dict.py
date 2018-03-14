import EECS337.recipegenerator as recipe
import  EECS337.scrapeurl as allurl
from difflib import SequenceMatcher
import nltk
import collections


allingred=[]
allcm=[]

chinese=allurl.chineseurl()
for i in chinese:
    myrecipe=recipe.returnRecipe(i)
    allcm=allcm+myrecipe['cooking method']
    tempingred=myrecipe['ingredients']
    for j in tempingred:
        allingred.append(j["measurement"])
print("-------------top measurement")
ti=collections.Counter(allingred)
ltopi=len(ti)
Topi=ti.most_common(ltopi)
print(Topi)
print("-------------top method")

tcm=collections.Counter(allcm)
ltopcm=len(tcm)
Topcm=tcm.most_common(ltopcm)

print(Topcm)

'''

print("-----------------top vegan description")

veganurl=allurl.veganurl()


for i in veganurl:
    myrecipe=recipe.returnRecipe(i)
    allcm=allcm+myrecipe['cooking method']
    tempingred=myrecipe['ingredients']
    for j in tempingred:
        allingred.append(j["name"])
print("-------------top ingredient")
ti=collections.Counter(allingred)
ltopi=len(ti)
Topi=ti.most_common(ltopi)
print(Topi)
print("-------------top method")

tcm=collections.Counter(allcm)
ltopcm=len(tcm)
Topcm=tcm.most_common(ltopcm)

print(Topcm)





######################################################
print("-----------------top vegetarian description")

vege=allurl.vegetarianurl()


for i in vege:
    myrecipe=recipe.returnRecipe(i)
    allcm=allcm+myrecipe['cooking method']
    tempingred=myrecipe['ingredients']
    for j in tempingred:
        allingred.append(j["name"])
print("-------------top ingredient")
ti=collections.Counter(allingred)
ltopi=len(ti)
Topi=ti.most_common(ltopi)
print(Topi)
print("-------------top method")

tcm=collections.Counter(allcm)
ltopcm=len(tcm)
Topcm=tcm.most_common(ltopcm)

print(Topcm)


print("-----------------top meat description")

meat=allurl.mandpurl()


for i in meat:
    myrecipe=recipe.returnRecipe(i)
    allcm=allcm+myrecipe['cooking method']
    tempingred=myrecipe['ingredients']
    for j in tempingred:
        allingred.append(j["name"])
print("-------------top ingredient")
ti=collections.Counter(allingred)
ltopi=len(ti)
Topi=ti.most_common(ltopi)
print(Topi)
print("-------------top method")

tcm=collections.Counter(allcm)
ltopcm=len(tcm)
Topcm=tcm.most_common(ltopcm)

print(Topcm)




print("-----------------top seafood description")

seafood=allurl.seafoodurl()


for i in seafood:
    myrecipe=recipe.returnRecipe(i)
    allcm=allcm+myrecipe['cooking method']
    tempingred=myrecipe['ingredients']
    for j in tempingred:
        allingred.append(j["name"])
print("-------------top ingredient")
ti=collections.Counter(allingred)
ltopi=len(ti)
Topi=ti.most_common(ltopi)
print(Topi)
print("-------------top method")

tcm=collections.Counter(allcm)
ltopcm=len(tcm)
Topcm=tcm.most_common(ltopcm)

print(Topcm)






print("-----------------top fruit description")

fruitandv=allurl.fruitandvurl()


for i in fruitandv:
    myrecipe=recipe.returnRecipe(i)
    allcm=allcm+myrecipe['cooking method']
    tempingred=myrecipe['ingredients']
    for j in tempingred:
        allingred.append(j["name"])
print("-------------top ingredient")
ti=collections.Counter(allingred)
ltopi=len(ti)
Topi=ti.most_common(ltopi)
print(Topi)
print("-------------top method")

tcm=collections.Counter(allcm)
ltopcm=len(tcm)
Topcm=tcm.most_common(ltopcm)

print(Topcm)

print("-----------------top dairy description")

dairy=allurl.dairyurl()


for i in dairy:
    myrecipe=recipe.returnRecipe(i)
    allcm=allcm+myrecipe['cooking method']
    tempingred=myrecipe['ingredients']
    for j in tempingred:
        allingred.append(j["name"])
print("-------------top ingredient")
ti=collections.Counter(allingred)
ltopi=len(ti)
Topi=ti.most_common(ltopi)
print(Topi)
print("-------------top method")

tcm=collections.Counter(allcm)
ltopcm=len(tcm)
Topcm=tcm.most_common(ltopcm)

print(Topcm)




print("-----------------top pandd description")

pandn=allurl.pandnurl()


for i in pandn:
    myrecipe=recipe.returnRecipe(i)
    allcm=allcm+myrecipe['cooking method']
    tempingred=myrecipe['ingredients']
    for j in tempingred:
        allingred.append(j["name"])
print("-------------top ingredient")
ti=collections.Counter(allingred)
ltopi=len(ti)
Topi=ti.most_common(ltopi)
print(Topi)
print("-------------top method")

tcm=collections.Counter(allcm)
ltopcm=len(tcm)
Topcm=tcm.most_common(ltopcm)

print(Topcm)
'''

