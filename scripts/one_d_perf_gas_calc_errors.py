#!/usr/bin/python

import sys
import re

# total arguments
n = len(sys.argv)

if (n < 3):
    print ("Error")
    print ("Wrong number of arguments: ", n)
    sys.exit()

Cv = 1.0
input_num = sys.argv[1]
input_ref = sys.argv[2]

rho_num = [0.0] * 800
U_num = [0.0] * 800
p_num = [0.0] * 800
e_num = [0.0] * 800

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
        e_num[i] = float(vals_num[1]) * Cv
        p_num[i] = float(vals_num[2])
        rho_num[i] = float(vals_num[3])
        U_num[i] = float(vals_num[4])
        # Print each line
        i = i + 1

rho_err = [0.0] * 800
U_err = [0.0] * 800
p_err = [0.0] * 800
e_err = [0.0] * 800

tot_rho_err = 0.0
tot_U_err = 0.0
tot_p_err = 0.0
tot_e_err = 0.0

# Open the file in read mode
with open(input_ref, 'r') as file:
    # Read each line in the file
    i = -1
    for line in file:
        if (i == -1):
            i = i + 1
            continue
        vals_ref = line.split()
        rho_err[i] = float(vals_ref[1]) - rho_num[i]
        U_err[i] = float(vals_ref[2]) - U_num[i]
        p_err[i] = float(vals_ref[3]) - p_num[i]
        e_err[i] = float(vals_ref[4]) - e_num[i]
        tot_rho_err = tot_rho_err + abs(rho_err[i])
        tot_U_err = tot_U_err + abs(U_err[i])
        tot_p_err = tot_p_err + abs(p_err[i])
        tot_e_err = tot_e_err + abs(e_err[i])
        i = i + 1


tot_rho_err = tot_rho_err / 800.0
tot_U_err = tot_U_err / 800.0
tot_p_err = tot_p_err / 800.0
tot_e_err = tot_e_err / 800.0

print (tot_rho_err, tot_U_err, tot_p_err, tot_e_err)

#
#END-OF-FILE
#
