import pandas as pd
import sqlite3
from task_common import exec_task

conn = sqlite3.connect("../data/sqlite.db")
demo_df_db = pd.read_sql_query("SELECT patientuid, zip_code, income, "
                               "'99' as diabetes, '0' as age, '' as sex, '0' as hef_1hour, '0' as hef_24hour FROM "
                               "demographics", conn)
print('Loaded data of patients')

measurements_df_db = pd.read_sql_query("SELECT * FROM measurements WHERE label in ('Sex', 'YOB', 'Heart Ejection "
                                       "Fraction', 'Diagnosis')", conn)
print("Processing measurements")

exec_task(demo_df_db, measurements_df_db)

print("Storing data into db")
demo_df_db.to_sql("output", conn, if_exists="replace")

conn.close()
print("Process finished")

