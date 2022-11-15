import pandas as pd
import xlsxwriter
import csv
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import messagebox
import os

#Abdullah Kamal functions:
def print_hi(name):
    print(f'Hi, {name}')

def UserDecision(): # to get the choice form the user to use cmd or csv files
  decision = int(input('Enter 1 to work with cmd, and  2 to work with csv and xlsx file: '))
  while decision != 1 and decision != 2 and decision != 3:# to enforce the user to only two choices
    # to take the user choice
    decision = int(input('Error! please enter 1 to work with cmd, and  2 to work with csv and xlsx file: '))
  if decision == 1: # to use cmd flow
    return '1'
  elif decision == 2: # to use files flow
    return '2'
  else:
    return '3'

def readCSV(file): # function that reads the inputs form a csv file
  # to take the file name from the user
  #pd.read_excel('sample.xlsx')
  df = pd.read_csv(file)
  df.columns = ['Inputs', 'Values']
  # assigning the header names
  #mapping the values from the user to local variables to be returned
  Starting_machines = df['Values'][0]
  Number_of_Boxes_for_each_machine = df['Values'][1]
  Machine_Price = df['Values'][2]
  Box_Price = df['Values'][3]
  Box_cost = df['Values'][4]
  Scrapping_price = df['Values'][5]
  Max_years = int(df['Values'][6])
  Interest_Rate = df['Values'][7]
  Demand_Start = df['Values'][8]
  Increasing_Rate = df['Values'][9]
  adversting_per_box = df['Values'][10]
  #Max_years = int(df['Values'][11])
  # to return the inputs after the file was read
  return Starting_machines, Number_of_Boxes_for_each_machine, Machine_Price, Box_Price, Box_cost, Scrapping_price, Max_years,Interest_Rate, Demand_Start,Increasing_Rate, adversting_per_box


def readCMD():
  # to read the needed inputs from the user by using cmd
  Starting_machines = int(input('Enter number of  Starting machines - int - : '))
  Number_of_Boxes_for_each_machine = int(input('Enter number of Boxes for each machine - int -: '))
  Machine_Price = float(input('Enter Machine Price - int - : '))
  Box_Price = float(input('Enter Box Price - int- : '))
  Box_cost = float(input('Enter Box cost - int - : '))
  Scrapping_price = float(input('Enter Scrapping price - int - : '))
  Max_years = int(input('Enter Max years - int - :'))
  Interest_Rate = float(input('Enter Interest Rate - float - : '))
  Demand_Start = int(input('Enter Demand Start - int - : '))
  Increasing_Rate = float(input('Enter Increasing Rate - float - : '))
  adversting_per_box = int(input('Enter adversting_per_box - int - : '))
  # to return the vlues to be avilable within the main flow
  return Starting_machines, Number_of_Boxes_for_each_machine, Machine_Price, Box_Price, Box_cost, Scrapping_price, Max_years,Interest_Rate, Demand_Start,Increasing_Rate, adversting_per_box

def plotGraph(yearAxis, targetList, targetName):
    plt.xlabel('years - axis')
    # naming the y axis
    plt.ylabel(targetName + ' axis')
    # giving a title to my graph
    plt.title(targetName)
    plt.plot(yearAxis, targetList)
    plt.show()


def WriteCMD(cashflow, npv):
  # to print the results of the cash flow and the npv values to the cmd
  print('Results of cash flow and NPV !!')
  print('Cash Flow =', cashflow)
  print('%-11s' %'NPV=','%-8d' %npv )

#def WriteCSV(filename, cashflowlist):
#    f = open(filename+'.csv', 'w')
#    writee = csv.writer(f)
#    #write.writerow(Details)
#    writee.writerows(cashflowlist)

def Writexlsx(filename, cashflow, year):
  # to write the results to a xlsx file
  #DictOfOutputs = dict({'Cash Flow': [cashflow], 'NPV': [npv]})
  #outputCSV = pd.DataFrame(DictOfOutputs)
  #outputCSV.to_csv('out.csv')
  #myWorkbook = xlsxwriter.Workbook(filename+str(year)+'.xlsx')
  myWorkbook = xlsxwriter.Workbook(filename+str(year)+'.xlsx')
  # the name file is assigned to be out.xlsx
  Results = myWorkbook.add_worksheet()
  # an array of the cash flow values if there are many values
  #Cash_Flow = [cashflow]
  # an array of the npv  values if there are many values
  #NPV = [npv]
  # naming the header specialy the first colums of the file to be 'Cash Flow'
  Results.write("A1", "Cash Flow")
  # naming the header specialy the 2nd colums of the file to be 'NPV Flow'
  Results.write("B1", "year")
  Results.write(1, 0, cashflow)# assining the first value to the 1st row and the second column
  Results.write(1, 1, year)# assining the first value to the 2nd row and the 2nd column
  myWorkbook.close()
  print('Results have been written in file "out.xlsx"!!')


def Revenue(boxes_sold_per_year, Box_price):
  return boxes_sold_per_year * Box_price
    #list_of_dict,listDict1,listDict2,listDict3,listDict4,list
#def CreateDict((Dict5,listDict6,listDict7,listDict8,listDict9,listDict10,listDict11)): # to create a list of dictionaries that we need to track there values

 # list_of_dict.append(listDict1, listDict2,listDict3,listDict4,listDict5,listDict6,listDict7,listDict8, listDict9, listDict10, listDict11)


  #dictionaries are: 1- RevenueDict, 2- DemandDict, 3-BoxSoldPerYearDict, 4- CashInDict, 5- CashOutDict, 6- runningMachincesDict
  # and also 7- BrokenMachinesDict, 8- ScappingValueDict, 9- COGSDict, 10-Machinespurchased ,11- Advs
