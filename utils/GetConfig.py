import yaml


class Conf:
    def __init__(self, path='./conf/config.yaml'):
        self.path = path
        self.data = None

    def get_config(self):
        with open(self.path, 'r', encoding="utf-8") as f:
            yml_data = f.read()
            self.data = yaml.load(yml_data, Loader=yaml.FullLoader)

        return self.data


