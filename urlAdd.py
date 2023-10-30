
def addurl(url):
    """
    Returns the converted url if the url does not have proper url string
    """
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    return url