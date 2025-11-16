# cps/audio_helper.py
import os

AUDIO_SUBDIR = os.environ.get("CW_AUDIO_SUBDIR", "audio")
AUDIO_EXTS = (".mp3", ".m4a", ".m4b", ".flac", ".wav", ".ogg")


def get_audio_dir(book_path: str) -> str | None:
	if not book_path:
		return None
	audio_dir = os.path.join(book_path, AUDIO_SUBDIR)
	if os.path.isdir(audio_dir):
		return audio_dir
	return None


def get_audio_files(book_path: str) -> list[str]:
	audio_dir = get_audio_dir(book_path)
	if not audio_dir:
		return []
	files = []
	for name in os.listdir(audio_dir):
		if name.lower().endswith(AUDIO_EXTS):
			files.append(name)
	return sorted(files)
