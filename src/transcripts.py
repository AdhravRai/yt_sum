from youtube_transcript_api import YouTubeTranscriptApi


ytt_api = YouTubeTranscriptApi()


def get_transcript(video_id: str) -> str:
    """
    Fetch transcript and return as a single string.
    """

    transcript = ytt_api.fetch(video_id)

    transcript_text = " ".join(
        chunk.text
        for chunk in transcript
    )

    return transcript_text