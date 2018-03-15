# recipeProj
EECS 337 Team project by Xinyi Wu, Group 22

-----------------------------Version for programming language---------------------<br/>
Python 3.6\
-----------------------------Package list----------------------------------------<br/>
Standard python package:json,copy,collections,re,request

External python package:nltk 3.2.4,beautifulsoup4 4.6.0

all the external package could be gotten by pip or use anaconda

-----------------------------------------Relative path import----------------------------<br/>
Some the code are used by import in relative path. If you are using pycharm, even though 
import the code that in the same path, it will report a no-module-name error notice. If you 
are in that situation, ignore the notice and run the code directly .

-------------------------------------File specification-----------------------------------<br/>
The txt file named as "output-XXX-prep" are all preparation files(or reference files) for 
creating the transformation diactionary.<br/>

All the runnable code are in EECS337 folder.
>-supporting code:<br/>
    >>-SL.py :Save the code into disk and arrange them into a more readable format.<br/>
    >>-scrapeurl.py :Scrape special urls for the extraction of description. (e.g. scrapy 100 Chinese 
    recipe urls from Allrecipes.com)<br/>
    >>-dict.py :Output the txt files of "output-XXX-prep", which includes descriptions of ingredients
    of different recipe syles by frequency <br/>
    
>-recipe extraction code:<br/>
  >>-recipegenerator.py :Scrape recipe information from the given url and arrange them into readable format.
  >>-recipeNT.py :Output single recipe.<br/>
  
>-transformation code:<br/>

  >>-to(style).py :Transform the original recipes into special styles, output the previous and changed one.
  
--------------------------------------------How to run------------------------------------------------<br/>
All the transformation code with recipeNT could directly run.

These code will request you to input url with a space(without the space, you will be redirected to that webpage,
at least in pycharm), if you do not input anything and enter, the program will use a default url to run.

--------------------------------------------Server no response------------------------------------------<br/>
Because the program runtimely extract information from website, there is possible to occur problems from HTTP connection 
and server respondence. If such problem comes, just rerun the code.
