# Author: Peter Kulisov
# Copyright: Peter Kulisov <peter.kulisov@gmail.com>
# If there are any issues contact me on the email above.
#
# Version 1.0
# Date: 11/08/2022
from mechanics import data_process
from settings import data_dict, unique_machines, target_time
from report_generate import report_generate

#takes data from local file and modifies data_dict
data_process(data_dict, unique_machines)

#takes data_dict and use it to generate report                
report_generate(data_dict, unique_machines, target_time)
