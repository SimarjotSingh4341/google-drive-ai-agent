from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import json

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

service_account_info = json.loads(
    os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
)

credentials = service_account.Credentials.from_service_account_info(
    service_account_info,
    scopes=SCOPES
)

service = build('drive', 'v3', credentials=credentials)


class GoogleDriveService:

    def __init__(self):
        self.folder_id = os.getenv("GOOGLE_DRIVE_FOLDER_ID")

    def get_all_folder_ids(self, parent_folder_id):

        folder_ids = [parent_folder_id]

        query = (
            f"'{parent_folder_id}' in parents "
            f"and mimeType='application/vnd.google-apps.folder' "
            f"and trashed=false"
        )

        response = service.files().list(
            q=query,
            fields="files(id, name)"
        ).execute()

        folders = response.get("files", [])

        for folder in folders:
            child_id = folder["id"]
            folder_ids.extend(self.get_all_folder_ids(child_id))

        return folder_ids

    def search_files(self, query: str):

        all_folder_ids = self.get_all_folder_ids(self.folder_id)

        parent_queries = [
            f"'{folder_id}' in parents"
            for folder_id in all_folder_ids
        ]

        parent_query = " or ".join(parent_queries)

        final_query = (
            f"({parent_query}) "
            f"and trashed=false "
            f"and ({query})"
        )

        response = service.files().list(
            q=final_query,
            fields="files(id, name, mimeType, modifiedTime, webViewLink)",
            pageSize=50
        ).execute()

        return response.get("files", [])
