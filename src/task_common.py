import pandas as pd
import datetime
import numpy


def exec_task(demo_df, measurements_df):
    # load data from measurements into each patient
    measurements_df['date'] = pd.to_datetime(measurements_df.loc[:, 'date'])
    today = datetime.datetime.now()
    for index, row in demo_df.iterrows():
        patient_data_df = measurements_df[measurements_df['patientuid'] == row['patientuid']]
        if patient_data_df.empty:
            continue
        # Find the sex for this patient
        sex_df = patient_data_df[patient_data_df['label'] == 'Sex']
        if not sex_df.empty:
            demo_df.loc[index, 'sex'] = sex_df.iloc[0]['value']

        # Find the age for this patient
        # THIS IS NOT ACCURATE, DUE TO NOT HAVING THE MONTH AND DAY OF BIRTH OF THE PATIENT
        age_df = patient_data_df[patient_data_df['label'] == 'YOB']
        yob = 0
        if not age_df.empty:
            yob = int(age_df.iloc[0]['value'])
            demo_df.loc[index, 'age'] = today.year - yob
        # Fill diabetes if present
        # THIS IS NOT ACCURATE, DUE TO NOT HAVING THE MONTH AND DAY OF BIRTH OF THE PATIENT
        diabetes_df = patient_data_df.loc[patient_data_df['label'] ==
                                          'Diagnosis'].loc[patient_data_df['value'] == 'Diabetes']. sort_values(
                                                                                            by='date', ascending=True)
        if not diabetes_df.empty and yob > 0:
            demo_df.loc[index, 'diabetes'] = int(diabetes_df.iloc[0]['date'].year) - yob
        # Get HEF
        # Heart Ejection Fraction
        hef_df = patient_data_df.loc[patient_data_df['label'] == 'Heart Ejection Fraction'].sort_values(by='date',
                                                                                                        ascending=False)
        if not hef_df.empty:
            last_hour = hef_df.iloc[0]['date'] - datetime.timedelta(hours=1)
            last_day = hef_df.iloc[0]['date'] - datetime.timedelta(days=1)
            hef_df_1h = hef_df.loc[hef_df['date'] > last_hour]
            hef_df_24h = hef_df.loc[hef_df['date'] > last_day]
            demo_df.loc[index, 'hef_1hour'] = numpy.average(pd.to_numeric(hef_df_1h['value']).to_numpy())
            demo_df.loc[index, 'hef_24hour'] = numpy.average(pd.to_numeric(hef_df_24h['value']).to_numpy())
        else:
            demo_df.loc[index, 'hef_1hour'] = numpy.NaN
            demo_df.loc[index, 'hef_24hour'] = numpy.NaN
