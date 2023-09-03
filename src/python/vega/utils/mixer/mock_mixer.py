from pydub import AudioSegment
from utils.mixer.mixer import Mixer


class MockMixer(Mixer):

	def _mix(self, instrumental_path: str, vocal_path: str, output_path: str):

		instrumental = AudioSegment.from_wav(instrumental_path)
		vocal_path = AudioSegment.from_wav(vocal_path)

		output = instrumental.overlay(vocal_path)

		output.export(output_path, format="wav")

