import os
import csv
import mimetypes
from datetime import datetime

# Path to the downloads folder where the files are located
download_folder = 'C:/Users/Carlos/Downloads'

# Output CSV file path, will be saved to the Desktop
output_csv = 'C:/Users/Carlos/Desktop/lista_archivos.csv'

# Initializing the list to store file data with new headers
data_list = [('Nombre de Archivo', 'Fecha de Creación', 'Fecha de Último Acceso', 'Tamaño del Archivo (bytes)', 'Tipo de Archivo')]

# Iterating through the files in the downloads folder
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)

    # Skip directories, only process files
    if os.path.isfile(file_path):
        # Get the file creation (modification) date
        creation_time = os.path.getmtime(file_path)
        creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')

        # Get the last access date of the file
        last_access_time = os.path.getatime(file_path)
        last_access_date = datetime.fromtimestamp(last_access_time).strftime('%Y-%m-%d %H:%M:%S')

        # Get the file size
        file_size = os.path.getsize(file_path)

        # Determine the file type (MIME type)
        filetype, _ = mimetypes.guess_type(file_path)
        filetype = filetype if filetype else 'Desconocido'

        #Add the file information to the list, including the new columns
        data_list.append((filename, creation_date, last_access_date, file_size, filetype))

# Saving the data to a CSV file
with open(output_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data_list)

# Confirmation message after saving the data
print(f'The data has been saved in {output_csv}')
