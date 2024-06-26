class Utils:
    
    @staticmethod
    def str_to_pairs(str):
        counter_key_val, counter_item = 0,0
        pairs= [[''] * 2 for _ in range(5)]
        for char in str:
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
    def remove_str_artefacts(str):
        str = str.replace('\n', "")
        str = str.replace("'", "")
        str = str.replace(" ", "")
        str = str.replace(",", "")
        str = str.replace(".", "")
        return str[str.index('{') + 1 : str.index('}')]
    
    @staticmethod
    def query_to_dict(str):
        str = Utils.remove_str_artefacts(str)
        pairs = Utils.str_to_pairs(str)
        dict = {key : val for key, val in pairs}
        return dict