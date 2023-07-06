# silver-octo-fiesta

---

# Azure Blob Storage Data Migration Utility
<img width="1265" alt="Screenshot 2023-07-06 at 9 16 10 AM" src="https://github.com/Marlvin12/silver-octo-fiesta/assets/122947486/1c5bca86-2e09-472a-9efd-1476ed05e848">


This utility is a Python script that automates the migration of data from a local directory to Azure Blob Storage. 

## Functionality

The script scans through a specified local directory, and uploads each file found to a specified Azure Blob Storage container.

## Requirements

- Python 3.6 or later
- azure-storage-blob package
- An Azure Storage account and a container in the account

## Installation

First, ensure that you have Python 3.6 or later installed on your system. You can download Python from [here](https://www.python.org/downloads/).

Then, install the required Python package using pip:

```bash
pip install azure-storage-blob
```

## Configuration

Before running the script, make sure to replace the placeholders in the script with your actual Azure Blob Storage details:

- Replace `"your_connection_string"` with your Azure Blob Storage account connection string.
- Replace `"your_container_name"` with your Azure Blob Storage container name.
- Replace `"/path/to/your/directory"` with the path to the local directory that contains the files you want to upload.

## Usage

To run the script, navigate to the script’s directory and type the following command in your terminal:

```bash
python your_script_name.py
```

Replace "your_script_name.py" with the actual name of your Python script.

The script will upload all files in the specified local directory to the specified Azure container.

## Extending Functionality

This is a basic data migration utility. To extend its functionality, consider adding error handling, logging, and the ability to handle files in subdirectories.

---

