import os
import shutil
import pandas as pd
data_dir = "../data/"
participants = os.listdir(data_dir)

for participant in participants:
    date_dir = os.listdir(data_dir+participant)
    participant_dir = data_dir+participant+'/'
    for date in date_dir:
        if not os.listdir(participant_dir+date):
            shutil.rmtree(participant_dir+date)
            continue
        final_dir = participant_dir+date+'/'
        left_data = pd.read_csv(final_dir+'left_data.csv',header=None).values
        right_data = pd.read_csv(final_dir + 'right_data.csv', header=None).values
        

