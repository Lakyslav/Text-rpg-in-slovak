import re

class DiacriticRemover:
    def __init__(self):
        # Inicializacia mapovania nahradnych znakov
        self.nahradne_znaky = {
            'á': 'a', 'č': 'c', 'ď': 'd', 'é': 'e', 'í': 'i', 'ľ': 'l', 'ĺ': 'l', 'ň': 'n', 'ó': 'o', 'ô': 'o',
            'ŕ': 'r', 'š': 's', 'ť': 't', 'ú': 'u', 'ý': 'y', 'ž': 'z',
            'Á': 'A', 'Č': 'C', 'Ď': 'D', 'É': 'E', 'Í': 'I', 'Ľ': 'L', 'Ĺ': 'L', 'Ň': 'N', 'Ó': 'O', 'Ô': 'O',
            'Ŕ': 'R', 'Š': 'S', 'Ť': 'T', 'Ú': 'U', 'Ý': 'Y', 'Ž': 'Z'
        }
        self.pattern = re.compile('|'.join(self.nahradne_znaky.keys()))

    def remove_diacritics(self, input_string):
        # Metóda na odstránenie diakritiky zo zadaneho reťazca
        return self.pattern.sub(lambda x: self.nahradne_znaky[x.group()], input_string)
