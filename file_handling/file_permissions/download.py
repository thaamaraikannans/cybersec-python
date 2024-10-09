import requests

def file_download():
    filename = "official_kannan.jpg"
    url = "https://www.isolutions.ch/media/gaykld1f/cybersecurity-month-fu-r-mehr-sicherheit.png?format=webp&rxy=0.6729323308270677%2C0.759676970203286&width=1220"
    res = requests.get(url, stream=True)
    with open(filename, "wb") as f:
        for chunk in res.iter_content(chunk_size=1024):
            f.write(chunk)
    return

file_download()