import pandas as pd
df = pd.read_csv('phone_dataset.csv')
models = list(df[df.brand == 'Samsung'].model)
models = [x.lower() for x in models]

filename = 'keyword.csv'
for model in models:
   model = model.lower()
   if 'tab' in model:
      continue
   if 'galaxy' in model:
      print(model)
   # with open(filename, 'a') as f:
   #    f.write(model+'\n')
