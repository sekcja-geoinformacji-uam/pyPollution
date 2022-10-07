import matplotlib.pyplot as plt
from IPython.display import display


class PollutionPlotter():
    '''
    Automate 
    '''

    def set_style(self, style: str) -> None:
        '''
        Sets style sheets avaiable in matplotlib.
        '''
        plt.style.use(style)

    def plot(self, *args, **kwargs):
        '''
        Plot y versus x as lines and/or markers
        '''
        plt.plot(*args, **kwargs)

    def bar(self, x, y, width, ticks, xlabel, label=''):
        '''
        Make a bar plot
        '''
        plt.bar(x, y, width=width, label=label)
        plt.xticks(ticks, xlabel)

    def hist(self, *args, **kwargs):
        '''
        Compute and plot a histogram
        '''
        plt.hist(*args, **kwargs)

    def format(self, config: dict) -> None:
        '''
        Sets the multiple for plot based on config dictionary
        '''
        if config["legend"]:
            plt.legend(loc=config["legend"])

        if config["avgline"]:
            plt.axhline(y=config["avgline"], color='red',
                        linestyle='--', linewidth=2, label='Average')

        plt.ylabel(config["ylabel"])
        plt.xlabel(config["xlabel"])
        plt.xticks(rotation=config["xticks"])
        plt.title(config["title"])
        plt.tight_layout()

    def show(self) -> None:
        '''
        Show the plot
        '''
        plt.show()

    def export(self, filename: str) -> None:
        '''
        Export the plot to .png image
        '''
        if not isinstance(filename, str):
            raise TypeError('Filename must be a string')

        plt.savefig(filename+'.png')
