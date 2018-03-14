import requests
import re
import nltk
from nltk.stem import WordNetLemmatizer

from bs4 import BeautifulSoup as bs

#diection/title -primary
cookdict=["grill","fry","saute","boil","roast","bake","sear","poach","simmer","broil","steam","blanch","braise","stew","smoke","sour"]
# ingredient
o_cookdict=["chop","grate","stir","shake","mince","crush","squeeze","blend","separate","grease"]

#direction
ctdict=["teaspoon","tablespoon","cup","stove","oven","bowl","skillet","cooker","pan","oven","steamer","toaster","pot","wok"]
le = WordNetLemmatizer()


#transfer some text description of quantity to numbers

###CD single token
def str2val (str) :
    ret=0.0
    if str.find('/')!=-1 :
        sub=str.split('/')
        ret += round(float(sub[0])/float(sub[1]),2)
    else :
        ret += int(str)
    return ret


#ingredient parts
def convert2struct( strr,o_cooking ) :
    ingreitem = {}
    step = 0
    name=''
    qt = 0.0
    meas = ''
    desc = ''
    prep = ''
    #in case of 'some (some) some'
    quota = re.search('(.*?)\((.*?)\)(.*)',strr)
    if quota :
        #separate () from the whole sentence, directly in description
        desc = quota[2].strip()+', '
        # connect the rest, send to the next step
        strr = quota[1]+quota[3]

    tokens = nltk.word_tokenize(strr)
    tagged = nltk.pos_tag(tokens)
    taglen = len(tagged)
    for i in range(taglen):
        if (tagged[i][1] =='CD' and (not tagged[i][0].isalpha())):
            qt += str2val(tagged[i][0])
        #########################first CD-->measurement, next--->preeparation
            if step ==0 :
                step = 1
            else :
                prep += ' ' + tagged[i][0]
        else :
            #hard occuring other verb type
            if tagged[i][1] =="VBD" :
                o_cooking.append(le.lemmatize(tagged[i][0],'v'))

            #no quantity
            if step == 0 :
                # ingred-noun
                step =2
                if tagged[i][1]=='NN' or tagged[i][1]=='NNS' or tagged[i][1]=='NNP' or tagged[i][1]=='NNPS' or tagged[i][1]=='FW' or tagged[i][1]=='JJ' :
                    name = tagged[i][0]
                else :
                    desc += ' ' + tagged[i][0]

            #####has processed quantity, followed with measurement
            elif step == 1:
                step +=1
                if tagged[i][1]=='NN' or tagged[i][1]=='NNS' or tagged[i][1]=='NNP' or tagged[i][1]=='NNPS'or tagged[i][1]=='FW' or tagged[i][1]=='JJ' :
                    meas += ' ' + tagged[i][0]
                else :
                    desc += ' ' + tagged[i][0]

            ###############-quantity,measurement, then ingred
            elif step >= 2 and step < 20 :
                step +=1
                if tagged[i][1]=='NN' or tagged[i][1]=='NNS' or tagged[i][1]=='NNP' or tagged[i][1]=='NNPS'or tagged[i][1]=='FW' or tagged[i][1]=='JJ' :
                    name += ' ' + tagged[i][0]
                elif tagged[i][1]==',' :
                    ############if has comma, then could be ingred-prepration
                    step =20
                else :
                    desc += ' ' + tagged[i][0]
            else :
                if tagged[i][1]=='NN' or tagged[i][1]=='NNS' or tagged[i][1]=='NNP' or tagged[i][1]=='NNPS'or tagged[i][1]=='FW' or tagged[i][1]=='JJ' :
                    name += ' ' + tagged[i][0]
                else :
                    prep += ' ' + tagged[i][0]

    if step==2 :  # in case of "1 egg"
        name = meas
        meas = "none"

    if name=="" : name="none"
    if meas=="" : meas="none"
    if desc=="" : desc="none"
    if prep=="" : prep="none"

    if(name!="none"):
        ingreitem['name'] = name.strip()
        ingreitem['quantity'] = qt
        ingreitem['measurement'] = meas.strip()
        ingreitem['descriptor'] = desc.strip()
        ingreitem['preparation'] = prep.strip()
        return ingreitem
    else:
        return None





#######direction/title---->method
def extractcookingmethod(str,p_cooking,o_cooking,cookingtools) :
    tokens = nltk.word_tokenize(str)
    tagged = nltk.pos_tag(tokens)
    taglen = len(tagged)
    for i in range(taglen):
        if tagged[i][1] =="VB" or tagged[i][1] =="VBD" or tagged[i][1] =="VBG" or tagged[i][1] =="VBN" or tagged[i][1] =="VBP"  or tagged[i][1] =="VBZ":
#            print(tagged[i][0])

            #find the stem of verb
            vbn = le.lemmatize(tagged[i][0],'v')
            ################find whther in primary or other
            k=cookdict.count(vbn.lower())
            if k :
                p_cooking.append(vbn.lower())

            k = o_cookdict.count(vbn.lower())
            if k:
                o_cooking.append(vbn.lower())

        #####some methond was tagged to noun, e,g, saute------>tools,methond ---->find by dic
        if tagged[i][1] == 'NN' or tagged[i][1] == 'NNS' or tagged[i][1] == 'NNP' or tagged[i][1] == 'NNPS'or tagged[i][1]=='FW' :
#            print(tagged[i][0])
            vbn = le.lemmatize(tagged[i][0])
            k = ctdict.count(vbn.lower())
            if k:
                cookingtools.append(vbn.lower())
            vbn = le.lemmatize(tagged[i][0],"v")
            k = cookdict.count(vbn.lower())
            if k:
                p_cooking.append(vbn.lower())
            k = o_cookdict.count(vbn.lower())
            if k:
                o_cooking.append(vbn.lower())
    return 1

