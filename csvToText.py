import pandas as pd
import os
import re
import uuid

def sanitize_filename(filename):
    """Sanitize the filename by removing or replacing special characters."""
    filename = re.sub(r'[\\/*?:"<>|]', '', filename)
    filename = filename.replace('/', '_').replace('\\', '_')
    return filename

# Specify the directory
directory = 'C:\\Users\\parkd\\OneDrive\\Desktop\\cultureplex'

# Folder for saving text files
folder_name = 'TXT'
folder_path = os.path.join(directory, folder_name)

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Loop to handle multiple CSV files
for file_number in range(1, 29):  # Includes data_1.csv to data_28.csv
    csv_file_name = f'data_{file_number}.csv'
    csv_file_path = os.path.join(directory, csv_file_name)

    # Read the CSV file
    df = pd.read_csv(csv_file_path)
    filenames = []

    for index, row in df.iterrows():
        filename_base = sanitize_filename(str(row.iloc[0]))
        unique_id = str(uuid.uuid4())
        filename_with_uuid = f"{filename_base}_{unique_id}"

        filenames.append(filename_with_uuid)

        full_filename = os.path.join(folder_path, filename_with_uuid + '.txt')

        content = str(row.iloc[2])
        with open(full_filename, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"File '{full_filename}' created.")

    df['filename'] = filenames
    updated_csv_name = f'LPdata_{file_number}.csv'
    df.to_csv(os.path.join(directory, updated_csv_name), index=False)
    print(f"Updated CSV file '{updated_csv_name}' with filenames saved.")
