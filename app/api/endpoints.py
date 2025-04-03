from fastapi import APIRouter

from app.clients.openai_digest import OpenAIClient
from app.services.summary_service import generate_summary

router = APIRouter()

@router.get("/status")
def bot_status():
    return {"status": "ok"}

@router.get("/video/{platform}/{video_id}/subtitles/{language}")
async def get_video_subtitles(video_url, language: str, ai_client: OpenAIClient):
    """
    Starts the process of downloading subtitles and generatopn summary for a video and returns the status.
    """
    generate_summary(ai_client, video_url, language)
    return {"status": "IN_PROGRESS", "video_url": video_url, "language": language}
