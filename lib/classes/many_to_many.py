class Article:
    # This will hold all the articles
    all = []

    def __init__(self, author, magazine, title):
        
        # I'm making the attributes private so that I can only access it in the property method when I want to modify it.
        self._author = author
        self._magazine = magazine
        self._title = title

        # I'm using ValueError to ensure that the correct value according to the conditions is passed. The same applies to TypeError if the type is incorrect.

        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise ValueError("Titles must be between 5 and 50 characters.")
        if not isinstance(author, Author):
            raise TypeError("author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be of type Magazine")

        # appending the articles to both author and magazine
        author.articles().append(self)
        magazine.articles().append(self)
        # Appending all the articles to the all []
        Article.all.append(self)

    # getting 
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    # Setting it by using the setter method so that the authors can be able to be changed
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    # The same applies here
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be of type Magazine")
        self._magazine = value

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Names must be longer than 0 characters")
        self._name = name
        self._articles = []

    # Read only property because the name of the author isn't to be changed
    @property
    def name(self):
        return self._name

    # Show all the articles the author has written
    def articles(self):
        return self._articles

    # A list of magazines that the author has contributed to. If an article is not in magazine, it can be added by using append.
    def magazines(self):
        magazines = []
        for article in self._articles:
            if article.magazine not in magazines:
                magazines.append(article.magazine)
        return magazines
    
    # Creating a new article
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)

        # appending the new article to the original articles
        self._articles.append(article)
        return article

    # adding topics / categories that the author chooses to focus on.
    def topic_areas(self):
        categories = []
        for article in self._articles:
            if article.magazine.category not in categories:
                categories.append(article.magazine.category)
        return categories or None

class Magazine:
    # Using an empty list to store all the magazines
    all_magazines = []

    # Conditions to be met
    def __init__(self, name, category):
        if not isinstance(name, str) or not 2 <= len(name) <= 16:
            raise ValueError("Names must be between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Categories must be longer than 0 characters.")

        self._name = name
        self._category = category
        # Where all the articles will be stored and added to the magazine.
        self._articles = []
        # Adding all the magazines inside the list
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 2 <= len(value) <= 16:
            raise ValueError("Names must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Categories must be longer than 0 characters.")
        self._category = value

    def articles(self):
        return self._articles

    # This will display a list of authors who have contributed in writing for a certain magazine
    def contributors(self):
        contributors = []
        for article in self._articles:
            # adding an author to the contributors list if they aren't there. 
            if article.author not in contributors:
                contributors.append(article.author)
        return contributors

    # The titles of all the articles the author has written
    def article_titles(self):
        titles = []
        for article in self._articles:
            titles.append(article.title)
        return titles or None

    def contributing_authors(self):
        # I'm putting it in a dictionary so that it has a key and a value. Author and article
        authors_count = {}
        for article in self._articles: 
            # This is to find which article is written by an author
            author = article.author
            if author in authors_count: 
                # If an author and their article is already in the authors_count, whenever they write a new article, the article will increment itself by one
                authors_count[author] += 1
            else: #google to see if this can work
                # If the author and their article is not in the count, it will add itself.
                authors_count[author] = 1

        # I'm using a list data type so that it can list all the authors who contributed in writing articles and the item method to count how many articles they have written from authors_count
        contributing_authors = []
        for author, count in authors_count.items():
            # if the author has written more than 2 articles, they will be added to the list and if they have less than 2 articles, they won't be added.
            if count > 2:
                contributing_authors.append(author)
        return contributing_authors or None

    @classmethod
    def top_publisher(cls):
        # This is to check if there are no magazines
        if not cls.all_magazines:  
            return None
        # Initializing magazine to None as default so that when iterating, it can check if there are magazines
        max_magazine = None
        # checking how many articles are there / getting the number.
        for magazine in cls.all_magazines: 
            articles_count = len(magazine.articles())

        return max_magazine