from landDatabase import *
import random

white = 0
green = 0
blue = 0
red = 0
black = 0
swamp = 0
colorless = 0

def mysplit(s):
    temp = s
    ##print(temp)
    number = 0
    name = ""
    for x in temp:
        if not x:
            break
        if x in numbers:
            number = x
            ##print(number)
        else:
            name = name + x + " " 
    
    
    return number, name.rstrip()

def multiline_input(sentinel=''):
    for inp in iter(input, sentinel):
        yield inp.split()
        
##copied code from internet

def gatherMana(list):
    keys = list.keys()

    global white
    global red
    global green
    global blue
    global black
    global colorless
    
    for i in keys:
        ##print(i)
        if i in lands:
            num = int(list.get(i))
            for x in lands.get(i).split(" "):
                ##print(x)
                if x == 'Red':
                    red += num
                    ##print(red)
                    ##print("updated red")
                elif x == 'White':
                    white += num
                elif x == 'Colorless':
                    colorless += num
                elif x == 'Green':
                    green += num
                elif x == 'Blue':
                    blue += num
                elif x == 'Black':
                    black += num
            ##number of lands
    ##print(red)
    
    
def calcAverageLands(numTurns):
    AverageWhite = 0
    AverageRed = 0
    AverageBlack = 0
    AverageBlue = 0
    AverageGreen = 0
    AverageColorless = 0
    
    for x in range(1000):
        
        total = 99
        whitetemp = white
        redtemp = red
        blacktemp = black
        bluetemp = blue
        greentemp = green
        colorlesstemp = colorless
    
        other = total - (white + red + black + blue + green + colorless)
    
        
    
    
        for z in range(numTurns + 7):
        
            mana = [whitetemp / total, 
                    redtemp / total,
                    blacktemp / total,
                    bluetemp / total,
                    greentemp / total,
                    colorlesstemp / total,
                    other / total]
            
            temp = [""] * 100
            whiteProb = round(mana[0] * 100)
            redProb = round(mana[1] * 100)
            blackProb = round(mana[2] * 100)
            blueProb = round(mana[3] * 100)
            greenProb = round(mana[4] * 100)
            colorlessProb = round(mana[5] * 100)
            otherProb = round(mana[6] * 100)
            
            print(redProb + other)
           
            
            first = whiteProb
            second = whiteProb + redProb
            third = whiteProb + redProb + blackProb
            fourth = whiteProb + redProb + blackProb + blueProb
            fifth = whiteProb + redProb + blackProb + blueProb + greenProb
            sixth = whiteProb + redProb + blackProb + blueProb + greenProb + colorlessProb
            seventh = whiteProb + redProb + blackProb + blueProb + greenProb + colorlessProb + otherProb


            for y in range(0, first):
                temp[y] = "white"         
            for a in range(first, second):
                temp[a] = "red" 
            for b in range(second, third):
                temp[b] = "black"
            for c in range(third, fourth):
                temp[c] = "blue"
            for d in range(fourth, fifth):
                temp[d] = "green"
            for e in range(fifth, sixth):
                temp[e] = "colorless"
            for f in range(sixth, seventh):
                temp[f] = "other"
            
                
            index = random.randrange(0, 100, 1)
            
            if temp[index] == "white":
                AverageWhite += 1
                whitetemp -= 1
                total -= 1
            elif temp[index] == "red":
                AverageRed += 1
                redtemp -= 1
                total -= 1
            elif temp[index] == "black":
                AverageBlack += 1
                blacktemp -= 1
                total -= 1
            elif temp[index] == "blue":
                AverageBlue += 1
                bluetemp -= 1
                total -= 1
            elif temp[index] == "green":
                AverageGreen += 1
                greentemp -= 1
                total -= 1
            elif temp[index] == "colorless":
                AverageColorless += 1
                colorlesstemp -= 1
                total -= 1
            elif temp[index] == "other":
                other -= 1
                total -= 1
     
    
    
    
    
    
    
    
            
    AverageWhite /= 1000
    AverageRed /= 1000
    AverageBlack /= 1000
    AverageBlue /= 1000
    AverageGreen /= 1000
    AverageColorless /= 1000
    
    
    
    print("Your Average Number of Mountains avaliable in " + str(numTurns) + " turns is " + str(AverageRed))   
        
        
        
        
         
            
            
            

            
           
        


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', 
'24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', 
'89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']