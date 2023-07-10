import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    # Einstellungen für eine authentischere Stimme
    engine.setProperty('pitch', 0.8)  # Verringere die Tonhöhe
    engine.setProperty('rate', 150)  # Erhöhe die Sprechgeschwindigkeit
    engine.setProperty('volume', 0.8)  # Erhöhe die Lautstärke

    # Überprüfe verfügbare Stimmen und wähle eine männliche Stimme aus
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.gender == 'male':
            engine.setProperty('voice', voice.id)
            break

    engine.say(text)
    engine.runAndWait()

text = input("Gib den Text ein, der vorgelesen werden soll: ")
text_to_speech(text)
