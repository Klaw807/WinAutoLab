from winautolab.image_download import clean_filename, extract_image_urls, filename_from_url


def test_clean_filename_removes_windows_invalid_characters():
    assert clean_filename('a<>:"/\\\\|?*b') == "ab"


def test_extract_image_urls_resolves_relative_and_absolute_paths():
    html = '<img src="/a.png"><img src="https://example.com/b.jpg">'
    urls = extract_image_urls(html, "https://site.test/post")
    assert urls == ["https://site.test/a.png", "https://example.com/b.jpg"]


def test_filename_from_url_uses_url_path_basename():
    assert filename_from_url("https://example.com/path/image.jpg?x=1") == "image.jpg"

