def level_19() -> None:
    print(f"\033[31mLevel 19\033[0m")
    import base64
    import wave
    with open("source/indian.txt", "r") as file:
        text = file.read().replace("\n", "")
    stream = base64.b64decode(text.encode())
    with open("source/indian.wav", "wb") as file:
        file.write(stream)

    with wave.open("source/indian.wav", "rb") as f1:
        with wave.open("source/india_reverse.wav", "wb") as f2:
            f2.setparams(f1.getparams())
            for _ in range(f1.getnframes()):
                f2.writeframes(f1.readframes(1)[::-1])


if __name__ == "__main__":
    level_19()

#  "level_19/indian.txt" shows as follow:
#
# UklGRvyzAQBXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YdizAQBABkAMQAtAAEADQAJA
# BEAEQAJAAkAGQAVABUAEQApAC0AJQAhAD0APQANADUAFQAVAD0AEQA5ADUAGQAlAAj8PQAVABkAE
# ...... ...... ...... ...... ...... ...... ...... ...... ...... ...... ......
# Bj8HPwdABT8BQApABj8BQA9AAT8IQA0/Dj8EQAk/A0AHQAw/EEAPQAM/AkANPw8/AUAAPwBAB0AA
# PwRACEAGPwpADj8JQBA=