# Amylase activity and Reducing sugar calculator for Quantitative Salivary amylase assay based on temperature 
# Somesh Thakar
# March 2026
# Spectophotometric readings took with blank subtraction and under '540 nm'


import numpy as np
import matplotlib.pyplot as plt
def standard_assay_glucose():
    avg_absorbance_list = []
    concentrations = input('''Please enter the different concentrations of glucose used for constructing 
the standard curve of glucose concentrations separated by commas = ''')
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


def amylase_activity_reducing_sugar_concentration(slope,intercept):
    # ---------- Calculating the amylase activity for each temperature parameter ----------
    minutes_incubation = int(input("Please enter the time (minutes) for which the samples were incubated for = "))
    volume_enzyme = int(input("Please enter the volume (ml) of enzyme used in this assay = "))
    temperatures = input("Please enter the different temperatures used for this assay separated by commas = ")
    temperature_list = [int(x) for x in temperatures.split(",") ]
    for i in temperature_list:
        amylase_OD = input(f"Please enter the OD reading of the samples kept at {i}°C separated by commas = ")
        amylase_OD_list = [float(x) for x in amylase_OD.split(",")]
        amylase_OD_average = np.mean(amylase_OD_list)
        Reducing_sugar_concentration_mg_ml = (amylase_OD_average - intercept) / slope
        Reducing_sugar_concentration_micromol = (Reducing_sugar_concentration_mg_ml/180.16) * 1000
        amylase__activity = Reducing_sugar_concentration_micromol/(minutes_incubation*volume_enzyme)
        print(f"The concentration of Reducing sugar in the test solution is {Reducing_sugar_concentration_micromol:.5f} micro moles ")
        print(f"The amylase activity of the test solution is {amylase__activity:.5f} micromole per min per ml ")


standard_coefficients = standard_assay_glucose()
slope = (standard_coefficients[0])
intercept = (standard_coefficients[1])
while True:
    user_input_temp = input('''Please enter if the temperature assay was performed
Press 1 for Yes
Press 0 for No  ''')
    if user_input_temp == "1":
        amylase_activity_reducing_sugar_concentration(slope,intercept)
        print("Thank You")
        break
    elif user_input_temp == "0":
        print("Thank You")
        break
    else: 
        print("I didn't understand that, please try again")