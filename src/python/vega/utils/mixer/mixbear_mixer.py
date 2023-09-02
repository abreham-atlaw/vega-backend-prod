from utils.mixer.mixer import Mixer
from pydub import AudioSegment


class AudiodubMixer(Mixer):

	def _mix(self, instrumental_path: str, vocal_path: str, output_path: str):
		instrumental = AudioSegment.from_wav(instrumental_path)
		vocal = AudioSegment.from_wav(vocal_path).apply_gain(10)

		output = instrumental.overlay(vocal, position=3000, gain_during_overlay=-5)
		output.export(output_path, format="wav")
