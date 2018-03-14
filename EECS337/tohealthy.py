import EECS337.recipegenerator as recipe
import EECS337.SL as sl
import copy
meas_ingred={
    "salt":[{"teaspoon":0.5},{"tablespoon":0.2},{"cup":0.01}],
    "oil":[{"teaspoon":2},{"tablespoon":1},{"cup":0.1}],
    "sugar":[{"teaspoon":0.5},{"tablespoon":0.2},{"cup":0.02}],

}
meas_list=["teaspoon","tablespoon","cup"]
condilist=["salt","oil","sugar"]
meat=["beef","chicken","pork","turkey","steak","ham","bulk","roast","bacon","sausage","meat","lamb","gigot","drumstick","wing","veal","leg","rib","hen","duck","goose","rabbit"]
health_method_mapping_from=[["simmer","steam","smoke","stew","blanch","braise"],["roast","broil","bake","saute","sear"]]
health_method_mapping_to=["boil","grill"]
health_tool_mapping_from=[["steamer","cooker","pot"],["toaster","oven","pan","wok"]]
health_tool_mapping_to=["skillet","grill"]
toolist=["steamer","cooker","pot","toaster","oven","pan","wok"]

url="https://www.allrecipes.com/recipe/220125/slow-cooker-beef-pot-roast/?clickId=right%20rail0&internalSource=rr_feed_recipe_sb&referringId=237320%20referringContentType%3Drecipe"
myrecipe=recipe.returnRecipe(url)
print("-----------previous recipe")
print(myrecipe)
oldrecipe=copy.deepcopy(myrecipe)
cm=myrecipe['cooking method']
ingred=myrecipe['ingredients']
#direct=myrecipe['step']
ct=myrecipe['cooking tools']


#############################process condition
for i in range(len(ingred)):
    tempname=ingred[i]['name']
    flag=0
    for j in condilist:
        if(flag==1):
            break
        if(tempname.find(j)!=-1):
            tempm=ingred[i]['measurement']
            for k in range(len(meas_list)):
                if(tempm.find(meas_list[k])!=-1):
                    qvalue=meas_ingred[j][k][meas_list[k]]
                    if(qvalue<ingred[i]['quantity']):
                        ingred[i]['quantity']=qvalue
                        flag=1
                        break



########################decrease meat

for i in range(len(ingred)):
    tempname=ingred[i]['name']
    for j in meat:
        if(tempname.find(j)!=-1):
            tempq=ingred[i]['quantity']
            if(tempq!=0):
                ingred[i]['quantity']=round(tempq/2,2)
                break

##############################change cook method and tools
newct=[]
for i in range(len(cm)):
    for j in range(len(health_method_mapping_from)):
        if(cm[i] in health_method_mapping_from[j] ):
            if(health_method_mapping_to[j] not in cm):
                cm[i]=health_method_mapping_to[j]
                newct.append(health_tool_mapping_to[j])
            else:
                cm[i]="none"
newcm=[]
for i in cm:
    if(i!="none"):
        newcm.append(i)
myrecipe['cooking method']=newcm
for i in range(len(ct)):
    if(ct[i] in toolist):
        ct[i]="none"
for i in ct:
    if(i!="none" and i not in newct):
        newct.append(i)
myrecipe['cooking tools']=newct


myrecipe['ingredients']=ingred
myrecipe["title"]+="(to healthy)"
print("---------after transform")
print(myrecipe)

sl.file_name+="(to healthy style)"
sl.saving(oldrecipe,myrecipe)



