import logic

card = logic.TextCard()
storage = logic.LocalStorageImpl()
storage.save_card(card)
cardAux = storage.load_card(card)
print(card.__dict__)
print(cardAux.__dict__)
