import csv
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

lang_counter = Counter()

for response in lang_responses:
    lang_counter.update(response.split(';'))

languages=[]
popularity=[]

for item in lang_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.title("Most common lanuages")
plt.xlabel("# of people")
plt.tight_layout()

plt.show()
