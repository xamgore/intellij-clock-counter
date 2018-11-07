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


    def __stringify(self, pad_title, pad_count):
        title = '{0: <{pad}}' \
            .format(self.name + ':', pad=pad_title)
        loads = '{load_icon}{count: <{pad}}' \
            .format(count=self.downloadsCount, load_icon='\u21ca', pad=pad_count)
        rates = '{star_icon}{rating}' \
            .format(rating=self.totalRating, star_icon='\u2729')
        votes = '{human_icon}{votes}' \
            .format(votes=self.totalVotes, human_icon='\ua19c')

        return '{}  {}  {}  {}'.format(title, loads, rates, votes)


    @staticmethod
    def stringify(plugins):
        pad_title = 1 + max(len(pl.name) for pl in plugins)
        pad_count = max(len(str(pl.downloadsCount)) for pl in plugins)
        return '\n'.join(pl.__stringify(pad_title, pad_count) for pl in plugins)
