
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gasolina = pd.read_csv('gasolina.csv')

sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=gasolina, marker='o', color='purple')

plt.title('Preço da Gasolina em SP - 10 primeiros dias de Julho/2021')
plt.xlabel('Dia')
plt.ylabel('Preço de Venda (R$)')

plt.savefig('gasolina.png')


plt.show()