import speech_recognition as sr

audio_file = "school02.wav"
r = sr.Recognizer()

# 使用PocketSphinx进行离线语音识别
with sr.AudioFile(audio_file) as source:
    audio_data = r.record(source)

try:
    # 使用PocketSphinx进行离线语音识别
    text = r.recognize_sphinx(audio_data)
    print(text)
except sr.UnknownValueError:
    print("无法识别音频内容")
except sr.RequestError as e:
    print(f"无法连接到PocketSphinx语音识别服务: {e}")
