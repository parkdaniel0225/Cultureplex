
import csv
import os
import math

def split_csv(file_path, chunk_size=20971520):
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    output_folder = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_file_template = os.path.join(output_folder, file_name + '_part{0}' + file_extension)

    with open(file_path, encoding="utf8") as file:
        reader = csv.reader(file)
        header = next(reader)
        chunk_count = 1
        chunk = []

        for row in reader:
            chunk.append(row)
            current_chunk_size = sum(len(row) for row in chunk)

            if current_chunk_size >= chunk_size:
                with open(output_file_template.format(chunk_count), 'w') as output_file:
                    writer = csv.writer(output_file)
                    writer.writerow(header)
                    writer.writerows(chunk)

                chunk_count += 1
                chunk = []

        if chunk:
            with open(output_file_template.format(chunk_count), 'w') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(header)
                writer.writerows(chunk)

file_path = r'C:\Users\parkd\OneDrive\Desktop\cultureplex\uFINAL_copy1.csv'
split_csv(file_path)
