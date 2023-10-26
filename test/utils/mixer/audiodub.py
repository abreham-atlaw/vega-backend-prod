import unittest


from utils.mixer.audiodub import AudiodubMixer


class AudiodubMixerTest(unittest.TestCase):

	def test_functionality(self):
		mixer = AudiodubMixer()
		out = mixer.mix(
			"/home/abreham/Projects/TeamProjects/Vega/Server/vega-backend/temp/music/tmpzr1z578j.wav",
			"/home/abreham/Projects/TeamProjects/Vega/Server/vega-backend/temp/music/tmpqb60tvg3.wav"
		)
		print(out)

