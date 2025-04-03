import os
from typing import Callable
from urllib.parse import urlparse
import yt_dlp as youtube_dl


def download_subtitles(video_url: str, language: str) -> str | None:
    """
    Download video subtitles from identified platform
    :param language:
    :param video_url:
    :return:
    """
    platform, downloader = __parse_platform(video_url)

    if downloader:
        return downloader(video_url, language)
    else:
        print(f"No downloader found for {platform} platform.")

def __parse_platform(video_url) -> tuple[str, Callable[[str, str], str | None]] | None:
    """
    Parse the platform from the video URL and return platform and the download function
    :param video_url:
    :return:
    """
    parsed_url = urlparse(video_url)
    if "youtube.com" in video_url or "youtu.be" in parsed_url.netloc:
        return "youtube", __download_youtube_subtitles

def __download_youtube_subtitles(video_url: str, subtitle_language: str) -> str | None:
    """
    Download subtitles from YouTube video
    :param video_url:
    :param subtitle_language:
    :return:
    """
    ydl_opts = {
        'writesubtitles': True,
        'subtitleslangs': [subtitle_language],
        'skip_download': True,
        'outtmpl': '/path/to/save/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegSubtitlesConvertor',
            'format': 'srt',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([video_url])
        if result == 0:
            info_dict = ydl.extract_info(video_url, download=False)
            subtitle_path = os.path.join('/path/to/save/', f"{info_dict['title']}.{subtitle_language}.srt")
            return subtitle_path
        else:
            return None