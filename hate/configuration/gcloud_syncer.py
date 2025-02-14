import os
import logging


class GCloudSync:

    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):
       
        logging.info(f"Uploading {self} to gcloud storage")
        logging.info(f"Uploading {gcp_bucket_url} to gcloud storage")
        logging.info(f"Uploading {filepath} to gcloud storage")
        logging.info(f"Uploading {filename} to gcloud storage")

        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        logging.info(f"Command to sync folder to gcloud: {command}")
        # command = f"gcloud storage cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        os.system(command)

    # def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):
    #     logging.info(f"Uploading {self} to gcloud storage")
    #     logging.info(f"Uploading {gcp_bucket_url} to gcloud storage")
    #     logging.info(f"Uploading {destination} to gcloud storage")
    #     logging.info(f"Uploading {filename} to gcloud storage")

    #     command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
    #     logging.info(f"Uploading {command} command")
    #     # command = f"gcloud storage cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
    #     os.system(command)
 #gsutil cp gs://hate_speech_recognition_nlp/dataset.zip D:\Projects\NLP End to End\End-to-End-NLP-Project\artifacts\02_11_2025_12_24_17\DataIngestionArtifacts/dataset.zip
    def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):
        logging.info(f"Uploading {filename} from {gcp_bucket_url} to {destination}")

        # Ensure Windows path is correctly formatted
        destination_path = os.path.join(destination, filename)

        # Enclose paths in quotes to handle spaces
        command = f'gsutil cp gs://{gcp_bucket_url}/{filename} "{destination_path}"'

        logging.info(f"Running command: {command}")
        os.system(command)  # Run