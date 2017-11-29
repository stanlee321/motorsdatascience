# read python dict back from the file
import os
import pickle
#from  libs.path_file import get_path_to_files
#get_path_to_files
cwd = os.getcwd()           # Original Path to libs

#cwd = os.system()
original_path = cwd
print('ORIGINAL PATH', original_path)



path = original_path + '\outputs'

pkl_file_17 = open(path+ '\data_2017.pkl', 'rb')
pkl_file_16 = open(path+ '\data_2016.pkl', 'rb')
pkl_file_15 = open(path+ '\data_2015.pkl', 'rb')

year_2017 = pickle.load(pkl_file_17)
year_2016 = pickle.load(pkl_file_16)
year_2015 = pickle.load(pkl_file_15)


pkl_file_17.close()
pkl_file_16.close()
pkl_file_15.close()

pklmonth_data_2017 = open(path+'\month_data_dict_2017.pkl', 'rb')
pklmonth_data_2016 = open(path+'\month_data_dict_2016.pkl', 'rb')
pklmonth_data_2015 = open(path+'\month_data_dict_2015.pkl', 'rb')

month_data_2017 = pickle.load(pklmonth_data_2017)
month_data_2016 = pickle.load(pklmonth_data_2016)
month_data_2015 = pickle.load(pklmonth_data_2015)

pklmonth_data_2017.close()
pklmonth_data_2016.close()
pklmonth_data_2015.close()


#print(year_2015['OCT']['WASHER'])

def get_aviable_months(month_data):
    aviable_months_name = []
    aviable_months_number = []
    month_dict = {1:'ENE',2:'FEB',3:'MAR',4:'ABR',5:'MAY',6:'JUN',7:'JUL',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DIC'}
    for keys in month_data.keys():
        if keys in month_dict.keys():
            aviable_months_name.append(month_dict[keys])
            aviable_months_number.append(keys)
    aviable_months_number = sorted(aviable_months_number, key=int)
    return aviable_months_name, aviable_months_number


aviable_2017_months, aviable_2017_months_as_number = get_aviable_months(month_data_2017)
print(aviable_2017_months)
print(aviable_2017_months_as_number)

aviable_2016_months, aviable_2016_months_as_number = get_aviable_months(month_data_2016)
print(aviable_2016_months)
print(aviable_2016_months_as_number)

aviable_2015_months, aviable_2015_months_as_number = get_aviable_months(month_data_2015)
print(aviable_2015_months)
print(aviable_2015_months_as_number)

#print(year_2016['MAR']['WASHER']['Motor'])





 ## MACHINE PART
def machine(machine):
	global year_2017, year_2016, year_2015,\
			month_data_2017, month_data_2016, month_data_2015, \
			aviable_2017_months, aviable_2017_months_as_number, \
			aviable_2016_months, aviable_2016_months_as_number, \
			aviable_2015_months, aviable_2015_months_as_number

	def machine_to_work(machine, year_data, aviable_YEAR_months):
	    # FUNCTION TO CLEAR THE VOID SPACES IN THE DATA WITH i.e Nominal values, descriptions and so on.
	    try:
	        for month in aviable_YEAR_months:
	            for index, value in enumerate(year_data[month][machine]['Nominal_current']):
	                if value == 0.0:

	                    year_data[month][machine]['Nominal_current'][index] = year_data[month][machine]['Nominal_current'][index-1]

	                else:
	                    pass
	    except Exception as e:
	        print("this: ", e)

	    try:
	        for month in aviable_YEAR_months:
	            for index, value in enumerate(year_data[month][machine]['Description']):
	                if value == 0.0:

	                    year_data[month][machine]['Description'][index] = year_data[month][machine]['Description'][index-1]

	                else:
	                    pass
	    except Exception as e:
	        print('this one: ', e)
	machine_to_work(machine, year_2016, aviable_2016_months)
	machine_to_work(machine, year_2015, aviable_2015_months)
	machine_to_work(machine, year_2017, aviable_2017_months)



	# 2017 Motors
	aviable_2017_motors = year_2017['MAR'][machine]['Motor']        # Geting all the aviable MOTORS TO WORK ON WASHER
	print(aviable_2017_motors)


	# 2016 Motors
	aviable_2016_motors = year_2016['MAR'][machine]['Motor']        # Geting all the aviable MOTORS TO WORK ON WASHER
	print(aviable_2016_motors)

	
	# 2015 Motors
	aviable_2015_motors = year_2015['MAR'][machine]['Motor']        # Geting all the aviable MOTORS TO WORK ON WASHER
	print(aviable_2015_motors)


	# Function to create a currents tuple from the index that we provide him
	# index represent motor
	def get_current(index, year_201X, aviable_YEAR_months):
	    L1 = []
	    L2 = []
	    L3 = []
	    N = []
	    place = []
	    descrip = []
	    for month in aviable_YEAR_months:
	        L1.append(year_201X[month][machine]['L1'].at[index])
	        L2.append(year_201X[month][machine]['L2'].at[index])
	        L3.append(year_201X[month][machine]['L3'].at[index])
	        N.append(year_201X[month][machine]['Nominal_current'].at[index])
	        place.append(year_201X[month][machine]['Place'].at[index])
	        descrip.append(year_201X[month][machine]['Description'].at[index])
	        
	    return(L1,L2,L3,N,place,descrip)

	# Create the dictionary where we can get the currents from every motor throught the aviable
	# months, the format is as follow currents_conveyor (in this case) currents_conveyor['Motor'][0,1,2] +
	# where 0,1,2 represent the lines l1,l2,l3.

	def create_currents_dict(start, year_201X, aviable_YEAR_months, aviable_YEAR_motors):
	    currents_MACHINE = {}
	    index = start
	    
	    for motor in range(len(year_201X['MAR'][machine]['L1'])):
	        currents = get_current(index, year_201X, aviable_YEAR_months)
	        for month in aviable_YEAR_months:
	            currents_MACHINE[year_201X[month][machine]['Motor'][motor]] = currents
	        
	        index = index + 1
	    for motor in aviable_YEAR_motors:
	        for value in range(len(currents_MACHINE[motor][3])):
	            currents_MACHINE[motor][3][value] = str(currents_MACHINE[motor][3][value]).replace(' Amp.','').replace(' Amp,','').replace('Amp','').replace('3,5A','3.5')
	    return(currents_MACHINE)


	currents_MACHINE_2017 = create_currents_dict(0, year_2017, aviable_2017_months, aviable_2017_motors)

	currents_MACHINE_2016 = create_currents_dict(0, year_2016, aviable_2016_months, aviable_2016_motors)

	currents_MACHINE_2015 = create_currents_dict(0, year_2015, aviable_2015_months, aviable_2015_motors)

	return( currents_MACHINE_2015, currents_MACHINE_2016, currents_MACHINE_2017,\
			aviable_2017_months, aviable_2017_months_as_number, \
			aviable_2016_months, aviable_2016_months_as_number, \
			aviable_2015_months, aviable_2015_months_as_number, \
			aviable_2017_motors,aviable_2016_motors,aviable_2015_motors)
	        





    #libs.main(["test_ieee_cases.py","-xs"])
    #return os.chdir(original_path+'\excel_data\CORRIENTES %s' %year)
