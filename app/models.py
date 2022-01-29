class Sources:
    """
    Sources class to define sources object
    """

    def __init__(self, id, name, description, url, category, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


class Articles:
    """
    Articles class to define articles object
    """

    def __init__(self, author, title, description, url, url_to_Image, published_at, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_Image = url_to_Image
        self.published_at = published_at
        self.content = content