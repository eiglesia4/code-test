import pandas as pd
from task_common import exec_task

# Load demographics
demo_df_file = pd.read_csv('../data/demographics.csv', delimiter=',')
print('Loaded data of patients')

# Accommodate data frame to the final necessary columns
demo_df_file = demo_df_file.drop('bmi', axis=1)
demo_df_file['diabetes'] = 99
demo_df_file['age'] = 0
demo_df_file['sex'] = ""
demo_df_file['hef_1hour'] = 0
demo_df_file['hef_24hour'] = 0

# Load measurements
measurements_df_file = pd.read_csv('../data/measurements.csv', delimiter='|')
print("Processing measurements")

exec_task(demo_df_file, measurements_df_file)

print("Saving data")
demo_df_file.to_csv("../data/output.csv", index=False, columns=["patientuid", "age", "sex", "income", "zip_code",
                                                                "hef_1hour", "hef_24hour", "diabetes"])
print("Process finished")