###############or use dict. to delete dup.
def processlist (cooklist):

    templist = []
    listlen = len(cooklist)
    for i in range(listlen) :
        if ( templist.count(cooklist[i])==0 ):
            templist.append(cooklist[i])
    return templist

def returnRecipe(url):
    p_cooking = []
    o_cooking = []
    cookingtools = []
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    }
    #url='https://www.allrecipes.com/recipe/12976/cowboy-stew-i/?internalSource=previously%20viewed&referringContentType=home%20page&clickId=cardslot%205'

    recipes = {}
    if(url==None):
        url = input("Please input URL(type a space in the end then enter): ")

        print("You want to transform recipe url is :"+ url)

        url=url.strip()

    cont = requests.get(url,timeout=150,headers=headers).content

    soup = bs(cont, "html.parser")

    #print(soup.prettify())

    ######generate stem


    ingred_time = ""
    ingred_servings = ""
    ingred_cals = ""

    infos = soup.find("title")
    strsp = infos.text.split(' - ')  #######delete web name
    recipes['title'] = strsp[0]

    print(strsp[0])

    ######first extract cooking methond from title
    extractcookingmethod(strsp[0],p_cooking,o_cooking,cookingtools)

    #Ingredients
    print("\nIngredients")

    ingred =[]
    infos = soup.find("ul",{"class":"checklist dropdownwrapper list-ingredients-1"})

    if infos :
        ingredinfo = infos.find_all("span",{"class":"recipe-ingred_txt added"})
        if ingredinfo :
            for i in ingredinfo :
                print(i.text)
                ingreitem = convert2struct(i.text,o_cooking)
    #            print (ingreitem)
                if(ingreitem!=None):
                    ingred.append(ingreitem)

    infos = soup.find("ul",{"class":"checklist dropdownwrapper list-ingredients-2"})        ##############how many????

    if infos :
        ingredinfo = infos.find_all("span",{"class":"recipe-ingred_txt added"})
        if ingredinfo :
            for i in ingredinfo :
                print(i.text)
                ingreitem = convert2struct(i.text,o_cooking)
    #            print (ingreitem)
                if (ingreitem != None):
                    ingred.append(ingreitem)

    recipes['ingredients'] = ingred

    # Directions
    print("\nDirections")

    direct=[]
    ################second extracting cooking methond by directions
    infos = soup.find("ol",{"class":"list-numbers recipe-directions__list"})

    if infos :
        directinfo = infos.find_all("span",{"class":"recipe-directions__list--item"})
        if directinfo :
            stepn=len(directinfo)
            for i in range(stepn) :
#                print(directinfo[i].text)
                tempdiret=directinfo[i].text
                direct.append("["+str(i+1)+"]:"+tempdiret)
                extractcookingmethod(directinfo[i].text,p_cooking,o_cooking,cookingtools)

    # footnotes ----nutrition/addtional info.

    fn={}

    fnsec = soup.find_all("section",{"class":"recipe-footnotes"})

    if fnsec :
        for fninfo in fnsec :
            i = fninfo.find("h4", {"class": "recipe-footnotes__h4"})

            print("\n"+i.text.strip())
            if i.text.strip() =="Nutrition Facts":    #nutrition-info
                fn_nu = fninfo.find("span",{"itemprop":"calories"})
                if fn_nu:
                    fn_cal =  fn_nu.text
                    fn['calories']=fn_cal
#                    print(fn_cal)

                fn_nu = fninfo.find("span",{"itemprop":"fatContent"})
                if fn_nu:
                    fn_fat =  fn_nu.text
                    fn['fatContent']=fn_fat+" g fat"
#                    print(fn_fat+" g fat")

                fn_nu = fninfo.find("span",{"itemprop":"carbohydrateContent"})
                if fn_nu:
                    fn_car =  fn_nu.text
                    fn['carbohydrateContent']=fn_car+" g carbohydrates"
#                    print(fn_car+" g carbohydrates")

                fn_nu = fninfo.find("span",{"itemprop":"proteinContent"})
                if fn_nu:
                    fn_pro =  fn_nu.text
                    fn['proteinContent']=fn_pro+" g protein"
#                    print(fn_pro+" g protein")

                fn_nu = fninfo.find("span",{"itemprop":"cholesterolContent"})
                if fn_nu:
                    fn_cho =  fn_nu.text
                    fn['cholesterolContent']=fn_cho+" mg cholesterol"
#                    print(fn_cho+" mg cholesterol")

                fn_nu = fninfo.find("span",{"itemprop":"sodiumContent"})
                if fn_nu:
                    fn_sod =  fn_nu.text
                    fn['sodiumContent']=fn_sod+" mg sodium"
#                    print(fn_sod+" mg sodium")
            else :

                #sometimes has info for cook method
                fn_ginfo = fninfo.find_all("li")
                if fn_ginfo :
                    for j in fn_ginfo:
                        print(j.text)
                        extractcookingmethod(j.text,p_cooking,o_cooking,cookingtools)

    p_cooking = processlist(p_cooking)
    o_cooking = processlist(o_cooking)
    cookingtools = processlist(cookingtools)

    recipes['cooking method'] = p_cooking
    recipes['other cooking method'] = o_cooking
    recipes['cooking tools'] = cookingtools
#    recipes['step']=direct
#    recipes['nutrition facts']=fn
    print(recipes)

    return recipes
