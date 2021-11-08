import pickle

from card import Card


def save():
    card = Card("Digital", "4215")

    with open('db/tdc.db', 'wb') as db:
        pickle.dump(card, db)


save()


def load():
    with open('db/tdc.db', 'rb') as db:
        tdc = pickle.load(db)
        print(tdc.toString())


load()
