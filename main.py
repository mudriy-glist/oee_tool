from datetime import datetime
import pandas as pd


df = pd.read_excel("./export_oee.xlsx")
df_new = pd.DataFrame({
    "machine" : df["TSWCID"],
    "part_no" : df["WOPartNo"],
    "wo" : df["TSWONo"],
    "op_no" : df["TSOperNo"],
    "total_time_hour" : df["TSTotTimeDec"],
    "qty" : df["TSQuantity"],
    "start_time" : df["TSStartTime"],
    "finish_time" : df["TSFinishTime"],
    "employee_id" : df["TSEmployeeID"],
    "op_complete" : df["TSOpComplete"]
})
df_new["total_time_day"] = None
df_new["date"] = [d.date() for d in df_new["start_time"]]
unique_machines = list(df_new['machine'].unique())
unique_machines_values = list(df_new['machine'].value_counts())
print(unique_machines)
for i in unique_machines:
