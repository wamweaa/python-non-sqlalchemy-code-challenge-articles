class Article:
    all = []

    def __init__(self, author, magazine, title):

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        self._magazine = magazine

    @property
    def title(self):
        return self._title

    def set_title(self, title):
        raise AttributeError("Cannot change the title after the article is instantiated.")

    title = property(fget=lambda self: self._title, fset=set_title)

class Author:
    def __init__(self, name='Unknown'):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def set_name(self, name):
        raise AttributeError("Cannot change the name after the author is instantiated.")

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters, inclusive")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")

        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters, inclusive")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1

        return [author for author, count in author_counts.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda magazine: len(magazine.articles()))


