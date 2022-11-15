import functions
import matplotlib.pyplot as plt
if __name__ == '__main__':
    functions.print_hi('Welcome to the financial Model ^-^ ')
    decision  = functions.UserDecision()
    if decision == '1':
        #call cmd functions

        print('We are working with cmd')
        Starting_machines,Number_of_Boxes_for_each_machine,Machine_Price,Box_Price,Box_cost,Scrapping_price,Max_years,Interest_Rate,Demand_Start,Increasing_Rate, adversting_per_box = functions.readCMD()
        n = int(input('enter the number of years:'))
        listRevenue = []
        listdemand = []
        list_of_dict = []
        listDict0 = {}
        listDict1 = {}
        listDict2 = {}
        listDict3 = {}
        listDict4 = {}
        listDict5 = {}
        listDict6 = {}
        listDict7 = {}
        listDict8 = {}
        listDict9 = {}
        listDict10 = {}
        cashflowIn = []
        cashflowOutL = []
        BoxSoldL = []
        RunMachinesL = []
        COGSList = []
        MachinepurL = []
        LastAdvsL = []
        for i in range(1, n+1):
            print('i', i)
            #listOfDict = functions.CreateDict()
            #listOfDict = functions.updateDictionary(i, listOfDict, )
            #year, listDict, revenue, demand, BoxSoldPerYear, CashIn, CashOut,
            # runningMachinces, BrokenMachines, ScappingValue, COGS, Machinespurchased, Advs
            #running_machines_per_year = functions.Run_machines_per_year(dict_purshed_machines, i, broken_per_year)
            #Number_of_Boxes_for_each_machine = Number_of_Boxes_for_each_machine
            if i == 1:
                demand = Demand_Start
                running_machines_per_year = Starting_machines
            else:
                print('')
                #call demand function
                #call running muchines

            #machines_purchased to be added to the list of dictionaries for its year
            machines_purchased = functions.machines_purchased_per_year(Starting_machines,demand, running_machines_per_year, Number_of_Boxes_for_each_machine)
            DictMachinespurchased = {}
            DictMachinespurchased = functions.CreateDictMachinespurchased(i, machines_purchased, DictMachinespurchased)
            #print('sdfdghj')
            print(DictMachinespurchased)
            #print('year',i)
            currentYear = i
            broken_per_year, scraping_value = functions.broken_machines_per_year(DictMachinespurchased, i)
            #print(broken_per_year)
            Run_machines_per_year = functions.Run_machines_per_year(DictMachinespurchased, i, broken_per_year)
            adversting_cash_all_years= []
            advsList = functions.adversting_cash_flow(Run_machines_per_year,Number_of_Boxes_for_each_machine,demand,Increasing_Rate, adversting_cash_all_years, adversting_per_box)#adversting_cash_all_years is a list of advertsing cashes
            LastYearAdvs = advsList[-1]
            demand = functions.demand(Increasing_Rate,demand,LastYearAdvs)
            boxes_sold_per_year = functions.boxes_sold_per_year(Run_machines_per_year, Number_of_Boxes_for_each_machine)
            revenue = boxes_sold_per_year*Box_Price#instead of using separated function
            COGS = boxes_sold_per_year*Box_cost
            Annual_Cash_Flow, Cash_In, Cash_Out = functions.Annual_Cash_Flow (revenue,COGS,scraping_value, machines_purchased, Machine_Price, LastYearAdvs)
            Net_Profit_Value = functions.Net_Profit_Value(Interest_Rate, Annual_Cash_Flow)

            #print(machines_purchased, adversting_cash_all_years, advsList, demand, boxes_sold_per_year, Annual_Cash_Flow, Net_Profit_Value)
            #print("***")

            #Dictionaries

            #list_of_dict = functions.CreateDict(list_of_dict,listDict1,listDict2,listDict3,listDict4,listDict5,listDict6,listDict7,listDict8,listDict9,listDict10,listDict11))
            #listOfDict = functions.updateDictionary(i, listOfDict,revenue, demand, boxes_sold_per_year,Cash_In, Cash_Out,Run_machines_per_year, broken_per_year, scraping_value, COGS,  machines_purchased,  LastYearAdvs, listDict1,listDict2,listDict3,listDict4,listDict5,listDict6,listDict7,listDict8,listDict9,listDict10,listDict11)
            listDict0['Year'+  str(i)] = revenue
            listRevenue.append(revenue)
            listdemand.append(demand)
            listDict1['Year'+  str(i)] = demand
            listDict2['Year'+  str(i)] = boxes_sold_per_year
            BoxSoldL.append(boxes_sold_per_year)
            listDict3['Year'+  str(i)] = Cash_In
            cashflowIn.append(Cash_In)
            listDict4['Year'+  str(i)] = Cash_Out
            cashflowOutL.append(Cash_Out)
            listDict5['Year'+  str(i)] = Run_machines_per_year
            RunMachinesL.append(Run_machines_per_year)
            listDict6['Year'+  str(i)] = broken_per_year
            listDict7['Year'+  str(i)] = scraping_value
            listDict8['Year'+  str(i)] = COGS
            COGSList.append(COGS)
            listDict9['Year'+  str(i)] = machines_purchased
            MachinepurL.append(machines_purchased)
            listDict10['Year'+  str(i)] = LastYearAdvs
            LastAdvsL.append(LastYearAdvs)
            list_of_dict = functions.updateDictionary(list_of_dict, listDict0, listDict1, listDict2, listDict3, listDict4, listDict5, listDict6, listDict7, listDict8, listDict9, listDict10)

            functions.Writexlsx('cashIn',Cash_In,i)
            #functions.Writexlsx('cashout',Cash_Out,i)
        year_axis = []
        for i in range(n):
            year_axis.append(i+1)
        print(year_axis)

        #demand Plot:
        functions.plotGraph(year_axis, listdemand, 'Demand')
        #Revenue Plot
        functions.plotGraph(year_axis, listRevenue, 'Revenue')
        functions.plotGraph(year_axis, COGSList, 'COGS')
        functions.plotGraph(year_axis, BoxSoldL, 'boxes sold per year')
        functions.plotGraph(year_axis, RunMachinesL, 'Run machines per year')
        functions.plotGraph(year_axis, MachinepurL, 'machines purchased')
        functions.plotGraph(year_axis, LastAdvsL, 'Year Advs')
        functions.plotGraph(year_axis, cashflowIn, 'cash flow In')
        functions.plotGraph(year_axis, cashflowOutL, 'cash flow Out')

    elif decision == '2':
        #call files functions
        print('We are working with csv or xlsx files')
        file = input('enter the file name')
        Starting_machines,Number_of_Boxes_for_each_machine,Machine_Price,Box_Price,Box_cost,Scrapping_price,Max_years,Interest_Rate,Demand_Start,Increasing_Rate, adversting_per_box  = functions.readCSV(file)
        n = int(input('enter the number of years:'))
        listRevenue = []
        listdemand = []
        list_of_dict = []
        listDict0 = {}
        listDict1 = {}
        listDict2 = {}
        listDict3 = {}
        listDict4 = {}
        listDict5 = {}
        listDict6 = {}
        listDict7 = {}
        listDict8 = {}
        listDict9 = {}
        listDict10 = {}
        cashflowIn = []
        cashflowOutL = []
        BoxSoldL = []
        RunMachinesL = []
        COGSList = []
        MachinepurL = []
        LastAdvsL = []
        for i in range(1, n+1):
            print('i', i)
            #listOfDict = functions.CreateDict()
            #listOfDict = functions.updateDictionary(i, listOfDict, )
            #year, listDict, revenue, demand, BoxSoldPerYear, CashIn, CashOut,
            # runningMachinces, BrokenMachines, ScappingValue, COGS, Machinespurchased, Advs
            #running_machines_per_year = functions.Run_machines_per_year(dict_purshed_machines, i, broken_per_year)
            #Number_of_Boxes_for_each_machine = Number_of_Boxes_for_each_machine
            if i == 1:
                demand = Demand_Start
                running_machines_per_year = Starting_machines
            else:
                print('')
                #call demand function
                #call running muchines

            #machines_purchased to be added to the list of dictionaries for its year
            machines_purchased = functions.machines_purchased_per_year(Starting_machines,demand, running_machines_per_year, Number_of_Boxes_for_each_machine)
            DictMachinespurchased = {}
            DictMachinespurchased = functions.CreateDictMachinespurchased(i, machines_purchased, DictMachinespurchased)
            #print('sdfdghj')
            print(DictMachinespurchased)
            #print('year',i)
            currentYear = i
            broken_per_year, scraping_value = functions.broken_machines_per_year(DictMachinespurchased, i)
            #print(broken_per_year)
            Run_machines_per_year = functions.Run_machines_per_year(DictMachinespurchased, i, broken_per_year)
            adversting_cash_all_years= []
            advsList = functions.adversting_cash_flow(Run_machines_per_year,Number_of_Boxes_for_each_machine,demand,Increasing_Rate, adversting_cash_all_years, adversting_per_box)#adversting_cash_all_years is a list of advertsing cashes
            LastYearAdvs = advsList[-1]
            demand = functions.demand(Increasing_Rate,demand,LastYearAdvs)
            boxes_sold_per_year = functions.boxes_sold_per_year(Run_machines_per_year, Number_of_Boxes_for_each_machine)
            revenue = boxes_sold_per_year*Box_Price#instead of using separated function
            COGS = boxes_sold_per_year*Box_cost
            Annual_Cash_Flow, Cash_In, Cash_Out = functions.Annual_Cash_Flow (revenue,COGS,scraping_value, machines_purchased, Machine_Price, LastYearAdvs)
            Net_Profit_Value = functions.Net_Profit_Value(Interest_Rate, Annual_Cash_Flow)

            #print(machines_purchased, adversting_cash_all_years, advsList, demand, boxes_sold_per_year, Annual_Cash_Flow, Net_Profit_Value)
            #print("***")

            #Dictionaries

            #list_of_dict = functions.CreateDict(list_of_dict,listDict1,listDict2,listDict3,listDict4,listDict5,listDict6,listDict7,listDict8,listDict9,listDict10,listDict11))
            #listOfDict = functions.updateDictionary(i, listOfDict,revenue, demand, boxes_sold_per_year,Cash_In, Cash_Out,Run_machines_per_year, broken_per_year, scraping_value, COGS,  machines_purchased,  LastYearAdvs, listDict1,listDict2,listDict3,listDict4,listDict5,listDict6,listDict7,listDict8,listDict9,listDict10,listDict11)
            listDict0['Year'+  str(i)] = revenue
            listRevenue.append(revenue)
            listdemand.append(demand)
            listDict1['Year'+  str(i)] = demand
            listDict2['Year'+  str(i)] = boxes_sold_per_year
            BoxSoldL.append(boxes_sold_per_year)
            listDict3['Year'+  str(i)] = Cash_In
            cashflowIn.append(Cash_In)
            listDict4['Year'+  str(i)] = Cash_Out
            cashflowOutL.append(Cash_Out)
            listDict5['Year'+  str(i)] = Run_machines_per_year
            RunMachinesL.append(Run_machines_per_year)
            listDict6['Year'+  str(i)] = broken_per_year
            listDict7['Year'+  str(i)] = scraping_value
            listDict8['Year'+  str(i)] = COGS
            COGSList.append(COGS)
            listDict9['Year'+  str(i)] = machines_purchased
            MachinepurL.append(machines_purchased)
            listDict10['Year'+  str(i)] = LastYearAdvs
            LastAdvsL.append(LastYearAdvs)
            list_of_dict = functions.updateDictionary(list_of_dict, listDict0, listDict1, listDict2, listDict3, listDict4, listDict5, listDict6, listDict7, listDict8, listDict9, listDict10)

            functions.Writexlsx('cashIn',Cash_In,i)
            #functions.Writexlsx('cashout',Cash_Out,i)
        year_axis = []
        for i in range(n):
            year_axis.append(i+1)
        print(year_axis)

        #demand Plot:
        functions.plotGraph(year_axis, listdemand, 'Demand')
        #Revenue Plot
        functions.plotGraph(year_axis, listRevenue, 'Revenue')
        functions.plotGraph(year_axis, COGSList, 'COGS')
        functions.plotGraph(year_axis, BoxSoldL, 'boxes sold per year')
        functions.plotGraph(year_axis, RunMachinesL, 'Run machines per year')
        functions.plotGraph(year_axis, MachinepurL, 'machines purchased')
        functions.plotGraph(year_axis, LastAdvsL, 'Year Advs')
        functions.plotGraph(year_axis, cashflowIn, 'cash flow In')
        functions.plotGraph(year_axis, cashflowOutL, 'cash flow Out')

    elif decision == '3':
        functions.GUI()
