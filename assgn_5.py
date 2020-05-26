import os
import pickle


class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()
    def __str__(self):
        return ('key "{0}" not found.  Available keys: '
                '({1})'.format(self.key, ', '.join(self.keys)))

class ConfigPickleDict(dict):

    config_dir = '/Users/dom/PycharmProjects/Udemy_OOP/OOPython_5/configs/'
    # config_dir = './configs/'

    def __init__(self, pickle_name):
        self._filename = os.path.join(ConfigPickleDict.config_dir, pickle_name)
        if not os.path.isfile(self._filename):
            with open(self._filename, 'wb') as fh:
                pickle.dump({}, fh)

        with open(self._filename, 'wb+') as fh:
            pkl = pickle.load(fh)
            self.update(pkl)

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'wb') as fh:
            print(pickle.dump(self, fh))

cd = ConfigPickleDict('config_file')
cd['key'] = 'value'
print (cd)