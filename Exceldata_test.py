import os
import pandas as pds
import numpy as np

wdir = "/Users/Bugrahan/PycharmProjects/Exceldata_test"
filename = "Ergebnistabellen_MyoDBS_1.xlsx"
pseud = '60_MDE_0702_PD,66_MBZ_0912_PD,77_FDP_2607_PD,62_FDN_2103_PD,48_FSR_1602_PD,62_FWG_2401_PD,55_MLR_2203_PD,57_FRK_0712_PD,63_FBE_2310_PDD'
sheetname = "Rigor"

"""imports the pseudonyms of the subjects to be processed in order to later read the data accordingly"""
os.chdir(wdir)
frame_name = pds.read_excel("Ergebnistabellen_MyoDBS_1.xlsx",
                             sheet_name=sheetname)
print(frame_name)
if pseud == '':
    # ignores the data categorised as wrong/bad from the dataset (see patienten_onoff.xls for details)
    subjlist = frame_name.pseud
else:
    subjlist = frame_name[frame_name.pseud == pseud]
    idx_list = np.where(frame_name['pseud'] == pseud)