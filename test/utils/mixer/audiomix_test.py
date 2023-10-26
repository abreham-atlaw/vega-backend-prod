import unittest

from utils.mixer.audiomix import AudioMix


class AudioMixTest(unittest.TestCase):

	def test_functionality(self):

		mixer = AudioMix()
		outpath = mixer.mix(
			"/home/abreham/Projects/TeamProjects/Vega/Server/vega-backend/temp/music/tmpzr1z578j.wav",
			"/home/abreham/Projects/TeamProjects/Vega/Server/vega-backend/temp/music/tmpqb60tvg3.wav"
		)
		print(outpath)

