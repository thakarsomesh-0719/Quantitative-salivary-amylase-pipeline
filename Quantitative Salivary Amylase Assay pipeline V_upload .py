# Amylase activity and Reducing sugar calculator for Quantitative Salivary amylase assay based on temperature and pH
# Somesh Thakar
# March 2026
# Spectophotometric readings took with blank subtraction and under '540 nm'


import numpy as np
import matplotlib.pyplot as plt


def standard_assay_glucose(): # ---------- Function to create the standard curve of glucose for the assay ---------- 
    avg_absorbance_list = []
    concentrations = input("Please enter the different concentrations of glucose used for constructing the standard curve of glucose concentrations separated by commas =\n")
    concentration_list = [float(x) for x in concentrations.split(",") ]
    for conc in concentration_list:
        raw = input(f"Please enter the absorbance readings for the {conc} concentration of glucose separated by commas = ")
        readings = [float(x) for x in raw.split(",")]
        avg_absorbance_list.append(np.mean(readings))
    # ---------- Plotting the graph using matplotlib.pyplot ----------
    plt.plot(concentration_list,avg_absorbance_list, color = "red")
    plt.title("Concentration v/s absorbance graph with trendline")
    plt.xlabel("Concentration of glucose")
    plt.ylabel("Absorbance")
    # ---------- calculation of slope and intercepts of the graph using numpy ----------
    coefficents = np.polyfit(concentration_list, avg_absorbance_list, 1)
    trendline = np.poly1d(coefficents)
    plt.plot(concentration_list, trendline(concentration_list), color='blue', linestyle='--', label='Trendline')
    plt.legend()
    plt.show()
    print(f"Equation: y = {coefficents[0]:.2f}x + {coefficents[1]:.2f}")
    return coefficents


def amylase_activity_reducing_sugar_concentration(amylase_OD_average): # ---------- Function to calculate the reducing sugar concentration and amylase activity of the test solutions ---------- 
    global minutes_incubation
    global volume_enzyme
    global slope
    global intercept
    Reducing_sugar_concentration_mg_ml = (amylase_OD_average - intercept)/slope
    Reducing_sugar_concentration_micromol = (Reducing_sugar_concentration_mg_ml/180.16) * 1000
    amylase__activity = Reducing_sugar_concentration_micromol/(minutes_incubation*volume_enzyme)
    print(f"The concentration of Reducing sugar in the test solution is {Reducing_sugar_concentration_micromol:.5f} micro moles ")
    print(f"The amylase activity of the test solution is {amylase__activity:.5f} micromole per ml")


def amylase_od_avg(prompt): # ---------- Function to calculate average OD readings of the amylase test solutions ---------- 
    amylase_OD = input(prompt)
    amylase_OD_list = [float(x) for x in amylase_OD.split(",")]
    return np.mean(amylase_OD_list)

    # ---------- Main block ---------- 
standard_coefficients = standard_assay_glucose()
slope = (standard_coefficients[0])
intercept = (standard_coefficients[1])
while True:
    user_input = int(input("Please enter if any further assay performed ?\nPlease press 1 for yes \nPlease press 0 for no\n"))
    if user_input == 0: # ---------- No Further assay (User wants to exit the program) ---------- 
        break

    elif user_input == 1:
        user_input = int(input("Please enter any one of the following \nPlease press 1 for Temperature assay only \nPlease press 2 for pH assay only \nPlease press 3 for both the afformentioned assays \nPlease press 0 to exit \n"))
        minutes_incubation = int(input("Please enter the time (minutes) for which the samples were incubated for = "))
        volume_enzyme = float(input("Please enter the volume (ml) of enzyme used in this assay = "))
        if user_input == 1: # ---------- User requires calculations for only a temperature assay ---------- 
            parameter = input("Please enter the different temperatures used for this assay separated by commas = ")
            parameter_list = [int(x) for x in parameter.split(",")]
            for i in parameter_list:
                amylase_OD_average = amylase_od_avg(f"Please enter the OD reading of the samples kept at {i}°C separated by commas = ")
                amylase_activity_reducing_sugar_concentration(amylase_OD_average)
            break
        
        elif user_input == 2: # ---------- User requires calculations for only a pH assay ---------- 
            parameter = input("Please enter the different pH used for this assay separated by commas = ")
            parameter_list = [int(x) for x in parameter.split(",")]
            for i in parameter_list:
                amylase_OD_average = amylase_od_avg(f"Please enter the OD reading of the samples kept at pH {i} separated by commas = ")
                amylase_activity_reducing_sugar_concentration(amylase_OD_average)
            break

        elif user_input == 3: # ---------- User requires calculations for both temperature and pH based assays ---------- 
            parameter = input("Please enter the different temperatures used for this assay separated by commas = ")
            parameter_list = [int(x) for x in parameter.split(",")]
            for i in parameter_list:
                amylase_OD_average = amylase_od_avg(f"Please enter the OD reading of the samples kept at {i}°C separated by commas = ")
                amylase_activity_reducing_sugar_concentration(amylase_OD_average)     
            parameter = input("Please enter the different pH used for this assay separated by commas = ")
            parameter_list = [int(x) for x in parameter.split(",")]
            for i in parameter_list:
                amylase_OD_average = amylase_od_avg(f"Please enter the OD reading of the samples kept at pH {i} separated by commas = ")
                amylase_activity_reducing_sugar_concentration(amylase_OD_average)
            break
        elif user_input == 0: # ---------- No Further assay (User wants to exit the program) ---------- 
            break
        else:
            print("I didn't understand that, please try again")
    else:
        print("I didn't understand that, please try again")
