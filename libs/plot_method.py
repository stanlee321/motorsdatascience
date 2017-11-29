#from libs import clean_data
from parsing_data import machine
import matplotlib.pyplot as plt
import os
import numpy as np
plt.style.use('ggplot')

cwd = os.getcwd()           # Original Path to libs
original_path = cwd
print('ORIGINAL PATH', original_path)


machi = 'PALETIZADORA'

currents_MACHINE_2015, currents_MACHINE_2016, currents_MACHINE_2017,\
aviable_2017_months, aviable_2017_months_as_number, \
aviable_2016_months, aviable_2016_months_as_number, \
aviable_2015_months, aviable_2015_months_as_number,\
aviable_2017_motors,aviable_2016_motors,aviable_2015_motors  = machine(machi)

#print(currents_MACHINE_2016['M1'][0])
#print(currents_MACHINE_2015['M1'][1])
#print(currents_MACHINE_2017['M1'][2])
#print(currents_MACHINE_2017['M1'][3])





def plot_motor(machine, motor, current_MACHINE_YEAR_1, current_MACHINE_YEAR_2,current_MACHINE_YEAR_3, aviable_YEAR_months, aviable_YEAR_months_as_number,\
              aviable_YEAR_months_2, aviable_YEAR_months_as_number_2,aviable_YEAR_months_3, aviable_YEAR_months_as_number_3, kind):
    
    
    path_to_save = original_path +'\outputs\images'
    #path_to_save = 'D:\\Mis documentos T Electrico\\Python Scripts\\Cleaning_currents\\corrientes_linea_servicio\\WASHER_2015_2016_WITHOUT\\'

        
    L1_2016 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_1[motor][0] ]
    L2_2016 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_1[motor][1] ]
    L3_2016 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_1[motor][2] ]
    
    
    L1_2015 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_2[motor][0] ]
    L2_2015 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_2[motor][1] ]
    L3_2015 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_2[motor][2] ]
    if kind == 1 : # NOrmal plot
        plt.figure(figsize=(20,10))
        plt.plot(aviable_YEAR_months_as_number, current_MACHINE_YEAR_1[motor][3],'-',linestyle='solid', color='0.20', label='Nominal:  %s' %current_MACHINE_YEAR_1[motor][3])

    
        plt.xticks(aviable_YEAR_months_as_number, aviable_YEAR_months)

        plt.plot(aviable_YEAR_months_as_number, current_MACHINE_YEAR_1[motor][0],'-', color='red', label='L1: %s' %L1_2016)
        plt.plot(aviable_YEAR_months_as_number, current_MACHINE_YEAR_1[motor][1],'-', color='b', label='L2:  %s' %L2_2016)
        plt.plot(aviable_YEAR_months_as_number, current_MACHINE_YEAR_1[motor][2],'-', color='g', label='L3: %s' %L3_2016)
    
        plt.legend()
    
        plt.axes().set(xlim=(1,12),label='Months', ylabel='currents [A]',title='A Simple Plot %s'%motor+' -- '+str(current_MACHINE_YEAR_1[motor][4][-1]))
        plt.savefig(path_to_save+'WASHER_%s.jpg' %motor)
    
    if kind ==2: # Convined plot
        plt.figure(figsize=(20,10))
        plt.plot(aviable_YEAR_months_as_number, current_MACHINE_YEAR_1[motor][3],'-',linestyle='solid', color='0.20', label='Nominal:  %s' %current_MACHINE_YEAR_1[motor][3])


        plt.xticks(aviable_YEAR_months_as_number, aviable_YEAR_months)

        plt.plot(aviable_YEAR_months_as_number, current_MACHINE_YEAR_1[motor][0],'-', color='red', label='L1: %s' %L1_2016)
        plt.plot(aviable_YEAR_months_as_number, current_MACHINE_YEAR_1[motor][1],'-', color='b', label='L2:  %s' %L2_2016)
        plt.plot(aviable_YEAR_months_as_number, current_MACHINE_YEAR_1[motor][2],'-', color='g', label='L3: %s' %L3_2016)
    
        plt.plot(aviable_YEAR_months_as_number_2, current_MACHINE_YEAR_2[motor][0],'--',color='red', label='L1: %s' %L1_2015+ 'From 2015')
        plt.plot(aviable_YEAR_months_as_number_2, current_MACHINE_YEAR_2[motor][1],'--',color='b', label='L2:  %s' %L2_2015+ 'From 2015')
        plt.plot(aviable_YEAR_months_as_number_2, current_MACHINE_YEAR_2[motor][2],'--',color='g',label='L3: %s' %L3_2015+ 'From 2015')
        
        plt.legend()
    
        plt.axes().set(xlim=(1,12),label='Months', ylabel='currents [A]',title='A Simple Plot %s'%motor+' -- '+str(current_MACHINE_YEAR_1[motor][4][-1]))
        plt.savefig(path_to_save+'WASHER_%s.jpg' %motor)
    
    
    if kind ==3: # Line Chart
        
        years_as_months = {1:'ENE 2015',2:'FEB 2015',3:'MAR 2015',4:'ABR 2015',5:'MAY 2015',6:'JUN 2015',7:'JUL 2015',8:'AUG 2015',9:'SEP 2015',10:'OCT 2015',11:'NOV 2015',12:'DIC 2015',\
             13:'ENE 2016',14:'FEB 2016',15:'MAR 2016',16:'ABR 2016',17:'MAY 2016',18:'JUN 2016',19:'JUL 2016',20:'AUG 2016',21:'SEP 2016',22:'OCT 2016',23:'NOV 2016',24:'DIC 2016',\
             25:'ENE 2017',26:'FEB 2017', 27:'MAR 2017', 28:'ABR 2017',29:'MAY 2017'}
        
        L1_2017 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_3[motor][0] ]
        L2_2017 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_3[motor][1] ]
        L3_2017 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_3[motor][2] ]

        
        
        L1_2016 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_1[motor][0] ]
        L2_2016 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_1[motor][1] ]
        L3_2016 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_1[motor][2] ]


        L1_2015 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_2[motor][0] ]
        L2_2015 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_2[motor][1] ]
        L3_2015 = ["{0:.2f}".format(round(value,2)) for value in current_MACHINE_YEAR_2[motor][2] ]

        L1 = L1_2015 + L1_2016 + L1_2017
        L2 = L2_2015 + L2_2016 + L2_2017
        L3 = L3_2015 + L3_2016 + L3_2017
        
        
        plt.figure(figsize=(25,10))
        
        
      
    
        l1 = aviable_YEAR_months_as_number
        l2 = aviable_YEAR_months_as_number_2
        l3 = aviable_YEAR_months_as_number_3
        
        l4 = l2 +[value + 12 for value in l1] + [value +24 for value in l3]
        
        n = ["{0:.2f}".format(round(float(value),2)) for value in (current_MACHINE_YEAR_1[motor][3])]+\
        ["{0:.2f}".format(round(float(value),2)) for value in (current_MACHINE_YEAR_2[motor][3])]+\
        ["{0:.2f}".format(round(float(value),2)) for value in (current_MACHINE_YEAR_3[motor][3])]
        print(n)
        def get_aviable_months_L(month_data):
            aviable_months_name = []
            aviable_months_number = []

            for keys in years_as_months.keys():
                if keys in month_data:
                    aviable_months_name.append(years_as_months[keys])
                    aviable_months_number.append(keys)
            aviable_months_number = sorted(aviable_months_number, key=int)
            return aviable_months_name, aviable_months_number

        months_name,months_name_number = get_aviable_months_L(l4)
        plt.xticks(months_name_number, months_name)
        
        plt.plot( months_name_number, n,'-',linestyle='solid', color='0.20', label='Nominal:  %s' %n)

        plt.plot( months_name_number,L1,'-', color='red', label='L1: %s' %L1)
        plt.plot( months_name_number,L2,'-', color='b', label='L2:  %s' %L2)
        plt.plot( months_name_number,L3,'-', color='g', label='L3: %s' %L3)
    
               
        plt.legend(loc = 9, fancybox = True, shadow = True)
    
        plt.axes().set(xlim=(1,28),label='Months', ylabel='currents [A]',title='A Simple Plot %s'%motor+' -- '+str(current_MACHINE_YEAR_1[motor][4][-1]))
        plt.savefig(path_to_save +"\_"+ machi +'_%s.jpg' %motor)

#PLOTING the WASHER!!
"""
for motor in aviable_2016_motors:
    try:
        plot_motor(machine,motor,currents_MACHINE_2016, currents_MACHINE_2015,currents_MACHINE_2017,\
                   aviable_2016_months, aviable_2016_months_as_number,\
                   aviable_2015_months, aviable_2015_months_as_number,\
                   aviable_2017_months, aviable_2017_months_as_number, kind = 3)
    except Exception as e:
        print("I can't this motor " +str(motor) + ' by this:', e)
"""
