from app.clients.openai_digest import OpenAIClient
from app.services.subtitles_service import download_subtitles

def generate_summary(ai_client: OpenAIClient, video_url: str, subtitles_language: str = 'en', is_audio: bool = False):
    """
    Generate summary from video subtitles
    :param ai_client:
    :param video_url:
    :param subtitles_language:
    :param is_audio:
    :return:
    """
    subtitles_path = download_subtitles(video_url, subtitles_language)

    if not subtitles_path:
        return "Failed to download subtitles."

    # Generate summary using subtitles
    with open(subtitles_path, 'r') as file:
        subtitles = file.read()
        summary_result = ai_client.generate_text_summary(subtitles, subtitles_language)

        if is_audio:
            result = generate_audio_summary(summary_result, subtitles_language)
            print(result)
        else:
            print(summary_result)

def generate_audio_summary(summary_result: str, language: str) -> str:
    """
    Generate audio summary from subtitles
    :param summary_result:
    :param language:
    :return:
    """
    summary = f"Audio summary in {language}: " + summary_result[:100] + "..."  # Truncate to first 100 characters
    return summary

