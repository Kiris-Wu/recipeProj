import EECS337.recipegenerator as recipe
import EECS337.SL as sl
import  EECS337.scrapeurl as curl
from difflib import SequenceMatcher
import nltk
import collections
import copy
general_condi=["oil","soy sauce","vinegar","pepper","cumin","thyme","sugar","sauce","wine","flour"]
chinese_condi_mapping_from=["oil",["soy sauce","oyster sauce","soy","sauce"],"vinegar","pepper","cumin","thyme","sugar",["ketchup","mayonnaise","mustard","curry","miso","teriyaki","doenjang"],"wine","flour"]
chinese_condi_mapping_to=["chinese sesame oil","chinese lijingji sauce","chinese rice vinegar","chinese red pepper","chinese five spices powder","coriander","chinese maltose","chinese lao gan ma","chinese rice wine","cornstarch"]
########################water related/heat related
chinese_method_mapping_from=[["simmer","steam","smoke","stew","blanch","braise"],["roast","broil","bake","grill","sear"]]
chinese_method_mapping_to=["boil","saute"]

chinese_tool_mapping_from=[["steamer","cooker","pot"],["toaster","oven","pan"]]
chinese_tool_mapping_to=["skillet","wok"]


allingred=[]
allcm=[]
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def directiontrans(direct,vfrom,vto,index):
    if(index==-1):
        for i in range(len(direct)):
            for j in range(len(direct[i])):
                if(similar(direct[i][j],vfrom)>0.9):
                    direct[i] = direct[i].replace(direct[i][j],vto)


    else:
        for i in range(len(direct)):
            if(vfrom in direct[i]):
                direct[i]=direct[i].replace(vfrom,vto)
                continue
            if(general_condi[index] in direct[i]):
                direct[i]=direct[i].replace(general_condi[index],vto)
                continue

    return direct



########################count frequency for the descriptions of chinese cuisine to build mappings
'''
chineseurl=curl.chineseurl()

for i in chineseurl:
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
    print("You did not enter anything, using the default link...")
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
#            direct=directiontrans(direct,cm[i],chinese_method_mapping_to[j],-1)
            cm[i]=chinese_method_mapping_to[j]
myrecipe['cooking method']=cm
for i in range(len(ct)):
    for j in range(len(chinese_tool_mapping_from)):
        if(ct[i] in chinese_tool_mapping_from[j] and chinese_tool_mapping_to[j] not in ct):
#            direct=directiontrans(direct,ct[i],chinese_tool_mapping_to[j],-1)
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
#                        direct=directiontrans(direct,prevname,chinese_condi_mapping_to[i],i)
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
#                    direct = directiontrans(direct, prevname, chinese_condi_mapping_to[i],i)
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
myrecipe["title"]+="(to Chinese style)"
#myrecipe['step']=direct
print("---------after transform")
print(myrecipe)


sl.file_name+="(to Chinese style)"
sl.saving(oldrecipe,myrecipe)




