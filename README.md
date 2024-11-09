# Multi-Modal Translator with Text and Speech Translation in NLP

## Project Overview

The Multi-Modal Translator is a user-friendly web-based application designed to translate English input (text or audio) into Spanish. With support for multiple input formats, this project provides output in both text and audio, catering to diverse user needs and enhancing accessibility. The app uses the MarianMT Model for translations, Google Text-to-Speech (gTTS) for audio, and SpeechRecognition for processing audio inputs. Built with Flask, it delivers a seamless experience in a streamlined interface.

## Features

- **Input Options**: Accepts English text, text files (.txt), and audio files.
- **Translation**: Translates English to Spanish using the MarianMT Model.
- **Output Formats**: Provides both text and audio outputs; saves results as text files or plays as audio.
- **User Interface**: A web interface with HTML, CSS, and JavaScript for intuitive navigation.

## How It Works

1. **Input Handling**
   - **Text**: Users can type English text directly.
   - **Audio**: Users upload an audio file, which is transcribed to text.
   - **Text File**: Users upload a .txt file, which is prepared for translation.

2. **Translation Process**
   - Utilizes the `Helsinki-NLP/opus-mt-en-es` model for high-quality English-to-Spanish translations.
   - Breaks down longer sentences to ensure complete translation.

3. **Output Options**
   - **Text**: Translated text displayed in the interface.
   - **Audio**: Translated text is converted to Spanish audio using gTTS.
   - **File**: Saves the translated output as a downloadable .txt file.

## User Interface

The interface, built with HTML and CSS, allows users to easily select input/output options, upload files, and access their translations. JavaScript enables dynamic input handling, enhancing user interaction.

<br>
<img src="https://github.com/karthi-1212/Multi-Modal-Translator-with-Text-and-Speech-Translation-in-NLP/UI - Img/Front - End.png" alt="Times Series img" width="1000" height="400">

## Achievements

This project highlights effective NLP techniques for multi-modal translation, making it a versatile tool for real-world applications. It demonstrates how NLP, Flask, and modern translation models can be combined to create accessible communication tools.

## Conclusion

The Multi-Modal Translator with Text and Speech Translation provides an adaptable solution for translation tasks, showcasing NLP's potential to enhance multilingual communication through practical applications.
