import json
file_name="myrecipeoutput"
file_suf=".txt"

def saving(pre,nre):
    whole_name = file_name + file_suf
    with open(whole_name, 'w') as file_obj:
        file_obj.write("-------Before--------\n")
        file_obj.write(json.dumps(pre,sort_keys=True, indent=4, separators=(',', ': ')))
        file_obj.write("\n")
        file_obj.write("-------After-------\n")
        file_obj.write(json.dumps(nre, sort_keys=True, indent=4, separators=(',', ': ')))
        print("Successfully saving!")

def savingsingle(re):
    whole_name = file_name + file_suf
    with open(whole_name, 'w') as file_obj:
        file_obj.write("-------Extracting information--------\n")
        file_obj.write(json.dumps(re, sort_keys=True, indent=4, separators=(',', ': ')))
        print("Successfully saving!")
