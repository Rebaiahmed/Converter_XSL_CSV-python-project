import pandas as pd
import filemapper as fm
import xlrd


all_files = fm.load('./data_excel')


for f in all_files:
     print(f)
     #xls = pd.ExcelFile('./data_excel/'+f)
     data_sheets = xlrd.open_workbook('./data_excel/'+ f)




df = pd.read_excel('GRIP-IRA 2009-2010.xls')
# this will read the first sheet into df
xls = pd.ExcelFile('GRIP-IRA 2009-2010.xls')

# Now you can list all sheets in the file
#print(xls.sheet_names)

sheet_to_df_map = {}
for sheet_name in xls.sheet_names:
    #print(sheet_name)
    sheet_to_df_map[sheet_name] = xls.parse(sheet_name)
    #print(sheet_to_df_map[sheet_name])
    sheet_to_df_map[sheet_name]['annee']=2020
    sheet_to_df_map[sheet_name].to_csv(sheet_name +'.csv', sep='\t', encoding='utf-8')
