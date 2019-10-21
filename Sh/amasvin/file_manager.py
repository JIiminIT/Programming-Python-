import pickle

class FileManager():

    def __init__(self, filename):
        self.filname = filename

    def save(self,data):
        with open(self.filname,"wb") as f:
            pickle.dump(data,f)

    def load(self):
        try:
        with open(self.filname, "rb") as f:
            data = pickle.load(f)

        except FileNotFoundError:
            raise FileNotFoundError

        return data
