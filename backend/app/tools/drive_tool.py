from langchain.tools import tool
from app.services.drive_service import GoogleDriveService

service = GoogleDriveService()

@tool
def drive_search_tool(query: str):
    '''
    Search files in Google Drive using Drive API q parameter.
    '''

    files = service.search_files(query)

    if not files:
        return "No matching files found."

    results = []

    for f in files:
        results.append({
            "name": f["name"],
            "type": f["mimeType"],
            "modified": f.get("modifiedTime"),
            "link": f.get("webViewLink")
        })

    return results