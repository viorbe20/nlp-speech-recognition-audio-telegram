import speech_recognition as sr

audio_file_path = ""

def transcribe_file(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "No se pudo reconocer el audio"
    except sr.RequestError as e:
        return f"Error en la solicitud al servicio de reconocimiento de voz: {e}"


# Call to trasncription function
transcription = transcribe_file(audio_file_path)

print("Transcripción del audio:")
print('-' * len("Transcripción del audio:"))
print(transcription)