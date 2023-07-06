from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

try:
    blob_service_client = BlobServiceClient.from_connection_string("XXXXXXXXXXXXXXXXXX")
    
    container_name = "XXXXXXXXXXXX"
    local_path = "XXXXXXXXXXXXX"
    for filename in os.listdir(local_path):
        
        blob_client = blob_service_client.get_blob_client(container_name, filename)

        print("\nUploading to Azure Storage as blob:\n\t" + filename)

        with open(os.path.join(local_path, filename), "rb") as data:
            blob_client.upload_blob(data)

except Exception as ex:
    print('Exception:')
    print(ex)
