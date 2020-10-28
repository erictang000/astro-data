import subprocess
import sys

for i in range(2, 10):
	if i == 2:
		for j in range(399, 999):
			original_stdout = sys.stdout # Save a reference to the original standard output

			with open('input.txt', 'w') as f:
				sys.stdout = f # Change the standard output to the file we created.
				print('!$$SOF')
				print(f'COMMAND= \"{i}99\"')
				print(f'CENTER= \"{j}@399\"')
				print('MAKE_EPHEM= \"YES\"')
				print('TABLE_TYPE= \"OBSERVER\"')
				print('START_TIME= \"2000-01-01\"')
				print('STOP_TIME= \"2020-12-25\"')
				print('STEP_SIZE= \"1 d\"')
				print('CAL_FORMAT= \"CAL\"')
				print('TIME_DIGITS= \"MINUTES\"')
				print('ANG_FORMAT= \"HMS\"')
				print('OUT_UNITS= \"KM-S\"')
				print('RANGE_UNITS= \"AU\"')
				print('APPARENT= \"AIRLESS\"')
				print('SUPPRESS_RANGE_RATE= \"NO\"')
				print('SKIP_DAYLT= \"NO\"')
				print('EXTRA_PREC= \"NO\"')
				print('R_T_S_ONLY= \"NO\"')
				print('REF_SYSTEM= \"J2000\"')
				print('CSV_FORMAT= \"YES\"')
				print('OBJ_DATA= \"YES\"')
				print('QUANTITIES= \"1,9,20,23,24\"')
				print('!$$EOF')
				sys.stdout = original_stdout # Reset the standard output to its original value
				f.close();
			output_name = f"output{i}_{j}.txt"
			with open(output_name, 'w') as f:
				sys.stdout = f # Change the standard output to the file we created.
				# perl_script = subprocess.Popen(["perl", "sample_horizons_batch_script.pl"], stdout=sys.stdout)
				print(subprocess.check_output(["perl", "sample_horizons_batch_script.pl"]))
				# perl_script.check_output()
				sys.stdout = original_stdout # Reset the standard output to its original value
				f.close();
			print(i, j);
	else:
		for j in range(1, 999):
			original_stdout = sys.stdout # Save a reference to the original standard output

			with open('input.txt', 'w') as f:
				sys.stdout = f # Change the standard output to the file we created.
				print('!$$SOF')
				print(f'COMMAND= \"{i}99\"')
				print(f'CENTER= \"{j}@399\"')
				print('MAKE_EPHEM= \"YES\"')
				print('TABLE_TYPE= \"OBSERVER\"')
				print('START_TIME= \"2000-01-01\"')
				print('STOP_TIME= \"2020-12-25\"')
				print('STEP_SIZE= \"1 d\"')
				print('CAL_FORMAT= \"CAL\"')
				print('TIME_DIGITS= \"MINUTES\"')
				print('ANG_FORMAT= \"HMS\"')
				print('OUT_UNITS= \"KM-S\"')
				print('RANGE_UNITS= \"AU\"')
				print('APPARENT= \"AIRLESS\"')
				print('SUPPRESS_RANGE_RATE= \"NO\"')
				print('SKIP_DAYLT= \"NO\"')
				print('EXTRA_PREC= \"NO\"')
				print('R_T_S_ONLY= \"NO\"')
				print('REF_SYSTEM= \"J2000\"')
				print('CSV_FORMAT= \"YES\"')
				print('OBJ_DATA= \"YES\"')
				print('QUANTITIES= \"1,9,20,23,24\"')
				print('!$$EOF')
				sys.stdout = original_stdout # Reset the standard output to its original value
				f.close();
			output_name = f"output{i}_{j}.txt"
			with open(output_name, 'w') as f:
				sys.stdout = f # Change the standard output to the file we created.
				# perl_script = subprocess.Popen(["perl", "sample_horizons_batch_script.pl"], stdout=sys.stdout)
				print(subprocess.check_output(["perl", "sample_horizons_batch_script.pl"]))
				# perl_script.check_output()
				sys.stdout = original_stdout # Reset the standard output to its original value
				f.close();
			print(i, j);

				
