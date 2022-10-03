import pandas as pd
from pyPollution.main import PollutionData

zp2010 = pd.read_csv("data/zachpom_2010_pm10.csv", sep=";")
zp2020 = pd.read_csv("data/zachpom_2020_pm10.csv", sep=";")


zp2010['Month'] = pd.to_datetime(zp2010['Date'])
zp2010MeanMonth = zp2010.groupby(zp2010['Month'].dt.strftime('%B')).mean()
zp2010MeanMonth['month_order'] = [4, 8, 12, 2, 1, 7, 6, 3, 5, 11, 10, 9]
zp2010MeanMonth.reset_index(inplace=True)
zp2010MeanMonth.set_index('month_order', inplace=True)
zp2010MeanMonth.sort_index(inplace=True)

zp2020['Month'] = pd.to_datetime(zp2020['Date'])
zp2020MeanMonth = zp2020.groupby(zp2020['Month'].dt.strftime('%B')).mean()
zp2020MeanMonth['month_order'] = [4, 8, 12, 2, 1, 7, 6, 3, 5, 11, 10, 9]
zp2020MeanMonth.reset_index(inplace=True)
zp2020MeanMonth.set_index('month_order', inplace=True)
zp2020MeanMonth.sort_index(inplace=True)


# print(zp2020MeanMonth)

plot2010 = PollutionData()
plot2010.plot(x=zp2010MeanMonth.Month,
              y=zp2010MeanMonth.Koszalin, label="Koszalin")
plot2010.plot(zp2010MeanMonth.Month,
              zp2010MeanMonth.Szczecinek, label="Szczecinek")
plot2010.plot(zp2010MeanMonth.Month,
              zp2010MeanMonth.Szczecin, label="Szczecin")
plot2010.ylabel = 'Mean monthly PM10'
plot2010.format('')
plot2010.print()

# plot2020 = PollutionData()
# plot2020.plot(x=zp2020MeanMonth.Month,
#               y=zp2020MeanMonth.Koszalin, label="Koszalin")
# plot2020.plot(zp2020MeanMonth.Month,
#               zp2020MeanMonth.Szczecinek, label="Szczecinek")
# plot2020.plot(zp2020MeanMonth.Month,
#               zp2020MeanMonth.Szczecin, label="Szczecin")
# plot2020.ylabel = 'Mean monthly PM10'
# plot2020.format()
# plot2020.print()

# print(zp2010MeanMonth['Koszalin'].head(1))

# masno.bar(zp2010MeanMonth['Month'].head(3),
#           zp2010MeanMonth['Koszalin'].head(3), label='test')
# masno.format(add_grid=False)
# masno.print()

# wykresy dla poszcegolnych miast
# wykresy dla miesiecy z min i max, przetestuj czy to ma sens
# jeszcze dla 2020!!!!
