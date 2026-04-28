import os
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests


INVALID_FILENAME_CHARS = '\\/:*?"<>|'


class _ImageSrcParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "img":
            return
        for key, value in attrs:
            if key == "src" and value:
                self.sources.append(value)
                return


def clean_filename(filename: str) -> str:
    cleaned = filename
    for char in INVALID_FILENAME_CHARS:
        cleaned = cleaned.replace(char, "")
    return cleaned


def extract_image_urls(html: str, base_url: str) -> list[str]:
    parser = _ImageSrcParser()
    parser.feed(html)
    return [urljoin(base_url, src) for src in parser.sources]


def filename_from_url(url: str) -> str:
    filename = os.path.basename(urlparse(url).path)
    return clean_filename(filename or "image")


def download_images(url: str, folder: str | Path, timeout_seconds: int = 30) -> list[Path]:
    destination = Path(folder)
    destination.mkdir(parents=True, exist_ok=True)

    response = requests.get(url, timeout=timeout_seconds)
    response.raise_for_status()

    saved_files: list[Path] = []
    for image_url in extract_image_urls(response.text, url):
        image_response = requests.get(image_url, timeout=timeout_seconds)
        image_response.raise_for_status()
        save_path = destination / filename_from_url(image_url)
        save_path.write_bytes(image_response.content)
        saved_files.append(save_path)
    return saved_files
