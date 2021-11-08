import pickle

from card import Card


cardls = []
cardls.append(Card("Digital", "4815"))
cardls.append(Card("Libreton Fisica", "0976"))


def save(toSave):

    with open('db/tdc.db', 'wb') as db:
        pickle.dump(toSave, db)


save(cardls)


def load():
    with open('db/tdc.db', 'rb') as db:
        data = pickle.load(db)
    return data


data = load()

for card in data:
    print(card.getData())