#for i in range(11):
#  dictionary = {'Dict': None}
#  dictionary['Dict'] = i+1
#  list_of_dict.append(dictionary)
#return list_of_dict

def CreateDictMachinespurchased(year, NumberMachinespurchased, DictMachinespurchased):
    print('year', year)
    DictMachinespurchased['year'+str(year)] = NumberMachinespurchased
    return DictMachinespurchased

# to add the new values to corresponding dictionaries with each year and return the same list of dict with the updated values
def updateDictionary(list_of_dict, listDict0, listDict1, listDict2, listDict3, listDict4, listDict5, listDict6, listDict7, listDict8, listDict9, listDict10):
   list_of_dict.append(listDict0)
   list_of_dict.append(listDict1)
   list_of_dict.append(listDict2)
   list_of_dict.append(listDict3)
   list_of_dict.append(listDict4)
   list_of_dict.append(listDict5)
   list_of_dict.append(listDict6)
   list_of_dict.append(listDict7)
   list_of_dict.append(listDict8)
   list_of_dict.append(listDict9)
   list_of_dict.append(listDict10)
   return list_of_dict


def broken_machines_per_year(dict_purcheced, year):
  #a function that return the added macines that was broken
  broken_per_year = 0
  #print(len(dict_purcheced))
  for i in range(len(dict_purcheced)):
    broken_per_year = 0
    if year - i == 10:
    #if len(dict_purcheced[i:]) == 10:
      print(dict_purcheced)
      broken_per_year = broken_per_year + dict_purcheced['year '+str(i)]
  scraping_value =  broken_per_year * 100000
  # scraping_value is the value of selling the borken machines, broken_per_year is the number of broken machines till now!
  #Within the fist 10 years, there is no broken machines
  # instead of reducing its price, we know that each machine can not work with th 10th year of its buying
  return broken_per_year, scraping_value





def boxes_sold_per_year(running, produced):
    b = running * produced
    # produced is the boxes per machines, running is the running machines
    return b

def GUI():
    window = tk.Tk()
    inputs= []

    def getinputs():
        file = filedialog.askopenfile()
        inputs.append(file)
        #print(file.find('Inputs.csv'))
        for put in inputs:
            get =tk.Label(frame, text=put, bg='gray')
            get.pack()

    def start():
        a = tk.Label(frame, text='Hi, Welcome to the financial model', bg='gray')
        a.pack()

    frame = tk.Frame(window, height=200, width=200, bg='white')
    frame.pack()

    star = tk.Button(window, text='star the program', padx=10, pady=6, fg='black', command= start)
    star.pack()

    get_inputs = tk.Button(window, text='Get inputs from the User', padx=10, pady=6, fg='black', command= getinputs )
    get_inputs.pack()

    text = tk.Text(window, padx=5, pady=3)
    text.pack()

    window.mainloop()
    exit()

def cash_in(rev, scraping):
    c = rev + scraping
    return c


def Run_machines_per_year(dict_purshed_machines, year, broken_per_year):
    #run = pur - broken
    num_of_running_machines = 0
    for i in range(len(dict_purshed_machines)):
        #print(dict_purshed_machines['year'+str(year)])
        num_of_running_machines = num_of_running_machines + dict_purshed_machines['year'+str(year)]
    return num_of_running_machines-broken_per_year


def Annual_Cash_Flow (Revnues,COGS,Scrap_Value, machines_purchased, Machine_Price, LastYearAdvs):
    # Revnues= 1000000
    # COGS= 500000
    # Scrap_Value= 40000
    # Machine_Bought_Cash= 200000
    Cash_In= (Revnues+Scrap_Value)
    Machine_Bought_Cash = machines_purchased*Machine_Price
    Cash_Out= (COGS+Machine_Bought_Cash+LastYearAdvs)
    Annual_Cash_Flow= (Cash_In-Cash_Out)
    return Annual_Cash_Flow, Cash_In, Cash_Out


def Net_Profit_Value(Interst_Rate, ACF):
    NPV= Interst_Rate*ACF
    return NPV


def demand(Increasing_Rate,previous_demand,adversting_cash_per_year):
    demand= (previous_demand*(1+Increasing_Rate))+adversting_cash_per_year #This is the advserting for the current year (Current iteration)
    return demand

def machines_purchased_per_year(Starting_machines,demand, running_machines_per_year, number_of_box_per_each_machine):
    machines_purchased=Starting_machines
    import math
    if demand > running_machines_per_year*number_of_box_per_each_machine: #d= 660K running =500K B=2
        machines_purchased = math.ceil((demand - (running_machines_per_year*number_of_box_per_each_machine))/number_of_box_per_each_machine)
    return machines_purchased

def adversting_cash_flow(running_machines_per_year,number_of_box_per_each_machine,demand,Increasing_Rate, adversting_cash_all_years, adversting_per_box):#adversting_cash_all_years is a list of advertsing cashes

    adversting_boxes= (running_machines_per_year*number_of_box_per_each_machine) - (demand*Increasing_Rate)
    adversting_cash= adversting_boxes * adversting_per_box #advertsing cost for each box
    if adversting_cash > 0:
        adversting_cash_all_years.append(adversting_cash)
    else:
        adversting_cash_all_years.append(0)
    # We should perform a for loop in the main function to take all years instances
    return adversting_cash_all_years
