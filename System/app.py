from flask import Flask, render_template, request, send_file
import torch
from transformers import MarianMTModel, MarianTokenizer
import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS
import os

app = Flask(__name__)

# Load the MarianMT model and tokenizer
model_name = 'Helsinki-NLP/opus-mt-en-es'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Move model to the appropriate device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def convert_to_wav(file_path):
    """Convert audio file to .wav format using pydub."""
    audio = AudioSegment.from_file(file_path)
    wav_path = "temp_audio.wav"
    audio.export(wav_path, format="wav")
    return wav_path

def translate_text(user_input):
    """Translate English text to Spanish."""
    inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True).to(device)
    with torch.no_grad():
        translated_tokens = model.generate(**inputs)
    translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translation

def text_to_speech(text, filename="translated_audio.mp3"):
    """Convert text to speech in Spanish."""
    tts = gTTS(text=text, lang='es')
    tts.save(filename)
    return filename

def translate_audio_file(file_path):
    """Detect English text from an audio file and translate it."""
    recognizer = sr.Recognizer()
    if not file_path.endswith(".wav"):
        file_path = convert_to_wav(file_path)
    
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        user_input = recognizer.recognize_google(audio)
        return user_input
    except (sr.UnknownValueError, sr.RequestError):
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_type = request.form.get("input_type")
        output_format = request.form.get("output_format")
        translation_result = None
        translated_audio_path = None
        
        if input_type == "text":
            user_input = request.form["text_input"]
            translation_result = translate_text(user_input)
            
            if output_format == "audio":
                translated_audio_path = text_to_speech(translation_result)

        elif input_type == "audio":
            audio_file = request.files["audio_file"]
            audio_file_path = "uploaded_audio.wav"
            audio_file.save(audio_file_path)
            
            user_input = translate_audio_file(audio_file_path)
            if user_input:
                translation_result = translate_text(user_input)
                
                if output_format == "audio":
                    translated_audio_path = text_to_speech(translation_result)

        return render_template("index.html", 
                               translation=translation_result, 
                               audio_file=translated_audio_path)
    return render_template("index.html")

@app.route("/download_audio")
def download_audio():
    return send_file("translated_audio.mp3", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
