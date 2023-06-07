def convert_url_suitable(string: str):
    return string.lower().replace("_", "-").replace("’", "").replace(" ", "-").replace(":", "")


def convert_title_suitable(string: str):
    return string.replace("®", "").replace("™", "")