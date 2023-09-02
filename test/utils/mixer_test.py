import typing

import unittest

from src.python.vega.utils.mixer.audiomix import AudioMix


class TestAudioMixer(AudioMix):
    def __init__(self):
        super().__init__("/home/inkoops/Temp/1-sept-2023")


class AudioMixerTest(unittest.TestCase):
    def test_functionality(self):
        test_audio = TestAudioMixer()
        test_audio._mix(
            "/home/inkoops/Downloads/Untitled1.wav",
            "/home/inkoops/Downloads/Untitled.wav",
            test_audio._generate_filepath())
