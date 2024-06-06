class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

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

    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise ValueError("Cannot change the title after the article is instantiated.")
        elif isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters, inclusive.")


class Author:
    def __init__(self, name='Unknown'):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise ValueError("Cannot change the name after the author is instantiated.")
        elif isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters, inclusive.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        if not self.articles():
            return None
        author_counts = {}
        for article in self.articles():
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1

        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles()), default=None)