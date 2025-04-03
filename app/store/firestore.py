from google.cloud import firestore
from datetime import datetime, timedelta

# Инициализация клиента Firestore
db = firestore.Client.from_service_account_json("path_to_your_service_account.json")

def save_video_link_and_time(video_id: str, expiration_time: datetime):
    doc_ref = db.collection("video_links").document(video_id)
    doc_ref.set({
        "video_id": video_id,
        "expiration_time": expiration_time,
    })

def get_video_link(video_id: str):
    doc_ref = db.collection("video_links").document(video_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    return None
