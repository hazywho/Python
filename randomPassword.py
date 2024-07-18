import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r"C:\Users\zanyi\Downloads\gefefe.xlsx")
print(df[1])
fig,ax = plt.subplots()
ax.plot(df[1].tolist(),df[1].tolist())
plt.show()