import typing

import time
from datetime import datetime
import random

from features.authentication.models import VegaUser
from features.core.models import QueryParams, GenerationRequest, Song
from utils.generator.generator import Generator


class MockGenerator(Generator):

	def __generate(self, request: GenerationRequest) -> Song:

		self._update_status(request, GenerationRequest.Status.instrumental)
		request.status = GenerationRequest.Status.instrumental.value
		request.save()

		time.sleep(8)  # GENERATING INSTRUMENTAL
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


		title = random.choice([
			"Dreaming of You",
			"Rise and Shine",
			"Lost  in the Jungle",
			"Moonlight Sonata",
			"Fireworks"
		])

		mock_song = random.choice([
			song
			for song in Song.objects.all()
			# if song.audio not in [
			# 	"https://dl.dropboxusercontent.com/scl/fi/81wlkohwgsj8sqphkimt3/1697636885.5656.wav?rlkey=ig4g88dx5lu0bclvjyitoccf5&dl=0&raw=1"
			# ]
		])

		audio, lyrics = mock_song.audio, mock_song.lyrics

		cover = random.choice([
			"https://dl.dropboxusercontent.com/scl/fi/ogc9g25l9gebvj6r7uj1g/_91259a40-5cf1-4bf0-bcfb-6d450d8525df.jpeg?rlkey=4vkx18bfwkvn854gio174kwm7&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/xgjlkx4sh3g2bnxg3eixu/_e410fab7-e6b1-4089-9b55-b68f24858394.jpeg?rlkey=enkqklcme40zmm7soblw4xgps&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/gxx3bdmhq59uy7fknx3ta/_296dff94-512e-4926-91d8-dc8e0c59310a.jpeg?rlkey=gjpswlh27sc308cg80t3ne35r&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/40rvexwnuebe3ivj8uzv8/_abb99a3e-7bed-4291-a37a-9f4d9b2d6370.jpeg?rlkey=r89d15otwgbagixtwov9hm7yq&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/d00ptbdoyco9cemfw86im/_a4506d91-1859-46e4-950d-f832b3baa55a.jpeg?rlkey=knocj8sa0li1yr1ksg8derfd1&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/0c7kvwyiqx7fn16rvlyhv/_3ccb8f82-5513-4d83-b12a-e674ea6c5e9d.jpeg?rlkey=u1w2woa1zp1b8kceix7iwausi&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/hqojaknkzxs8h4988p6my/_f129b198-2b0c-4f59-a95a-2a27cefa72fc.jpeg?rlkey=m93hxgzd8e3v7skmws0h93ypl&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/te5aof21n7kh5udh5rwh5/_caa7f7aa-59d6-4b17-8985-56f6d65a70e6.jpeg?rlkey=gbw1vob38b2zo2ijntkrwgfea&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/9i3fz4o020og759ji3odj/_e49c8ee0-77f7-4448-bd7f-0a3189edcebf.jpeg?rlkey=cjesrr2p36mer4q8ut76ddhrq&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/4bulr7oqkc2hv0q4z3xzr/_a34afc48-aec4-4625-8dd8-62a2edbf5cbe.jpeg?rlkey=rcgvy8fqyiglimi9g9c3bqmlc&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/azwmi151vnbr8tyz9nnpm/_f3325b15-9b28-4ff2-9308-1cc1a92fafc0.jpeg?rlkey=wm1vp8y6xleicz4gtx7udmsf5&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/qqhb3q6ipdy9d07obht6g/_79557855-b73a-4ffd-8706-0fad7879d846.jpeg?rlkey=zlz16u2y8hqwgmb5tcvudx2ys&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/h4hdnaldml1ldse0ppr7j/_59dd85fa-32ef-4667-bd73-02e4da05d5a2.jpeg?rlkey=g0nxmz1h8026yb76id58gnqfz&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/351cd80hfwyg8wrb1wnsx/_84dc5c25-883c-47f9-8c1f-559a19516ce2.jpeg?rlkey=1hrw7562goqnju29ia2ogwlvk&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/ovhfjpn7420jbhew49889/_4ef53fec-637e-4ccd-834b-a11d089566a1.jpeg?rlkey=sg26w7nu3yf8e7yiivxy90fee&dl=0"
		])

		song = Song(
			title=title,
			audio=mock_song.audio,
			lyrics=mock_song.lyrics,
			cover=cover,
			duration=15.0
		)
		song.save()
		request.song = song

		self._update_status(request, GenerationRequest.Status.done)

		return song

	def generate(self, query_params: QueryParams, request: GenerationRequest) -> Song:
		return self.__generate(request)

	def generate_raw_query(self, query: str, request: GenerationRequest) -> Song:
		return self.__generate(request)

	def _generate_playlist_title(self, songs: typing.List[Song], user: VegaUser) -> str:
		return datetime.now().strftime("%d/%m/%Y")
