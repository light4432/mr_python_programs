import datetime
import os
import pickle

# Definition of the input directory containing .txt files
input_directory = r"C:\Users\alexa\Desktop\hackaton\end_data"

# Filtering input files for ACE (those starting with "ACE" and ending with ".txt")
input_files_ace = [f for f in os.listdir(input_directory) if f.endswith(".txt") and f.startswith("ACE")]
# Filtering input files for DSCOVR (those starting with "DSCOVR" and ending with ".txt")
input_files_dscovr = [f for f in os.listdir(input_directory) if f.endswith(".txt") and f.startswith("DSCOVR")]

# Function to convert a day number to month and day
def day_number_to_month_and_day(day_number, year):
    date = datetime.date(year, 1, 1) + datetime.timedelta(days=day_number - 1)
    result_month = date.month
    day_result = date.day
    return result_month, day_result

# Function to read and process a file
def file_read(file_name):
    try:
        with open(f'{input_directory}\{file_name}', 'r') as file:
            lines = file.readlines()
            final_list = []
            for i in range(len(lines)):
                lines[i] = lines[i].strip('\n')
                lines[i] = lines[i].replace("\t", "  ")
                month, day = day_number_to_month_and_day(int(lines[i][6:9]), int(lines[i][:4]))
                try:
                    final_list.append([datetime.date(int(lines[i][:4]), month, day), int(lines[i][11:13]),
                                       int(lines[i][15:17]), float(lines[i][18:len(lines[i])])])
                except ValueError:
                    a = 1
            return final_list
    except FileNotFoundError:
        return ("ERROR - FILE NOT FOUND")

# Function to organize data into lists
def into_list(input_files_ace, input_files_dscovr):
    data_ace = []
    data_dscovr = []
    for i in range(len(input_files_ace)):
        data_ace.append(file_read(input_files_ace[i]))
    for j in range(len(input_files_dscovr)):
        data_dscovr.append(file_read(input_files_dscovr[j]))
    return [data_ace, data_dscovr]

# Call the function to obtain the results
results = into_list(input_files_ace, input_files_dscovr)

# Separation of ACE and DSCOVR data
output_files_ace = results[0]
output_files_dscovr = results[1]

# Creating data for machine learning
ml_ace = []
for i in range(len(output_files_ace)):
    for j in range(10, len(output_files_ace[i])):
        ml_ace.append([[output_files_ace[i][k][3] for k in range(j - 10, j)], output_files_ace[i][j][3]])

ml_dscovr = []
for i in range(len(output_files_dscovr)):
    for j in range(10, len(output_files_dscovr[i])):
        ml_dscovr.append([[output_files_dscovr[i][k][3] for k in range(j - 10, j)], output_files_dscovr[i][j][3]])

# Saving data to pickle files
f_ace = open("ace.pkl", 'wb')
pickle.dump(ml_ace, f_ace)
f_ace.close()

f_dscovr = open("dscovr.pkl", 'wb')
pickle.dump(ml_dscovr, f_dscovr)
f_dscovr.close()

# Display a completion message
print('done')