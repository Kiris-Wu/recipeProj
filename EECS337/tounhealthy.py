import recipeProj.EECS337.recipegenerator as recipe
import recipeProj.EECS337.SL as sl
import copy
meas_ingred={
    "salt":[{"teaspoon":0.5},{"tablespoon":0.2},{"cup":0.01}],
    "oil":[{"teaspoon":2},{"tablespoon":1},{"cup":0.1}],
    "sugar":[{"teaspoon":0.5},{"tablespoon":0.2},{"cup":0.02}],

}
meas_list=["teaspoon","tablespoon","cup"]
condilist=["salt","oil","sugar"]
meat=["beef","chicken","pork","turkey","steak","ham","bulk","roast","bacon","sausage","meat","lamb","gigot","drumstick","wing","veal","leg","rib","hen","duck","goose","rabbit"]
unhealth_method_mapping_from=[["simmer","steam","boil","stew","blanch","braise"],["roast","broil","bake","saute","sear","grill"]]
unhealth_method_mapping_to=["smoke","fry"]
unhealth_tool_mapping_from=[["steamer","cooker","pot","skillet"],["toaster","oven","grill","wok"]]
unhealth_tool_mapping_to=["stove","pan"]
toolist=["steamer","cooker","pot","skillet","toaster","oven","grill","wok"]

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
        if(tempname.find(j)!=-1):
           tempq=round(ingred[i]['quantity']*2,2)
           ingred[i]['quantity']=tempq



########################increase meat

for i in range(len(ingred)):
    tempname=ingred[i]['name']
    for j in meat:
        if(tempname.find(j)!=-1):
            tempq=ingred[i]['quantity']
            if(tempq!=0):
                ingred[i]['quantity']=round(tempq*2,2)
                break

##############################change cook method and tools
newct=[]
for i in range(len(cm)):
    for j in range(len(unhealth_method_mapping_from)):
        if(cm[i] in unhealth_method_mapping_from[j] ):
            if(unhealth_method_mapping_to[j] not in cm):
                cm[i]=unhealth_method_mapping_to[j]
                newct.append(unhealth_tool_mapping_to[j])
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
myrecipe["title"]+="(to unhealthy)"
print("---------after transform")
print(myrecipe)

sl.file_name+="(to unhealthy style)"
sl.saving(oldrecipe,myrecipe)

