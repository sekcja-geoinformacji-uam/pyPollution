# pyPollution

Automatyzacja pracy nad danymi zanieczyszczeń powietrza

_dostępne moduły_:

### PollutionPlotter 
automatyzacja generowania wykresów liniowych, słupkowych i histogramów

`set_style` - ustawia styl zgodny z dostępnymi w matplotlib

`plot`, `hist`, `bar` - wybór rodzaju wykresu (liniowy, histogram, słupkowy)

`format` - formatuje wykres zgodnie ze słownikiem konfiguracyjnym
```
config = {
    "title": "Rozkład PM10 w Szczecinie w 2010",
    "ylabel": "Obserwacje",
    "xlabel": "PM10 (µg/m3)",
    "avgline": None,
    "legend": "upper right",
    "xticks": 0
}
plot = PollutionPlotter()
plot.format(config)
```
`show` - generowanie wykresu

`export` - eksport wykresu do formatu .png
