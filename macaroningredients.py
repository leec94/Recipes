'''
Caroline Lee, 7-28-15
'''

TOTALRECIPES = 2

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def main():
    recipenum = input("Which recipe (insert positive integer): ")
    if is_int(recipenum):
        recipenum = int(recipenum)
        if (recipenum > TOTALRECIPES) or (recipenum < 1):
            print ("Invalid number, first recipe will be calculated")
            recipenum = 1
    else:
        print("Invalid number, first recipe will be calculated")
        recipenum = 1
        
    print("")
    eggwhites = input("Amount of egg whites (g): ")

    if is_number(eggwhites):
        if (recipenum == 1):
            #first recipe based on averages found on the internet, 7-27-15
             eggwhites = float(eggwhites)
             gran = round(eggwhites * 0.65 * 100) / 100
             almond = round(eggwhites * 0.72 * 100) / 100
             powd = round(eggwhites * 1.5 * 100) / 100
             tartar = (round((eggwhites/36) *(0.125) *1000 + 75) // 125)
             vanilla = (round((eggwhites/36) *(0.5) *1000 + 75)// 125)

        elif (recipenum == 2):
            #tweaks from recipe one, 7-28-15
            eggwhites = float(eggwhites)
            gran = round(eggwhites * 0.6 * 100) / 100
            almond = round(eggwhites * 1.13 * 100) / 100
            powd = round(eggwhites * 1.7 * 100) / 100
            tartar = (((eggwhites/36) *(0.125) *1000 + 75) // 125)
            vanilla = (((eggwhites/36) *(0.5) *1000 + 75 )// 125)

        print (str(gran) + "g granulated sugar")
        print (str(almond) + "g almond flour")
        print (str(powd) + "g powdered sugar")
        print (str(vanilla) + "/8 tsp vanilla extract")
        print (str(tartar) + "/8 tsp cream of tartar (if not using copper bowl) \n")
                
main()
