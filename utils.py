class Utils:
    @staticmethod
    def str_to_pairs(string):
        counter_key_val, counter_item = 0,0
        pairs = [[''] * 2 for _ in range(5)]
        for char in string:
            if char == ';':
                counter_item += 1
                counter_key_val = 0
                continue
            elif char == ':':
                counter_key_val = 1
                continue
            pairs[counter_item][counter_key_val] += char

        return pairs

    @staticmethod
    def remove_str_artefacts(string):
        string = string.replace('\n', "")
        string = string.replace("'", "")
        string = string.replace(" ", "")
        string = string.replace(",", "")
        string = string.replace(".", "")
        string = string.replace("/", "")
        string = string.replace("\\", "")
        return string[string.index('{') + 1: string.index('}')]
    
    @staticmethod
    def query_to_dict(string):
        string = Utils.remove_str_artefacts(string)
        pairs = Utils.str_to_pairs(string)
        return {key: val for key, val in pairs}

    @staticmethod
    def minimum_mutations(source, typed, limit):
        if typed == source:
            return 0
        if limit < 0:
            return 0
        if source == "":
            return len(typed)
        if typed == "":
            return len(source)
        if typed[0] == source[0]:
            return Utils.minimum_mutations(typed[1:], source[1:], limit)
        else:
            add = 1 + Utils.minimum_mutations(source[0] + typed, source, limit - 1)
            remove = 1 + Utils.minimum_mutations(typed[1:], source, limit - 1)
            substitute = 1 + Utils.minimum_mutations(source[0] + typed[1:], source, limit - 1)
            return min(add, remove, substitute)

    @staticmethod
    def closest_finder(string, arr):
        lengths = []
        for candidate in arr:
            if not candidate:
                continue
            lengths.append(Utils.minimum_mutations(string, candidate, 999))
        return lengths.index(min(lengths))




