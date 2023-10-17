from utils.mixer.mixer import Mixer
from pydub import AudioSegment, effects
import librosa
import noisereduce as nr
import soundfile as sf

class AudiodubMixer(Mixer):

	def _mix(self, instrumental_path: str, vocal_path: str, output_path: str):
		instrumental = AudiodubMixer._normalize(instrumental_path)
		vocal = AudiodubMixer._normalize(AudiodubMixer._reduce_noise(vocal_path))

		output = instrumental.overlay(vocal, position=2000, gain_during_overlay=0)
		output.export(output_path, format="wav")

	def _reduce_noise(self, path):
		audio, sr = librosa.load(path)
		reduced_audio = nr.reduce_noise(y=audio, sr=sr)
		output = Mixer._generate_filepath()
		sf.write(output, reduced_audio, sr)
		return output

	def _normalize(self, path):
		raw_audio = AudioSegment.from_file(path)
		normalized_audio = effects.normalize(raw_audio)
		output = Mixer._generate_filepath()
		try:
			normalized_audio.export(output)
		except:
			sf.write(output, normalized_audio)
		return output
