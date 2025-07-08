import os
from datetime import datetime, timedelta

import whisper
from fastapi import FastAPI, File, UploadFile

## 디렉토리 설정
## 동영상이 저장되는 폴더 :uploads
## SRT 파일이 저장되는 폴더 : output
## FastAPI 실행
UPLOAD_DIR = './uploads'
OUTPUT_DIR = './output'

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

## Whisper 모델 로드
model = whisper.load_model('small')

app = FastAPI()

@app.get('/')
def index():
    return '환영합니다.'

## 요청 URL :/create_subtitle_video
## 요청 method : post
## return :요청 처리됨
@app.post('/create_subtitle_video')
async def create_subtitle_video(file: UploadFile = File(...)):
    print('\n=== 비디오 처리 시작 ===')
    ## video 파일명 지정
    ## temp_video_path = /uploads/temp_video_20250707_1720.mp4
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    temp_video_path = os.path.join(UPLOAD_DIR,f'/temp_video_{timestamp}.mp4')
    # print(temp_video_path)

    ## 업로드 영상 저장
    contents = await file.read()
    ## with문 사용하여 쓰기 작업: wb
    ## 파일 ㅈ경로 및 파일명 : temp_video_path

    with open(temp_video_path, 'wb') as file: ##wb 바이너리
        file.write(contents)

    print('whisper로 자막 추출시작')
    result = model.transcribe(temp_video_path)

    segments = result['segments']

    ## srt 파일 : 파일명 지정
    srt_filename = f'subtitle_{timestamp}.srt'
    srt_path =os.path.join(OUTPUT_DIR, srt_filename)

    ## srt 파일 생성
    ## with문 사용: 쓰기 작업
    with open(srt_path, 'w', encoding='utf-8') as file:
        for i, seg in enumerate(segments, 1):
            start = format_time(seg['start'])
            end = format_time(seg['end'])
            text = seg['text'].strip()

            file.write(f'{i}\n')
            file.write(f'{start} --> {end}\n')
            file.write(f'{text}\n\n')

    return '요청처리됨'

def format_time(seconds):
    '''
    * 초 단위 시간을 SRT 형식 (HH:MM:SS,mm)으로 변환
    '''
    td = timedelta(seconds=seconds)
    hours = int(td.total_seconds() // 3600)
    minutes = int((td.total_seconds() % 3600)// 60)
    seconds = int(td.total_seconds()% 60)
    milliseconds = int((td.total_seconds()% 1) * 1000)

    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}'





