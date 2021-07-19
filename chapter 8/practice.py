# IDiOTS LOOP
# import pyinputplus as pyip
# while True:
#     res = pyip.inputStr("Do you want to know how to make an indiot busy?\n")
#     if res == 'No':
#         break

# SANDWICH MAKER
import pyinputplus as pyip
print("Let's make a sandwich!!!\n")

breadType = pyip.inputMenu(['wheat','white','sourdough'], numbered=True)
meatType =  pyip.inputMenu(['chicken','turkey','ham','tofu'], numbered=True)
cheseOption = pyip.inputYesNo("Do you want chese?\n")
if cheseOption == "yes":
    cheseType = pyip.inputMenu(['cheddar','swiss','mozzarella'], numbered=True)
mayoOpton = pyip.inputYesNo("Do you want mayo, mustard, lectture or tomato? \n")
quantity = pyip.inputInt("How many sandwiches do you want? >>> ")
try:
    sumary = f'''
        You has {quantity} sandwich(es)\n
        Type of bread: {breadType}\n 
        Type of meat: {meatType}\n 
        Type of chese: {cheseType}\n 
        Has mayo? {mayoOpton}
    '''
except:
    sumary = f'''
        You has {quantity} sandwich(es)\n
        Type of bread: {breadType}\n 
        Type of meat: {meatType}\n 
        Has chese? {cheseOption}\n 
        Has mayo? {mayoOpton}
    '''

print(sumary)