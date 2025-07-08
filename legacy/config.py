import os


# # c:\course_video\16_ai\ai-model-development\backend\config.py
# print(__file__)

# # c:\course_video\16_ai\ai-model-development\backend
# print(os.path.dirname(__file__))

## 기본 디렉토리
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) ## abspath는 절대 경로

# c:\course_video\16_ai\ai-model-development\backend
# print('BASE_DIR >> ', BASE_DIR)

## 폴더 경로

VIDEO_DIR = os.path.join(BASE_DIR, 'source', 'video')
AUDIO_DIR = os.path.join(BASE_DIR, 'source', 'audio')
SUBTITLE_DIR = os.path.join(BASE_DIR, 'source', 'subtitle')

## 파일명
VIDEO_FILE = os.path.join(VIDEO_DIR, 'test.mp4')
AUDIO_FILE = os.path.join(AUDIO_DIR, 'test.wav')
SUBTITLE_TEXT_FILE = os.path.join(SUBTITLE_DIR, 'test.txt')
SUBTITLE_JSON_FILE = os.path.join(SUBTITLE_DIR, 'test.json')
SUBTITLE_SRT_FILE = os.path.join(SUBTITLE_DIR, 'test.srt')

print('VIDEO_DIR', VIDEO_DIR)
print('VIDEO_FILE', VIDEO_FILE)
print('AUDIO_DIR', AUDIO_DIR)
print('AUDIO_FILE', AUDIO_FILE)
