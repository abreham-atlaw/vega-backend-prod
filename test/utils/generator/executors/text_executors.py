import unittest




class TextLMTitleExecutorTest(unittest.TestCase):

	def setUp(self) -> None:
		import os
		os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vega.settings")
		import django
		django.setup()

	def test_functionality(self):
		from dependency_injection.lib_providers import LibProviders
		from utils.generator.executors.text import TitleExecutor

		executor = TitleExecutor(
			client=LibProviders.provide_llama2()
		)
		lyrics = """
(Verse 1)
In the haze of a midnight sky,
Our hearts ignite, we're soaring high.
A symphony of dreams collide,
As we dance through the electric night.

(Pre-Chorus)
We're rebels of the cosmic tide,
In this moment, we cannot hide.
Unleash the fire, let it rise,
We're breaking free, no compromise.

(Chorus)
We're the stars, shining bright,
Guiding souls through the darkest night.
With every beat, we come alive,
In this universe, we will survive.

(Verse 2)
Lost in time, we chase the unknown,
Through stardust trails, we're not alone.
The constellations paint the way,
Our voices echo, let them sway.

(Bridge)
We'll paint the sky with neon dreams,
A kaleidoscope of vibrant scenes.
Together we'll rewrite the script,
Our destiny, we won't resist.

(Chorus)
We're the stars, shining bright,
Guiding souls through the darkest night.
With every beat, we come alive,
In this universe, we will survive.

(Outro)
As the dawn breaks, we'll leave our mark,
A symphony of love, a work of art.
Our random lyrics, forever etched,
In the cosmos, our souls are stretched.
"""

		for i in range(5):
			title = executor.generate(
				None,
				lyrics
			)
			self.assertNotEqual(title, "")
