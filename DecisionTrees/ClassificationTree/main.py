import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


cancer_df = pd.read_csv("breast-cancer.csv")

def calc_weighted_avg (imp1, imp2, imp1_multiplier, imp2_multiplier):
    
    return round(imp1_multiplier/(imp1_multiplier + imp2_multiplier) * imp2 + imp2_multiplier/(imp1_multiplier + imp2_multiplier) * imp1)



def calc_impurity(data):
    
    if len(np.unique(data[:,0])) > 2:
        
        sorted_data = data[data[:,0].argsort()]
        main_dict = {}

        for i in range(1,sorted_data):
            
            first_number = data[i-1,0]
            second_number = data[i,0]
            avg = (first_number + second_number) / 2

            true_xs = data[data[:,0] < avg]
            count_true_xs = len(true_xs)

            true_xs_true_ys = len(true_xs[true_xs[:,1] == True])
            true_xs_false_ys = len(true_xs[true_xs[:,1] == False])
            imp1 = round(1 - ((true_xs_true_ys / count_true_xs) ** 2) - ((true_xs_false_ys / count_true_xs) ** 2), 3)

            false_xs = data[data[:,0] > avg]
            count_false_xs = len(true_xs)

            false_xs_true_ys = len(false_xs[false_xs[:,1] == True])
            false_xs_false_ys = len(false_xs[false_xs[:,1] == False])
            imp2 = round(1 - ((false_xs_true_ys / count_false_xs) ** 2) - ((false_xs_false_ys / count_false_xs) ** 2), 3)



            
