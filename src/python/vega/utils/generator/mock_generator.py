import time

from apps.core.models import QueryParams, GenerationRequest, Song
from utils.generator.generator import Generator


class MockGenerator(Generator):

	def generate(self, query_params: QueryParams, request: GenerationRequest) -> Song:
		self._update_status(request, GenerationRequest.Status.instrumental)
		request.status = GenerationRequest.Status.instrumental.value
		request.save()
		time.sleep(5)  # GENERATING INSTRUMENTAL
		self._update_status(request, GenerationRequest.Status.lyrics)
		request.status = GenerationRequest.Status.lyrics.value
		request.save()
		time.sleep(5)  # GENERATING LYRICS
		self._update_status(request, GenerationRequest.Status.vocal)
		request.status = GenerationRequest.Status.vocal.value
		request.save()
		time.sleep(5)  # GENERATING VOCAL
		self._update_status(request, GenerationRequest.Status.mix)
		time.sleep(5)  # GENERATING MIX

		song = Song(
			title="Echoes in the Night",
			audio="https://www.dropbox.com/scl/fi/pct36wssa6ug85m8wdjtd/1693508148.414699.mp3?rlkey=6j41bktwj5bjltg0umyvak358&dl=0&raw=1",
			lyrics="""
(Verse 1)
In the city streets, the lights are bright
But they can't illuminate the darkness of my night
I'm lost in the shadows, can't find my way
My heart is heavy, my soul is gray

(Chorus)
Oh, the melody of sadness fills the air
A violin's cry, a piano's prayer
The drums beat slow, a funeral march
My heart is breaking, my spirit's crash

(Verse 2)
I thought I had it all, fame and wealth
But it's just an illusion, a fragile health
I'm chasing dreams, but they're hard to catch
I'm searching for a love that's out of reach

(Chorus)
Oh, the melody of sadness fills the air
A violin's cry, a piano's prayer
The drums beat slow, a funeral march
My heart is breaking, my spirit's crash

(Bridge)
I try to hide, but can't escape
The pain that's deep, the hurt that's real
I'm searching for a way to heal
But it's hard to find, it's hard to feel

(Verse 3)
I thought I had control, but it's slipping away
I'm losing myself, in every way
I'm trying to hold on, but it's too late
I'm falling apart, it's my fate

(Chorus)
Oh, the melody of sadness fills the air
A violin's cry, a piano's prayer
The drums beat slow, a funeral march
My heart is breaking, my spirit's crash

(Outro)
So I'll play this song, over and over
A sad melody, a sorrowful tune
I'll dance in the dark, with tears in my eyes
For the pain that I feel, it's my only disguise.
""",
			cover="https://www.dropbox.com/scl/fi/65jq2zoqg5l3o203aprq4/1693508148.414699.png?rlkey=bfngqxunb01xm86dam00xe3o8&dl=0&raw=1",
		)
		song.save()
		request.song = song

		self._update_status(request, GenerationRequest.Status.done)

