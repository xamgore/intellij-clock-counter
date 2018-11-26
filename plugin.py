from requests import get


class Plugin:
    """
    :type name : str
    :type totalVotes : int
    :type totalRating : float
    :type downloadsCount : int
    """


    def __init__(self, data):
        self.name = data['name']
        self.totalVotes = data['totalVotes']
        self.totalRating = data['totalRating']
        self.downloadsCount = data['downloadsCount']


    def __repr__(self):
        return 'Plugin({}, votes={}, rating={}, downloads={})' \
            .format(self.name, self.totalVotes, self.totalRating, self.downloadsCount)


    @staticmethod
    def load(plugin_id: int):
        url = 'https://plugins.jetbrains.com/plugin/getPluginInfo?pluginId=%s'
        return Plugin(get(url % plugin_id).json())


    def __stringify(self, pad_title, pad_count, stored_plugin: 'Plugin'):
        loads_diff = self.downloadsCount - stored_plugin.downloadsCount
        loads_diff = (' +%d' % loads_diff if loads_diff else '').rjust(4)

        title = '{0: <{pad}}' \
            .format(self.name + ':', pad=pad_title)
        loads = '{load_icon}{count: <{pad}}{loads_diff}' \
            .format(count=self.downloadsCount, load_icon='\u21ca', pad=pad_count, loads_diff=loads_diff)
        rates = '{star_icon}{rating}' \
            .format(rating=self.totalRating, star_icon='\u2729')
        votes = '{human_icon}{votes}' \
            .format(votes=self.totalVotes, human_icon='\ua19c')

        return '{}  {}  {}  {}'.format(title, loads, rates, votes)


    @staticmethod
    def stringify(plugins, stored_plugins):
        pad_title = 1 + max(len(pl.name) for pl in plugins.values())
        pad_count = max(len(str(pl.downloadsCount)) for pl in plugins.values())
        to_string = lambda pair: pair[1].__stringify(pad_title, pad_count, stored_plugins[pair[0]])
        return '\n'.join(map(to_string, plugins.items()))


    @property
    def data(self):
        return self.__dict__
