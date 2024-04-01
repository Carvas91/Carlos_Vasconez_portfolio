import os
import pandas as pd

# Path to the CSV file that contains the list of files to be deleted
path_to_csv = 'C:/path_to_your_downloaded_file/lista_para_eliminar.csv'
# Path to the Downloads folder from where the files will be deleted
download_folder = 'C:/Users/Carlos/Downloads'

# Loading the list of files from the CSV into a DataFrame
df = pd.read_csv(path_to_csv)

# Looping through the DataFrame to process each file
for archivo in df['Nombre de Archivo']:
    file_path = os.path.join(download_folder, archivo)
    try:
        os.remove(file_path)
        print(f'The file {archivo} has been successfully deleted.')
    except FileNotFoundError:
        print(f'The file {archivo} was not found and could not be deleted.')
    except PermissionError:
        print(f"Permission denied to delete the file {archivo}.")
    except Exception as e:
        print(f"An error occurred while deleting the file {archivo}: {e}")
