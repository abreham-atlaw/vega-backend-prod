import typing

from utils.mixer.mixer import Mixer
from pydub import AudioSegment, effects
import librosa
import noisereduce as nr
import soundfile as sf


class AudiodubMixer(Mixer):

	def _mix(self, instrumental_path: str, vocal_path: str, output_path: str):
		instrumental_path, vocal_path = self.__prepare_inputs(instrumental_path, vocal_path)

		instrumental = AudioSegment.from_file(instrumental_path)
		vocal = AudioSegment.from_file(vocal_path)

		output = instrumental.overlay(vocal, position=2000, gain_during_overlay=-10)
		output.export(output_path, format="wav")

	def __reduce_noise(self, path):
		audio, sr = librosa.load(path)
		reduced_audio = nr.reduce_noise(y=audio, sr=sr)
		output = self._generate_filepath()
		sf.write(output, reduced_audio, sr)
		return output

	def __normalize(self, path):
		raw_audio = AudioSegment.from_file(path)
		normalized_audio = effects.normalize(raw_audio)
		output = self._generate_filepath()
		normalized_audio.export(output)
		return output

	def __prepare_inputs(self, instrumental_path, vocal_path) -> typing.Tuple[str, str]:
		instrumental_path = self.__normalize(instrumental_path)
		vocal_path = self.__normalize(self.__reduce_noise(vocal_path))

		return instrumental_path, vocal_path
