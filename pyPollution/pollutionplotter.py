import matplotlib.pyplot as plt


class PollutionPlotter():
    '''
    add text
    '''

    def __init__(self):
        self._legend_loc = 'upper right'
        self._ylabel = ''
        self._xticks = 45
        self._avgline = 0.0

    @property
    def legend_loc(self) -> str:
        '''omamale'''
        return self._legend_loc

    @property
    def ylabel(self) -> str:
        return self._ylabel

    @property
    def xticks(self) -> int:
        return self._xticks

    @property
    def avgline(self) -> float:
        return self._avg

    @legend_loc.setter
    def legend_loc(self, loc: str) -> None:
        if not isinstance(loc, str):
            raise TypeError('Legend location must be a string')
        self._legend_loc = loc

    @ylabel.setter
    def ylabel(self, ylabel: str) -> None:
        if not isinstance(ylabel, str):
            raise TypeError('Y axis label must be a string')
        self._ylabel = ylabel

    @xticks.setter
    def xticks(self, xticks: int) -> None:
        if not isinstance(xticks, int):
            raise TypeError('X ticks rotation must be an integer')
        self._xticks = xticks

    @avgline.setter
    def avgline(self, avgline: float) -> None:
        self._avgline = avgline

    def plot(self, x, y, label=''):
        plt.plot(x, y, label=label)

    def bar(self, x, y, width, ticks, xlabel, label=''):
        plt.bar(x, y, width=width, label=label)
        plt.xticks(ticks, xlabel)

    def format(self, title='',  add_legend: bool = True, add_grid: bool = True, add_avgline: bool = False) -> None:
        if add_avgline:
            plt.axhline(y=self.avgline, color='red',
                        linestyle='--', linewidth=2, label='Average')

        if add_legend:
            plt.legend(loc=self._legend_loc)

        if add_grid:
            plt.grid()

        plt.ylabel(self._ylabel)
        plt.xticks(rotation=self._xticks)
        plt.title(title)
        plt.tight_layout()

    def print(self) -> None:
        plt.show()

    def save(self, filename: str) -> None:
        if not isinstance(filename, str):
            raise TypeError('Filename must be a string')

        plt.savefig(filename+'.png')

# linia ze srednimi wartosciami
# mozliwosc jej dodania przez boolean
