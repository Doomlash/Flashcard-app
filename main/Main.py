import pickle

import logic
from pathlib import Path

print(data_folder)
card = logic.TextCard("titulo2", "pregunta", "respuesta")
print(card.__dict__)
outfile2 = open(data_folder / "card3", "wb")
pickle.dump(card, outfile2)
outfile2.close()

infile=open("card","rb")
card=pickle.load(infile)
infile.close()
print(card.__dict__)