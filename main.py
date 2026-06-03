from src.transcript import get_transcript
from src.summarizer import generate_summary


def main():
    print("YouTube Video Summarizer")

    video_id = input("Enter Video ID: ")

    transcript = get_transcript(video_id)

    summary = generate_summary(transcript)

    print("\nSummary:\n")
    print(summary)


if __name__ == "__main__":
    main()