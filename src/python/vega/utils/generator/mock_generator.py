import time

from apps.core.models import QueryParams, GenerationRequest, Song
from utils.generator.generator import Generator


class MockGenerator(Generator):

	def __generate(self, request: GenerationRequest) -> Song:
		self._update_status(request, GenerationRequest.Status.instrumental)
		request.status = GenerationRequest.Status.instrumental.value
		request.save()
		time.sleep(15)  # GENERATING INSTRUMENTAL
		self._update_status(request, GenerationRequest.Status.lyrics)
		request.status = GenerationRequest.Status.lyrics.value
		request.save()
		time.sleep(8)  # GENERATING LYRICS
		self._update_status(request, GenerationRequest.Status.vocal)
		request.status = GenerationRequest.Status.vocal.value
		request.save()
		time.sleep(9)  # GENERATING VOCAL
		self._update_status(request, GenerationRequest.Status.mix)
		time.sleep(8)  # GENERATING MIX

		song = Song(
			title="Running the Game",
			# audio="https://www.dropbox.com/scl/fi/pct36wssa6ug85m8wdjtd/1693508148.414699.mp3?rlkey=6j41bktwj5bjltg0umyvak358&dl=0&raw=1",
			audio="https://www.dropbox.com/scl/fi/qbb7zl2iotvwr48p218h3/1693668027.065475.mp3?rlkey=ux9yn4282i8s20neofa6n07ub&dl=0&raw=1",
			lyrics="""
(Verse 1)
Verse 1:
I'm on the grind, 24/7, 365
My flow's so sick, it's contagious, you can't deny
The heavy drums and synth pads, they're taking me higher
I'm on a roll, ain't no stoppin', I'm on fire

Chorus:
I'm running the game, ain't no one gonna stop me
My rhymes so sharp, they'll leave you in a coffin, so gruesome
I'm the king of the throne, don't you forget it
My flow's like a drill, it'll leave you in a pit

Verse 2:
I'm lighting up the night, like a dark and gritty dream
My bars so tight, they'll leave you in a scheme
I'm on a mission, ain't no time for no games
I'm taking over, ain't no one gonna claim my fame

Chorus:
I'm running the game, ain't no one gonna stop me
My rhymes so sharp, they'll leave you in a coffin, so gruesome
I'm the king of the throne, don't you forget it
My flow's like a drill, it'll leave you in a pit

Bridge:
I'm the future of hip-hop, ain't no one gonna stop me
My sound's so new, it'll leave you in a frenzy
I'm the boss, ain't no one gonna take my place
I'm running the game, ain't no one gonna take my pace

Chorus:
I'm running the game, ain't no one gonna stop me
My rhymes so sharp, they'll leave you in a coffin, so gruesome
I'm the king of the throne, don't you forget it
My flow's like a drill, it'll leave you in a pit
""",
			cover="https://dl.dropboxusercontent.com/scl/fi/yp5goz0c3f9bezv1lrc0x/02.png?rlkey=jh8thuix6kb1n65q8cuy1em16&dl=0&raw=1",
		)
		song.save()
		request.song = song

		self._update_status(request, GenerationRequest.Status.done)

		return song

	def generate(self, query_params: QueryParams, request: GenerationRequest) -> Song:
		return self.__generate(request)

	def generate_raw_query(self, query: str, request: GenerationRequest) -> Song:
		return self.__generate(request)
