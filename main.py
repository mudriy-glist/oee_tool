from mechanics import data_process
from settings import data_dict, unique_machines, target_time
from report_generate import report_generate

#takes data from local file and modifies data_dict
data_process(data_dict, unique_machines)

#takes data_dict and use it to generate report                
report_generate(data_dict, unique_machines, target_time)
