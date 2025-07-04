## MoviePy : 동영상 편집을 위한 라이브러리
from moviepy import VideoFileClip

# input_video_path = "./source/video/test.mp4"
# output_audio_path = "./source/audio/test.wav"
from config import VIDEO_FILE, AUDIO_FILE



print('1. [영상에서 오디오 추출] 시작')

def extract_audio_moviepy(VIDEO_FILE, AUDIO_FILE):

    video = VideoFileClip(VIDEO_FILE)

    ## 비디오에서 오디오 추출

    video.audio.write_audiofile(AUDIO_FILE, fps=16000, nbytes=2, codec='pcm_s16le')

    ## 리소스 해제
    video.close()

## 함수 호출
extract_audio_moviepy(VIDEO_FILE, AUDIO_FILE)

print('2. [영상에서 오디오 추출] 완료')