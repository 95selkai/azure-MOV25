from flask import Flask, request
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from datetime import datetime
import uuid

app = Flask(__name__)

STORAGE_ACCOUNT = "novatrixstorage"
CONTAINER_NAME = "arenden"

account_url = f"https://{STORAGE_ACCOUNT}.blob.core.windows.net"
credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(
account_url=account_url,
credential=credential
)

container_client = blob_service_client.get_container_client(CONTAINER_NAME)


@app.route("/submit", methods=["POST"])
def submit():
name = request.form.get("name")
mail = request.form.get("mail")
msg = request.form.get("msg")
bild = request.files.get("bild")

arende_id = str(uuid.uuid4())

arende = f"""
Ärende-ID: {arende_id}
Datum: {datetime.now()}
Namn: {name}
E-post: {mail}
Meddelande: {msg}
"""

container_client.upload_blob(
name=f"{arende_id}-arende.txt",
data=arende,
overwrite=True
)

if bild and bild.filename:
container_client.upload_blob(
name=f"{arende_id}-{bild.filename}",
data=bild.stream,
overwrite=True
)

return "Tack! Ditt ärende har sparats."


if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000)
