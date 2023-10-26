from common.file_storage import FileStorage, DropboxClient
from common.gai_client import MusicGenClient, BarkClient, Llama2Client, ChatGPT
from vega.settings import GAI_URL, TMP_PATH, DROPBOX_FOLDER, DROPBOX_API_KEY, OPENAI_KEY


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
		return ChatGPT(
			OPENAI_KEY,
			"poet"
		)

	@staticmethod
	def provide_file_storage() -> FileStorage:
		return DropboxClient(
			token=DROPBOX_API_KEY,
			folder=DROPBOX_FOLDER
		)
