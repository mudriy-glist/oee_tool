import pandas as pd
from settings import FILE_NAME

def data_process(data_dict, unique_machines):

    #instance for data from excel file in pandas dataframe
    df = pd.read_excel(f"./{FILE_NAME}")

    #remap dataframe
    df = pd.DataFrame({
            "machine" : df["TSWCID"],
            "part_no" : df["WOPartNo"],
            "wo" : df["TSWONo"],
            "op_no" : df["TSOperNo"],
            "total_time_hour" : df["TSTotTimeDec"],
            "qty" : df["TSQuantity"],
            "start_time" : df["TSStartTime"],
            "finish_time" : df["TSFinishTime"],
            "employee_id" : df["TSEmployeeID"],
            "op_complete" : df["TSOpComplete"],
            "date" : None
        })

    #add date column to dataframe
    df["date"] = [d.date() for d in df["start_time"]]

#   algorithm to pull data from dataframe and populate data_dict
#   {'MACHINE': {'DATE':[QTY, TIME_TOTAL], 'DATE':[QTY, TIME_TOTAL]},
#   'MACHINE': {'DATE':[QTY, TIME_TOTAL], 'DATE':[QTY, TIME_TOTAL]}}
    for u in unique_machines:
        data_dict[u] = {}
        for i in range(len(df)):
            if df.loc[i, "machine"] == u:
                date = df.loc[i, "date"]
                add_list = [df.loc[i, "qty"], df.loc[i, "total_time_hour"]]
                if f"{date}" not in data_dict[u]:
                    data_dict[u][f"{date}"] = add_list
                else:
                    exch_list = data_dict[u][f"{date}"]
                    data_dict[u][f"{date}"] = [add_list[0] + exch_list[0], add_list[1] + exch_list[1]]