import yaml


class Datas:
    def get_data(self, filename):
        with open(f'../data/{filename}.yml') as f:
            return yaml.safe_load(f)