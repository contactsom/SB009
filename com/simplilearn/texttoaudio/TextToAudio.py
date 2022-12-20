from gtts import gTTS

f = open("simplilearn.txt")
x=f.read()

language="en"
audio=gTTS(text=x,slow=False)
audio.save("simplilearn.mp3")
