import argparse
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
import logging

# Setting up logging
logging.basicConfig(filename='azure_blob_operations.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def upload_blobs(local_path, container_name, blob_service_client):
    for filename in os.listdir(local_path):
        try:
            blob_client = blob_service_client.get_blob_client(container_name, filename)
            logging.info(f"Uploading to Azure Storage as blob: {filename}")
            with open(os.path.join(local_path, filename), "rb") as data:
                blob_client.upload_blob(data)
        except Exception as ex:
            logging.error(f"Exception occurred while uploading blob: {filename}. Exception: {ex}")

def download_blobs(local_path, container_name, blob_service_client):
    try:
        container_client = blob_service_client.get_container_client(container_name)
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            logging.info(f"Downloading blob: {blob.name}")
            blob_client = blob_service_client.get_blob_client(container_name, blob.name)
            with open(os.path.join(local_path, blob.name), "wb") as my_blob:
                blob_data = blob_client.download_blob()
                my_blob.write(blob_data.readall())
    except Exception as ex:
        logging.error(f"Exception occurred while downloading blobs from container: {container_name}. Exception: {ex}")

def delete_blobs(container_name, blob_service_client):
    try:
        container_client = blob_service_client.get_container_client(container_name)
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            logging.info(f"Deleting blob: {blob.name}")
            blob_client = blob_service_client.get_blob_client(container_name, blob.name)
            blob_client.delete_blob()
    except Exception as ex:
        logging.error(f"Exception occurred while deleting blobs from container: {container_name}. Exception: {ex}")

# Parsing command line arguments
parser = argparse.ArgumentParser(description='Perform operations on Azure Blob Storage')
parser.add_argument('--connection-string', required=True, help='Azure Blob Storage connection string')
parser.add_argument('--container-names', nargs='+', required=True, help='List of container names')
parser.add_argument('--local-path', required=True, help='Path to the local directory')

args = parser.parse_args()

try:
    blob_service_client = BlobServiceClient.from_connection_string(args.connection_string)
    for container_name in args.container_names:
        upload_blobs(args.local_path, container_name, blob_service_client)
        download_blobs(args.local_path, container_name, blob_service_client)
        delete_blobs(container_name, blob_service_client)
except Exception as ex:
    logging.error(f"Exception occurred while interacting with Azure Blob Storage. Exception: {ex}")

