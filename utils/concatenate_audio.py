import string

from pydub import AudioSegment


class Concatenate:

    def __init__(self):
        pass

    @staticmethod
    def add_files(audio_files: AudioSegment) -> AudioSegment:
        concatenated_audio = AudioSegment.empty()
        for audio_file in audio_files:
            concatenated_audio += AudioSegment.from_file(audio_file)
        return concatenated_audio

    def export_files(self, files: AudioSegment, output: string):
        return self.add_files(files).export(output)


if __name__ == "__main__":
    a = Concatenate()
    b = ["/Music/(2) Eminem - Lose Yourself [HD] - YouTube.MP3",
         "/Music/01. Amen (Pre Fight Prayer).mp3",
         "/Music/01. Jumpsuit.mp3",
         "/Music/01. Luis Fonsi, Daddy Yankee - Despacito ft. Justin Bieber.mp3"]
    a.export_files(b, "10")
