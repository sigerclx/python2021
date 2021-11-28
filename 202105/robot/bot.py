import ybc_speech as speech
import ybc_bot as bot

voice =speech.record('2.wav')
text =speech.voice2text(voice)
res =bot.chat(text)
speech.speak(res,3)