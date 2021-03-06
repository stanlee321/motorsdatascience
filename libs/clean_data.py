import os
import pandas as pd
import pickle
import xlrd


cwd = os.getcwd()           # Original Path to libs
original_path = cwd
print('ORIGINAL PATH', original_path)



def get_path_to_files(year):
    return os.chdir(original_path+'\excel_data\CORRIENTES %s' %year)

files = []

path_to_files2015 = get_path_to_files(2015)
files_2015 = os.listdir('.')
files.append(files_2015)


path_to_files2016 = get_path_to_files(2016)
files_2016 = os.listdir('.')
files.append(files_2016)


path_to_files2017 = get_path_to_files(2017)
files_2017 = os.listdir('.')
files.append(files_2017)



print('----Found Files----')
print('----Found Files----')


print(files_2015)
print(files_2016)
print(files_2017)

print(files)

## Cargamdp xlrd que nos permite leer archivos excel dentro de python
## con el fin de saber cuantos y que _sheets_ existen en cada archivo.



def data_frame_to_dict(excel_file, year):
    os.chdir(original_path+'\excel_data\CORRIENTES %s' %year)
    # loading the the names of every sheetname
    print(excel_file)
    wb = xlrd.open_workbook(excel_file)
    
    # dictionary to queue the data with the format dict[Maquine]= dataframe
    dict_for_dfs = {}
    
    # Dealing with sheets

    for data_sheet in wb.sheet_names():
        # this if statement is about the size of columns lenght, the last ones sheets are problematic
        # , this sheets have size from 0 to 5 , the rest are normal size from 0 to 10 or 11,
        # we don't want skip important columns, so the last sheets are passet without parse_cols
        
        if data_sheet =='BOMBAS DE VACIO' or 'AGUA DE SERVICIOS' or 'COMPERSOR-CHILLER' or 'EFLUENTES':
            month_201X = pd.read_excel(excel_file, skiprows=[0,1], sheetname='%s' %data_sheet)
            month_201X = month_201X.fillna(0.0)
            dict_for_dfs[data_sheet] = (month_201X)
            
            
        else:
            month_201X = pd.read_excel(excel_file, skiprows=[0,1], parse_cols=[1,2,5,6,7,8,9], sheetname='%s' %data_sheet)
            month_201X = month_201X.fillna(0.0)
            
            
            dict_for_dfs[data_sheet] = (month_201X)
    return(dict_for_dfs)

def create_year_201X(file_list_year, year):
    year_201X = {}
    month_data = {}
    for pos, file in enumerate(file_list_year):
    
        if "ENERO" in file:
            year_201X['ENE'] = (data_frame_to_dict(file_list_year[pos], year))
            month_data[1] = year_201X['ENE']
        if 'FEBRERO' in file:
            year_201X['FEB'] = (data_frame_to_dict(file_list_year[pos], year))
            month_data[2] = year_201X['FEB']
        if 'MARZO' in file:
            year_201X['MAR']=(data_frame_to_dict(file_list_year[pos], year))
            month_data[3] = year_201X['MAR']
        if 'ABRIL' in file:
            year_201X['ABR']=(data_frame_to_dict(file_list_year[pos], year))
            month_data[4] = year_201X['ABR']
        if 'MAYO' in file:
            year_201X['MAY'] = (data_frame_to_dict(file_list_year[pos], year))
            month_data[5] = year_201X['MAY']
            
        if "JUNIO" in file:
            year_201X['JUN'] = (data_frame_to_dict(file_list_year[pos], year))
            month_data[6] = year_201X['JUN']
        if 'JULIO' in file:
            year_201X['JUL'] = (data_frame_to_dict(file_list_year[pos], year))
            month_data[7] = year_201X['JUL']
        if 'AGOSTO' in file:
            year_201X['AUG'] = (data_frame_to_dict(file_list_year[pos], year))
            month_data[8] = year_201X['AUG']
        if 'SEPTIEMBRE' in file:
            year_201X['SEP'] = (data_frame_to_dict(file_list_year[pos], year))
            month_data[9] = year_201X['SEP']
        if 'OCTUBRE' in file:
            year_201X['OCT'] = (data_frame_to_dict(file_list_year[pos], year))
            month_data[10] = year_201X['OCT']
        if 'NOVIEMBRE' in file:
            year_201X['NOV'] = (data_frame_to_dict(file_list_year[pos], year)) 
            month_data[11] = year_201X['NOV']
        if 'DICIEMBRE' in file:
            year_201X['DEC'] = (data_frame_to_dict(file_list_year[pos], year)) 
            month_data[12] = year_201X['DEC']
    return year_201X, month_data




year_2015, month_data_2015 = create_year_201X(files_2015,2015)
year_2016, month_data_2016 = create_year_201X(files_2016,2016)
year_2017, month_data_2017 = create_year_201X(files_2017,2017)


## Taking the reference of 2017 





def parsing_columns(year_201X, files_year,year):

    os.chdir(original_path+'\excel_data\CORRIENTES %s' %year)

    aviable_months = list(year_201X.keys())
    wb = xlrd.open_workbook(files_year[-1])
    sheets = wb.sheet_names()
    print(aviable_months)

    

    # Giving Columns names to the compatible dataframes
    for month in aviable_months:
        for sheet in sheets:
            if len(year_201X[month][sheet].columns) == 10:
                year_201X[month][sheet] = year_201X[month][sheet].drop(year_201X[month][sheet].columns[[0,3,4]], axis = 1)
                year_201X[month][sheet].columns = ['Description', 'Place','Nominal_current','Motor','L1','L2','L3']
            elif len(year_201X[month][sheet].columns) == (11 or 12):
                year_201X[month][sheet] = year_201X[month][sheet].drop(year_201X[month][sheet].columns[[0,3,4,-1]], axis = 1)
                year_201X[month][sheet].columns = ['Description', 'Place','Nominal_current','Motor','L1','L2','L3']
            else:
                #year_2016[month][sheet] = year_2016[month][sheet].drop(year_2016[month][sheet].columns[[3,4]], axis = 1)
                print('los demas...NO COVERTIDOS', sheet)

parsing_columns(year_2015, files_2015,2015)
parsing_columns(year_2016, files_2016,2016)
parsing_columns(year_2017, files_2017,2017)



           
print("SAVING FILE DICT TO DISK: -----> " + original_path )            

def save_to_disk(year_201X, month_data_201X, year):

    # write python dict to a file

    output_year = open(original_path + '\outputs' +'\data_'+'%s' %year+'.pkl', 'wb')
    pickle.dump(year_201X, output_year)
    output_year.close()
    print('Done! %s'%year +'_data.pkl')



    output_dict = open(original_path + '\outputs'+'\month_data_dict_'+'%s' %year +'.pkl', 'wb')
    pickle.dump(month_data_201X, output_dict)
    output_dict.close()
    print('Done! %s'%year +'_month_data_dict.pkl')


save_to_disk(year_2015, month_data_2015, 2015)
save_to_disk(year_2016, month_data_2016, 2016)
save_to_disk(year_2017, month_data_2017, 2017)

os.chdir(original_path)

print(os.chdir(original_path))
print('Done!!!')

#if __name__ == "__main__":
