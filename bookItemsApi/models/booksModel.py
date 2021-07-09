from bookItemsApi.db import db


class BookItemModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    author = db.Column(db.String(80))
    pages = db.Column(db.Integer)

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def json(self):
        return {'name': self.name, 'author': self.author, 'pages': self.pages}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # Select * from books where name = name limit 1;

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
