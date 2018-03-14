import EECS337.recipegenerator as recipe
import EECS337.SL as sl
import copy
def islistInclude(targetlist,name):
    flag=0
    for i in targetlist:
        if(name.find(i)!=-1):
            flag=1
    if(flag==1):
        return True
    else:
        return False
def isInclude(namelist,target):
    flag=0
    for i in namelist:
        if(i.find(target)!=-1):
            flag=1
    if(flag==1):
        return True
    else:
        return False
general_meat=[
    "beef","cod fish","flounder","haddock","halibut","mahi","salmon","snapper","tilapia","trout",
    "tuna","walleye","clam","crab","lobster","mussel","octopus","squid","oyster","scallop","shrimp",
    "poultry","rib","hamburger","chicken","hen","duck","goose","rabbit","veal","venison",
    "lamb","pork","bacon","sausage","bratwurst","chorizo","kielbasa","turkey"
]
general_vege=[
    "bean","pea","lentils","apple","apricot","avocado","banana","berries","cherries","citrus","grapefruit",
    "lemon","lime","orange","coconut","date","fig","grape","kiwi","mango","melon","nectarine",
    "papaya","peach","pear","persimmon","pineapple","plum","pomegranate","raisin","mushroom",
    "artichoke","ratatouille","asparagus","beet","bell pepper","bok choy","broccoli","brussel sprout",
    "cabbage","carrot","cauliflower","celery root","chile pepper","corn","cucumber","eggplant","fennel",
    "garlic","green","arugula","chard","kale","lettuce","spinach","jicama","leek","nopales","okra",
    "olive","onion","parsnip","potatoe","radish","rhubarb","rhutabaga","shallot","squash","tomatillo",
    "tomato","turnip","water chestnut","yam"
]
general_dairy=["milk","butter","cheese","margarine","cream","yogurt","curd"]
general_dairy_vegan=["coconut milk","coconut butter","coconut cheese","coconut margarine","coconut cream","coconut yogurt","coconut curd"]
special_list_mapping_from=["egg","oil"]
special_list_mapping_to=["silken tofu","vegetable oil"]
vege_dairy=["soy","coconut","rice","almond","water chestnut","wheat"]
vege_oil=["vegetable","sesame","olive","coconut","peanut","sunflower","soy","cotton","rape","chili"]

vege_ingre_mapping_to=[
    "tempeh","tofu","seitan","gardein","eggplant","mushroom","bean","bok choy","broccoli","brussel sprout","lettuce","spinach","onion","carrot","corn",
    "cucumber","potato","tomato","cabbage","cauliflower","celery root","chile pepper","artichoke","ratatouille","asparagus","beet"
]
url = input("Please input URL(type a space in the end then enter): ")
print("You want to transform recipe url is :"+ url)
url=url.strip()
if(url==""):
    url="https://www.allrecipes.com/recipe/254940/honey-garlic-chicken-with-rosemary/?internalSource=previously%20viewed&referringContentType=home%20page&clickId=cardslot%2033"
myrecipe=recipe.returnRecipe(url)
print("-----------previous recipe")
print(myrecipe)
oldrecipe=copy.deepcopy(myrecipe)
ingred=myrecipe['ingredients']
#direct=myrecipe['step']
namelist=[]
for i in range(len(ingred)):
    namelist.append(ingred[i]['name'])
for i in range(len(ingred)):
    tempname=ingred[i]['name']
    flag=0
    if(tempname.find("egg")!=-1 ):
        if("silken tofu" not in namelist):
            ingred[i]['name'] = "silken tofu"
            ingred[i]['measurement'] = "pound"
            ingred[i]['descriptor'] = "none"
            ingred[i]['preparation'] = "none"
            namelist[i] = k
            continue
        else:
            ingred[i]['name']="none"
            continue

    if(tempname.find("oil")!=-1 ):
        if(islistInclude(vege_oil,tempname)):
            continue
        else:
            if ("vegetable oil" not in namelist):
                ingred[i]['name'] = "vegetable oil"
                ingred[i]['descriptor'] = "none"
                ingred[i]['preparation'] = "none"
                namelist[i] = k
                continue
            else:
                ingred[i]['name'] = "none"
                continue

    for j in general_meat:
        if(flag==1):
            break
        if(tempname.find(j)!=-1):
            for k in vege_ingre_mapping_to:
                if(not isInclude(namelist,k)):
                    ingred[i]['name']=k
                    ingred[i]['measurement']="ounce"
                    ingred[i]['descriptor']="none"
                    ingred[i]['preparation']="none"
                    namelist[i]=k
                    flag=1
                    break
    for j in range(len(general_dairy)):
        if(tempname.find(general_dairy[j])!=-1):
            if(islistInclude(vege_dairy,tempname)):
                break
            else:
                k=general_dairy_vegan[j]
                if(not isInclude(namelist,k)):
                    ingred[i]['name']=k
                    ingred[i]['measurement']="cup"
                    ingred[i]['descriptor']="none"
                    ingred[i]['preparation']="none"
                    namelist[i]=k
                    break
                else:
                    ingred[i]['name'] = "none"
                    break
newingred=[]
for i in range(len(ingred)):
    if(ingred[i]['name']!="none"):
        newingred.append(ingred[i])

myrecipe['ingredients']=newingred
myrecipe["title"]+="(to vegan)"
print("---------after transform")
print(myrecipe)

sl.file_name+="(to vegan style)"
sl.saving(oldrecipe,myrecipe)