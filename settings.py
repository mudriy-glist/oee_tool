# Author: Peter Kulisov
# Copyright: Peter Kulisov <peter.kulisov@gmail.com>
# If there are any issues contact me on the email above.
#
# Version 1.0
# Date: 11/08/2022
#target time which is used to calculate OEE first key
target_time = 18.316

#declare dictionary
data_dict = {}

#List of machines that will be pulled from excel
unique_machines = ['YAMAZAKI LATHE', 'VERT. MCING CEN',
'VAC-BLAST', 'V/C SMART-530C', 'V/C SMART-430A',
'TOOL ROOM', 'T_R_S GRINDER', 'T_R_PED DRILL',
'T_R_LATHE_L', 'T_R_BRIDGE', 'SYKES V6 SHAPER',
'SURFACE GRINDER', 'STUDER-33', 'STOCK STORE ISS',
'SPIRADRIVE HOB', 'SMALL CYL. GRD', 'SLOTTING',
'ROLL MARKING', 'QUALITY REVIEW', 'PRESSES',
'PLANNER ENG', 'PHOENIX 280C', 'PART PROTECTION',
'PART MARK ELEC', 'PART MARK', 'PAINTING',
'NEXUS-250_TC', 'MORI-SEIKI CHK', 'MOL-Part Mark',
'MOL-Mill/CNC','MOL-Lathe/CNC', 'MOL-Inspect', 'MOL-Grind/Hone',
'MOL-Gear/Spline', 'MOL-Bench/Assy', 'MIKRON HOBBERS',
'MAZAK QT', 'MATRIX WORM GRD', 'MATRIX THRD GRD',
'M_HARRISON 400T', 'LASER MARK', 'LASER ENGRAVE',
'LAPPING', 'KITAMURA MY C 4', 'INTERN GRINDER',
'IN PROCESS INSP', 'HONING', 'GLEASON P90G',
'GLEASON P60 HOB', 'GLEASON P400ES', 'GEAR GRINDER',
'FINAL INSPECT', 'ERFURT CYL. GRD', 'EDM WIRE', 'EDM SINK',
'DRILL & TAP', 'DOWDING HOBBER', 'DOIMAK WORM GRD',
'DEBURR', 'CENTRE LATHES', 'BAR STORES  CUT',
'BAR STORES', 'ASSY STORES ISS', 'ASSEMBLY INSP.', 'ASSEMBLY', '7A SPIRAL BEVEL',
'2A CONIFLEX BEV', '104 C/FLEX BEV', '**REWORK**']

#Data input filename
FILE_NAME = "export_oee.xlsx"