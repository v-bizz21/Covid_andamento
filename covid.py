import pandas as pd
from datetime import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
#generating timestamps and preparing them for iteration
dates = pd.date_range('2020-02-24', '2020-12-30')
print(dates)
i = 0
sd = []
for x in range (0, 311):
    stamp = dates[i]
    str(stamp)
    stamp.strftime('%Y-%m-%d')
    sa = stamp.strftime('%Y%m%d')
    i = i + 1
    sd.append(sa)
#print(sd)
#iteration to open multiple csv files
list2 = []
list2 = sd
df0 = pd.DataFrame()
k = 0
for x in range (0, 311):
    stamp = sd[k]
    frame = pd.read_csv(r'C:\Users\utente\dpc-covid19-ita-andamento-nazionale-%s.csv' % stamp)
    df0 = df0.append(frame)
    k = k + 1
#df0['tamponi_giornalieri'] = df0['tamponi'].shift(-1) - df0['tamponi']
print(df0.head())
print(df0.tail())
print(df0.describe())
print(df0.columns)
#plotting multiple lines in one graph
plt.figure(figsize= (12, 6))
plt.grid(True)
plt.title( "Covid- 19 in Italy" , size = 20 )
sns.color_palette()
sns.set_style('darkgrid')
plt_str = sns.lineplot(x = df0.data, y = df0.ricoverati_con_sintomi, data = df0, legend = 'brief')
sns.lineplot(x = df0.data, y = df0.terapia_intensiva, legend='brief', palette='pastel')
sns.lineplot(x = df0.data, y = df0.deceduti)
plt.legend(labels=['Totale ricoverati con sintomi', 'Totale terapia intensiva', 'Totale decessi'])
serie = df0['data']
curr_month = None
tickpos = []
ticklabel = []
z = 0
for idx in serie:
    # Parse datetime and reformat label as desired
    dateval = dates[z]
    str(dateval)
    month = dateval.strftime('%b')
    z = z + 1
    # Clunky filter for identifying the first record for each month
    # Good enough for a proof-of-concept but consider revising.
    if month != curr_month:
        # We want this position, so stash its index and the month name
        tickpos.append(idx)
        ticklabel.append(month)

        curr_month = month

plt_str.set_xticks(tickpos)
plt_str.set_xticklabels(ticklabel, rotation=45)
plt.ylabel('Casi')
plt.xlabel('Data')
plt.show()
