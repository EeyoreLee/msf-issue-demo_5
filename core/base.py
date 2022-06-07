import pandas as pd


class DFA(object):  # TODO the implement about DFA could refactor by c++ and pybind
    """an implement about Deterministic Finite Automaton for sensitive word detection
        It has the time complexity of O(n)

    Args:
        object (_type_): python base object
    """    

    def __init__(self) -> None:
        """Initialize keyword forest and delimit
        """        
        self.chains = {}
        self.delimit = '\x00'
        self.mode = None  # TODO optional[ loger_first | shorter_first | keep_all ] Currently longer_first

    def clean_all(self):
        self.chains = {}

    def add(self, keyword, prop=None):
        if keyword == '':
            return

        chains = self.chains
        for i in range(len(keyword)):
            if keyword[i] in chains:
                chains = chains[keyword[i]]
            else:
                if not isinstance(chains, dict):
                    break
                for j in range(i, len(keyword)):
                    chains[keyword[j]] = {}
                    leaf_chains = chains
                    chains = chains[keyword[j]]
                leaf_chains[keyword[j]] = {self.delimit: 0, "prop": prop}
                break

        if i == len(keyword) - 1:
            chains[self.delimit] = 0
            chains["prop"] = prop

    def detect(self, text):
        result = []
        i = 0
        while i < len(text):
            start_index = None
            chains = self.chains
            if text[i] not in chains:
                i += 1
                continue
            chains = chains[text[i]]
            start_index = i
            for j in range(i+1, len(text)+1):
                if self.delimit in chains:
                    result.append({"index": start_index, "keyword": text[start_index:j], "prop": chains["prop"]})
                if j == len(text):
                    i += 1
                    break
                if text[j] in chains:
                    chains = chains[text[j]]
                else:
                    i += 1
                    break
        return result

    def parse_text_file(self, path):
        with open(path) as f:
            keywords = f.read().splitlines()
        for kw in keywords:
            self.add(kw)
