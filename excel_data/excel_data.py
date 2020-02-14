import os
import pandas as pds
import numpy as np

wdir = "~Users/Bugrahan/Desktop/Data"
filename = "Ergebnistabellen_MyoDBS_1.xlsx"
pseud = ''
sheetname = "sheet name to look at"

"""imports the pseudonyms of the subjects to be processed in order to later read the data accordingly"""
os.chdir(wdir)
frame_name = pds.read_excel(Ergebnistabellen_MyoDBS_1.xlsx
                            ,sheet_name=sheetname)
if pseud == '':
    # ignores the data categorised as wrong/bad from the dataset (see patienten_onoff.xls for details)
    subjlist = frame_name.pseud
else:
    subjlist = frame_name[frame_name.pseud == pseud]
    idx_list = np.where(frame_name['pseud'] == pseud)