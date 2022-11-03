import pandas as pd

async def check_document_format():
    print('check document')

#Форматируем ФИО в ФИ
def format_fio(fio):
    return fio.split()[0] + fio.split()[1]

async def get_data_from_file(file):
    result_dict = {}
    #Преобразование файла, на первое время
    org_table = pd.read_excel(file,skiprows = 6,usecols = range(0,6),header=None,names = ['Name','Nan','Vac_type','Nan1','Work_days','Vac_days'])
    org_table.dropna(axis = 'columns',inplace= True)

    org_table['Name'] = org_table.apply(lambda row:format_fio(row['Name']),axis = 1)

    #org_table.to_dict('split')


    return org_table

