import typing

from utils.mixer.mixer import Mixer
from pydub import AudioSegment, effects
import librosa
import noisereduce as nr
import soundfile as sf


# Define a class named AudiodubMixer that inherits from the Mixer class
class AudiodubMixer(Mixer):

	# Override the _mix method from the Mixer class to mix two audio tracks using pydub
	def _mix(self, instrumental_path: str, vocal_path: str, output_path: str):
		# Prepare the input audio tracks by normalizing and reducing noise
		instrumental_path, vocal_path = self.__prepare_inputs(instrumental_path, vocal_path)

		# Load the instrumental and vocal tracks as AudioSegment objects
		instrumental = AudioSegment.from_file(instrumental_path)
		vocal = AudioSegment.from_file(vocal_path)

		# Overlay the vocal track on top of the instrumental track and export the result
		output = instrumental.overlay(vocal, position=2000, gain_during_overlay=-5)
		output.export(output_path, format="wav")

	# Private method to reduce noise in an audio track using noisereduce
	def __reduce_noise(self, path):
		# Load the audio track using librosa
		audio, sr = librosa.load(path)
		# Reduce noise in the audio track using noisereduce
		reduced_audio = nr.reduce_noise(y=audio, sr=sr)
		# Export the reduced audio track to a new file and return its path
		output = self._generate_filepath()
		sf.write(output, reduced_audio, sr)
		return output

	# Private method to normalize an audio track using pydub.effects.normalize
	def __normalize(self, path):
		# Load the raw audio track as an AudioSegment object
		raw_audio = AudioSegment.from_file(path)
		# Normalize the raw audio track using pydub.effects.normalize
		normalized_audio = effects.normalize(raw_audio)
		# Export the normalized audio track to a new file and return its path
		output = self._generate_filepath()
		normalized_audio.export(output)
		return output

	# Private method to prepare input audio tracks by normalizing and reducing noise
	def __prepare_inputs(self, instrumental_path, vocal_path) -> typing.Tuple[str, str]:
		# Normalize the instrumental track
		instrumental_path = self.__normalize(instrumental_path)
		# Reduce noise in the vocal track and then normalize it
		vocal_path = self.__normalize(self.__reduce_noise(vocal_path))

		return instrumental_path, vocal_path
