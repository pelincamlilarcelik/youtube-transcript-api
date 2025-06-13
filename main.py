from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from youtube_transcript_api import YouTubeTranscriptApi
import time 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/captions")
def get_captions(video_id: str, lang: str = "tr"):
    try:
        time.sleep(2) 
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        return {"captions": transcript}
    except Exception as e:
        return {"error": str(e)}
