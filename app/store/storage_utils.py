from datetime import datetime, timedelta, timezone

from app.store.firestore import save_video_link_and_time, get_video_link
from app.store.gcs import upload_audio_to_gcs, delete_audio_from_gcs


def handle_audio_and_link(audio_path: str, audio_file_name: str, video_id: str):
    # Загружаем аудио в GCS
    audio_url = upload_audio_to_gcs(audio_path, audio_file_name)

    # Сохраняем ссылку в Firestore с временем жизни 5-6 часов
    expiration_time = datetime.now(timezone.utc) + timedelta(hours=6)
    save_video_link_and_time(video_id, expiration_time)

    return audio_url

def check_expiration_and_delete(video_id: str, audio_file_name: str):
    # Получаем метаданные из Firestore
    video_data = get_video_link(video_id)
    if video_data:
        expiration_time = video_data["expiration_time"]
        if datetime.now(timezone.utc) > expiration_time:
            # Если время истекло, удаляем аудио из GCS
            delete_audio_from_gcs(audio_file_name)
            return "Audio file deleted from GCS"
    return "Audio file is still valid"