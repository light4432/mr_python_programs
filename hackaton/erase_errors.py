import os

# Directory containing input files
input_directory = r"C:\Users\alexa\Desktop\hackaton\raw_data"

# Output directory
output_directory = r"C:\Users\alexa\Desktop\hackaton\end_data"

# Filter input files with the .txt extension
input_files = [f for f in os.listdir(input_directory) if f.endswith(".txt")]

# Function to filter lines and write to the output file
def filter_and_write_input_file(input_file, output_directory):
    input_path = os.path.join(input_directory, input_file)
    
    with open(input_path, "r") as input_file:
        lines = input_file.readlines()
    
    # Step 2: Create a new list by removing lines containing "9999.99"
    new_lines = []
    
    for line in lines:
        if "9999.99" not in line:
            new_lines.append(line)
    
    # Build the output file name
    output_file_name = os.path.splitext(input_file)[0] + ".txt"
    output_path = os.path.join(output_directory, output_file_name)
    
    # Write filtered lines to the output file
    with open(output_path, "w") as output_file:
        output_file.writelines(new_lines)
    
    print(f"The file {input_file} has been processed, and the results have been written to {output_file_name}.")


# Iterate over input files and process them
for input_file in input_files:
    filter_and_write_input_file(input_file, output_directory)