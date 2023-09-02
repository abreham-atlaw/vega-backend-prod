from utils.concatenate_audio import Concatenate
from utils.mixer.mixer import Mixer


class MockMixer(Mixer):

	def _mix(self, instrumental_path: str, vocal_path: str, output_path: str):
		concatenate = Concatenate()
		concatenate.export_files(
			[
				instrumental_path,
				vocal_path
			],
			output_path
		)
