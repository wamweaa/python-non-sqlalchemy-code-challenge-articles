class Article:
    _all_articles = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article._all_articles.append(self)
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return[article for article in Article._all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines()))

class Magazine:
    _all_magazines = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all_magazines.append(self)

    def articles(self):
        return [article for article in Article._all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def contributing_authors(self):
        # Return a list of authors who have written more than 2 articles for this magazine
        author_counts = {}
        for article in self.articles():
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        return [author for author, count in author_counts.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        # Return the Magazine instance with the most articles
        max_articles = 0
        top_magazine = None
        for magazine in cls._all_magazines:
            num_articles = len(magazine.articles())
            if num_articles > max_articles:
                max_articles = num_articles
                top_magazine = magazine
        return top_magazine