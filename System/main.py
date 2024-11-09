import torch
from transformers import MarianMTModel, MarianTokenizer
import speech_recognition as sr
from gtts import gTTS
import os

# Load the MarianMT model and tokenizer
model_name = 'Helsinki-NLP/opus-mt-en-es'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Move model to the appropriate device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

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
    print(f"Audio saved as {filename}")
    os.system(f"start {filename}" if os.name == 'nt' else f"xdg-open {filename}")

def live_audio_translation():
    """Capture live audio, translate it, and provide options for output."""
    recognizer = sr.Recognizer()
    print("Listening... Speak English to translate to Spanish.")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print(f"Detected English text: {user_input}")
        
        # Translate detected text
        translated_text = translate_text(user_input)
        
        # Choose output type
        output_choice = input("Translate to (1) text or (2) audio: ").strip()
        if output_choice == '1':
            print(f"Translation: {translated_text}")
        elif output_choice == '2':
            text_to_speech(translated_text)

    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError:
        print("Speech recognition service is unavailable.")

# Main program
input_choice = input("Choose input type - Enter '1' for live audio translation or '2' for manual text input: ").strip()

if input_choice == '1':
    live_audio_translation()
elif input_choice == '2':
    user_input = input("Enter the English text you want to translate: ").strip()
    output_choice = input("Translate to (1) text or (2) audio: ").strip()
    translated_text = translate_text(user_input)
    
    if output_choice == '1':
        print(f"Translation: {translated_text}")
    elif output_choice == '2':
        text_to_speech(translated_text)
