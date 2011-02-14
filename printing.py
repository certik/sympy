class TableForm(object):

    def __init__(self, data):
        self._data = data

    def __str__(self):
        s = ""
        for l in self._data:
            s += " ".join([str(x) for x in l]) + "\n"
        return s

class MatrixForm(object):

    def __init__(self, data):
        self._data = data

    def __str__(self):
        s = ""
        for l in self._data:
            s += "[ " + " ".join([str(x) for x in l]) + " ]\n"
        return s
