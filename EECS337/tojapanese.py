import recipegenerator as recipe
import SL as sl
import scrapeurl as curl
from difflib import SequenceMatcher
import nltk
import collections
import copy
general_condi=["oil","soy sauce","vinegar","pepper","sauce","wine","flour"]
chinese_condi_mapping_from=["oil",["soy sauce","oyster sauce","soy","sauce"],"vinegar","pepper",["ketchup","mayonnaise","mustard","curry","doenjang","barbeque"],"wine",["flour","cornstarch"]]
chinese_condi_mapping_to=["sesame oil","mentsuyu","japanese rice vinegar","rayu","teriyaki","mirin","kinako"]
########################water related/heat related
chinese_method_mapping_from=[["simmer","steam","smoke","stew","blanch","braise"],["roast","saute","bake","grill","sear"]]
chinese_method_mapping_to=["boil","broil"]

chinese_tool_mapping_from=[["steamer","cooker","pot"],["toaster","oven","wok"]]
chinese_tool_mapping_to=["skillet","pan"]


allingred=[]
allcm=[]

'''
japaneseurl=curl.japaneseurl()

for i in japaneseurl:
    myrecipe=recipe.returnRecipe(i)
    allcm=allcm+myrecipe['cooking method']
    tempingred=myrecipe['ingredients']
    for j in tempingred:
        allingred.append(j["name"])

ti=collections.Counter(allingred)
ltopi=len(ti)
Topi=ti.most_common(ltopi)
print(Topi)
print("-------------")

tcm=collections.Counter(allcm)
ltopcm=len(tcm)
Topcm=tcm.most_common(ltopcm)

print(Topcm)







'''

##############################################test transform
url = input("Please input URL(type a space in the end then enter): ")
print("You want to transform recipe url is :"+ url)
url=url.strip()
if(url==""):
    print("You didn't enter anything, using the default link...")
    url="https://www.allrecipes.com/recipe/220125/slow-cooker-beef-pot-roast/?clickId=right%20rail0&internalSource=rr_feed_recipe_sb&referringId=237320%20referringContentType%3Drecipe"
myrecipe=recipe.returnRecipe(url)
print("-----------previous recipe")
oldrecipe=copy.deepcopy(myrecipe)
print(myrecipe)
cm=myrecipe['cooking method']
ingred=myrecipe['ingredients']
#direct=myrecipe['step']
ct=myrecipe['cooking tools']
namelist=[]
for i in range(len(cm)):
    for j in range(len(chinese_method_mapping_from)):
        if(cm[i] in chinese_method_mapping_from[j] and chinese_method_mapping_to[j] not in cm):
            cm[i]=chinese_method_mapping_to[j]
myrecipe['cooking method']=cm
for i in range(len(ct)):
    for j in range(len(chinese_tool_mapping_from)):
        if(ct[i] in chinese_tool_mapping_from[j] and chinese_tool_mapping_to[j] not in ct):
            ct[i]=chinese_tool_mapping_to[j]
myrecipe['cooking tools']=ct
for j in range(len(ingred)):
    prevname=ingred[j]["name"]
    namelist.append(prevname)
    flag=0
    for i in range(len(chinese_condi_mapping_from)):
        if(flag==1):
            break
        if(type(chinese_condi_mapping_from[i])==list):
            for k in chinese_condi_mapping_from[i]:
                if(prevname.find(k)!=-1):
                    if(chinese_condi_mapping_to[i] not in namelist):
                        prevname=chinese_condi_mapping_to[i]
                        ingred[j]["name"]=prevname
                        namelist[j]=prevname
                        flag=1
                        break
                    else:
                        thisq=ingred[j]["quantity"]
                        indexn=namelist.index(chinese_condi_mapping_to[i])
                        thatq=ingred[indexn]["quantity"]
                        ingred[indexn]["quantity"]=thisq+thatq
                        ingred[j]["name"]="None"
                        flag = 1
                        break
        else:
            if(prevname.find(chinese_condi_mapping_from[i])!=-1):
                if (chinese_condi_mapping_to[i] not in namelist):
                    prevname = chinese_condi_mapping_to[i]
                    ingred[j]["name"] = prevname
                    namelist[j] = prevname
                    flag = 1
                else:
                    thisq = ingred[j]["quantity"]
                    indexn = namelist.index(chinese_condi_mapping_to[i])
                    thatq = ingred[indexn]["quantity"]
                    ingred[indexn]["quantity"] = thisq + thatq
                    ingred[j]["name"] = "None"
                    flag = 1
newingred=[]
for j in range(len(ingred)):
    prevname=ingred[j]["name"]
    if(prevname!="None"):
        newingred.append(ingred[j])
myrecipe['ingredients']=newingred
myrecipe["title"]+="(to Japanese style)"
print("---------after transform")
print(myrecipe)


sl.file_name+="(to Japanese style)"
sl.saving(oldrecipe,myrecipe)

