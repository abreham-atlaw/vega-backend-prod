import unittest


from utils.mixer.audiodub import AudiodubMixer


class AudiodubMixerTest(unittest.TestCase):

	def test_functionality(self):
		mixer = AudiodubMixer()
		out = mixer.mix("/tmp/1697100317.78781.wav", "/tmp/1697100246.46386.wav")
		print(out)

