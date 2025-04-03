from google.cloud import storage
import os

# Инициализация клиента
client = storage.Client.from_service_account_json("path_to_your_service_account.json")
bucket_name = "your_bucket_name"
bucket = client.get_bucket(bucket_name)

def upload_audio_to_gcs(file_path: str, file_name: str):
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_path)
    return blob.public_url

def delete_audio_from_gcs(file_name: str):
    blob = bucket.blob(file_name)
    blob.delete()
    return f"{file_name} deleted from GCS."
