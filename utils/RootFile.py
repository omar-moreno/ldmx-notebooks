
import numpy as np
import uproot

class RootFile:
    """
    """
    def __init__(self):
        self.tree = None

    def open(self, file_path : str, tree_name : str) -> uproot.TTree : 
        """
        """
        self.tree = uproot.open('%s:%s' % (file_path, tree_name))

    def flat_array(self, branch : str, leaf : str) -> np.array: 
        """
        """
        array = self.tree[branch]['%s.%s' % (branch, leaf)].array(library='np')
        return np.array([i for j in array for i in j])

