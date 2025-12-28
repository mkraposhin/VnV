#!/usr/bin/python

import sys
import re

# total arguments
n = len(sys.argv)

if (n < 3):
    print ("Error")
    print ("Wrong number of arguments: ", n)
    sys.exit()

n_points = 2000
n_points_f= float(n_points)

input_num = sys.argv[1]
input_ref = sys.argv[2]

p_num = [0.0] * n_points
rho_num = [0.0] * n_points
alpha_num = [0.0] * n_points
U_num = [0.0] * n_points


# Open the file in read mode
with open(input_num, 'r') as file:
    # Read each line in the file
    i = -1
    for line in file:
        if (i == -1):
            i = i + 1
            continue
        vals_num = re.split('[,]', line)
        #print (i, vals_num[1])
        p_num[i] = float(vals_num[1])
        rho_num[i] = float(vals_num[2])
        alpha_num[i] = float(vals_num[3])
        U_num[i] = float(vals_num[4])
        # Print each line for debug
        #print (p_num[i], rho1_num[i], rho2_num[i], alpha_num[i], U_num[i])
        i = i + 1

p_err = [0.0] * n_points
rho_err = [0.0] * n_points
alpha_err = [0.0] * n_points
U_err = [0.0] * n_points

tot_p_err = 0.0
tot_rho_err = 0.0
tot_alpha_err = 0.0
tot_U_err = 0.0

c_rho = 0.0

# Open the file in read mode
with open(input_ref, 'r') as file:
    # Read each line in the file
    i = -1
    for line in file:
        if (i == -1):
            i = i + 1
            continue
        vals_ref = line.split()
        p_err[i] = float(vals_ref[1]) - p_num[i]
        rho_err[i] = float(vals_ref[2]) - rho_num[i]
        alpha_err[i] = float(vals_ref[3]) - alpha_num[i]
        U_err[i] = float(vals_ref[4]) - U_num[i]
        #print (vals_ref[1], vals_ref[2], vals_ref[3], vals_ref[4], vals_ref[5])
        #print (p_num[i], rho1_num[i], rho2_num[i], alpha_num[i], U_num[i])
        
        tot_p_err = tot_p_err + abs(p_err[i])
        tot_rho_err = tot_rho_err + abs(rho_err[i])
        tot_alpha_err = tot_alpha_err + abs(alpha_err[i])
        tot_U_err = tot_U_err + abs(U_err[i])
        i = i + 1

tot_p_err = tot_p_err / n_points_f
tot_rho_err = tot_rho_err / n_points_f
tot_alpha_err = tot_alpha_err / n_points_f
tot_U_err = tot_U_err / n_points_f

print(f"{tot_p_err:.6f} {tot_rho_err:.6f} {tot_alpha_err:.6f} {tot_U_err:.6f}")

#
#END-OF-FILE
#
