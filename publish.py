import os
import sys
from azure.storage.filedatalake import DataLakeServiceClient, ContentSettings
from pathlib import Path

CONTENT_TYPES = {
    "svg": "image/svg+xml",
    "png": "image/png",
    "html": "text/html",
    "js": "text/javascript",
    "css": "text/css",
    "json": "application/json",
    "txt": "text/plain",
    "ico": "image/x-icon",
}

print("Starting build_to_datalake.py")
# Set the environment variables
AZURE_STORAGE_CONNECTION_STRING = sys.argv[1]


if AZURE_STORAGE_CONNECTION_STRING is None or AZURE_STORAGE_CONNECTION_STRING == "":
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING is not set")


print("Connecting to datalake and connecting to $web container")
# init the datalake service client using the full connection string
datalake_service_client = DataLakeServiceClient.from_connection_string(
    AZURE_STORAGE_CONNECTION_STRING
)

# create connection to $web container
containter_client = datalake_service_client.get_file_system_client(file_system="$web")
print("Starting move files to datalake")
# upload the files to the app folder
local_path = Path(__file__).parent / "build"
print("debug: local_path: ", local_path)
for root, dirs, files in os.walk(local_path):
    for file in files:
        file_path = os.path.join(root, file)
        relative_path = os.path.relpath(file_path, local_path)
        datalake_file_client = containter_client.get_file_client(relative_path)

        with open(file_path, "rb") as data:
            content_type = file.split(".")[-1]

            if content_type in CONTENT_TYPES:
                content_type = CONTENT_TYPES[content_type]
            else:
                content_type = "text/plain"

            content_settings = ContentSettings(content_type=content_type)
            print(f"Uploading {file} to {relative_path} as {content_type}")
            datalake_file_client.upload_data(
                data, overwrite=True, content_settings=content_settings
            )
