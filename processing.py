import pandas as pd
import matplotlib.pyplot as plt

#wlkp2010 = pd.read_csv("data/more_stations/wielkopolska_2015.csv")
#wlkp2020 = pd.read_csv("data/wielkopolska_2020.csv")

zp2010 = pd.read_csv("data/zachpom_2010_pm10.csv", sep = ";")
zp2020 = pd.read_csv("data/zachpom_2020_pm10.csv", sep = ";")
#zp2010 = zp2010.set_index("Date")
#zp2020 = zp2020.set_index("Date")
#zp2010_szczecin = zp2010[['Date','Szczecin']]
#zp2010_szczecin = zp2010_szczecin.set_index('Date')

#zp2010_szczecinek = zp2010[['Date','Szczecinek']]
#zp2010_szczecinek = zp2010_szczecinek.set_index('Date')

zp2010['Month'] = pd.to_datetime(zp2010['Date'])

zp2010MeanMonth = zp2010.groupby(zp2010['Month'].dt.strftime('%B')).mean()
zp2010MeanMonth['month_order'] = [4, 8, 12, 2, 1, 7, 6, 3, 5, 11, 10, 9]
zp2010MeanMonth.reset_index(inplace = True)
zp2010MeanMonth.set_index('month_order', inplace = True)
zp2010MeanMonth.sort_index(inplace = True)

plt.plot(zp2010MeanMonth.Month, zp2010MeanMonth.Koszalin, label = 'Koszalin')
plt.plot(zp2010MeanMonth.Month, zp2010MeanMonth.Szczecinek, label = 'Szczecinek')
plt.plot(zp2010MeanMonth.Month, zp2010MeanMonth.Szczecin, label = 'Szczecin')
plt.legend(loc="upper right")
plt.ylabel('Średnie miesięczne stęzenie PM10')
plt.xticks(rotation = 45)
plt.show()


#print(zp2010.groupby(zp2010['Date'].dt.strftime('%B'))['Szczecin'].mean())
#print(zp2010_szczecin)