import wave

w = wave.open("message.wav", "rb")
p = open("pic.png","w+b")
binary_data = w.readframes(w.getnframes())
w.close()

newFileByteArray = bytearray(binary_data)

p.write(newFileByteArray)
print("hello")
