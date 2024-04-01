# AutoClean-Downloads

## Overview
The `DownloadsDeClutter` project was initiated from a simple realization during a routine check in PowerShell: my Downloads folder was cluttered with an overwhelming number of files. Manually sorting and deleting these files seemed like a daunting task, so I turned to Python and automation to streamline the process.

## Motivation
The main goal was to create an efficient, automated system for cleaning up the Downloads folder without the need for manual intervention. This was not only to save time but also to implement a solution that could be reused in the future, either on a scheduled basis or as needed.

## Process
1. **Initial Scripting in Visual Studio Code:** Utilized Python to script the initial phase of the project. This involved creating a DataFrame (df) that cataloged all files in the Downloads directory, capturing essential details such as file names, creation dates, file types, and sizes.

2. **Data Analysis with Google Colab:** To further analyze the dataset and make informed decisions on which files to delete, I leveraged Google Colab. This platform enabled me to filter out old image files, which were my primary targets for deletion.

3. **Creating a Target Deletion List:** After identifying the files to be purged, I compiled a new DataFrame listing these targets. This step was crucial for transitioning back to a local environment for the actual deletion process.

4. **Executing the Deletion Script in Visual Studio Code:** Finally, I returned to Visual Studio Code to run a Python script capable of deleting the files listed in the DataFrame from the Downloads directory. This step actualized the cleanup process, removing the unwanted files from my system.

## Tools and Libraries Used
- **Python:** The backbone of the project, used for scripting both the analysis and deletion processes.
- **Pandas:** A powerful data manipulation library that facilitated the handling of file data within DataFrames.
- **os, csv, mimetypes, datetime:** Essential Python libraries that were instrumental in file manipulation, data formatting, and understanding file properties.
- **Visual Studio Code:** My local IDE of choice for writing and executing Python scripts.
- **Google Colab:** An online platform that provided a more flexible environment for data analysis and manipulation.

## Conclusion
`AutoClean-Downloads` serves as a testament to the power of automation and data analysis. By combining Python scripting with strategic use of data analysis tools, I was able to significantly declutter my Downloads folder without the tedium of manual file management. This project not only streamlined my immediate cleanup task but also provided a reusable tool for future file management needs.
