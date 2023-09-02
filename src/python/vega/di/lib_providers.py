from lib.file_storage import FileStorage, DropboxClient
from lib.gai_client import MusicGenClient, BarkClient, Llama2Client
from vega.settings import GAI_URL, TMP_PATH, DROPBOX_FOLDER, DROPBOX_API_KEY


class LibProviders:

	@staticmethod
	def provide_musicgen_client() -> MusicGenClient:
		return MusicGenClient(
			url=GAI_URL,
			out_path=TMP_PATH
		)

	@staticmethod
	def provide_bark_client() -> BarkClient:
		return BarkClient(
			url=GAI_URL,
			out_path=TMP_PATH
		)

	@staticmethod
	def provide_llama2() -> Llama2Client:
		return Llama2Client(
			url=GAI_URL
		)

	@staticmethod
	def provide_file_storage() -> FileStorage:
		return DropboxClient(
			token=DROPBOX_API_KEY,
			folder=DROPBOX_FOLDER
		)