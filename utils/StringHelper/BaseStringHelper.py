from difflib import SequenceMatcher

class BaseStringHelper:

    def __init__(self) -> None:
        super().__init__()

    def remove_accent(self, text):

        """
            Change all accent characters to non-accent characters. E.g. á to a.
        """

        dict_diacritic = {
            'á':'a',
            'é':'e',
            'í':'i',
            'ó':'o',
            'ú':'u',
            'à':'a',
            'â':'a',
            'ê':'e',
            'ô':'o',
            'ã':'a',
            'õ':'o',
            'ç':'c',
            'Á':'A',
            'É':'E',
            'Í':'I',
            'Ó':'O',
            'Ú':'U',
            'À':'A',
            'Â':'A',
            'Ê':'E',
            'Ô':'O',
            'Ã':'A',
            'Õ':'O',
            'Ç':'C',
            'º':'o',
            'ª': 'a'
        }

        for key, value in dict_diacritic.items():
            text = text.replace(key, value)

        return text

    def fix_accent(self, text):
        if 'Ã¿Ã¿O' in text:
            text.replace("Ã¿Ã¿O", 'ÇÃO')
        return text
        
    def limit_string_size (self,text,size):      
        """
            Limits the string size.
            If the string is none, it will return none.
        """

        if text is None:
            return None         
        return text[0:size]
    
    def match_string(self, str1, str2):
        if str1==str2:
            return True
        return False
    
    def similarity_string(self, str1:str, str2:str)->float:
        similarity = 0
        if str1 is not None and\
        str2 is not None:
            similarity = float(SequenceMatcher(None, str1, str2).ratio())
        elif str1 is None and\
        str2 is None:
            similarity = 1
    
        return similarity
    
    def is_subtext_of(self, str1:str, str2:str):
        arr1 = str1.split(" ")
        arr2 = str2.split(" ")
        if len(arr1) > len(arr2):
            arr_bigger  = arr1
            arr_smaller = arr2
        else:
            arr_bigger  = arr2
            arr_smaller = arr1

        is_subtext = True
        
        for e in arr_bigger:
            is_subtext = is_subtext and (e in arr_smaller)
            if not is_subtext:
                return False
        
        return is_subtext

    def delete_entities(self, text:str):
        entities = [
            "&",
            " ",
            "<",
            ">",
            "&",
            '"',
            "'",
            "¢",
            "£",
            "¥",
            "€",
            "©",
            "®",
            "§",
            "¨",
            "»",
            "$"
        ]   
        cleantext:str
        cleantext = text
        for entity in entities:
            cleantext = cleantext.replace(entity, ' ')
        return cleantext
    
    def cut_percentage_text(self, start_percent:float, end_percent:float, text:str)->str:
        
        if start_percent > 1:
            start_percent = float(start_percent/100)
        
        if end_percent > 1:
            end_percent = float(end_percent/100)
        
        text_size = len(text)

        return_text = text[int(text_size*start_percent):int(text_size*end_percent)]

        return return_text
    def levenshtein_distance(self, s_dirty, t_dirty):
        s = self.remove_accent(s_dirty)
        t = self.remove_accent(t_dirty)
        # for all i and j, d[i,j] will hold the Levenshtein distance between
        # the first i characters of s and the first j characters of t
        m, n = len(s), len(t)
        # set each element in d to zero
        d = [[0 for x in range(n)] for y in range(m)]  
    
        
        # source prefixes can be transformed into empty string by
        # dropping all characters
        for i in range(0,m):
            d[i][0] = i
        
        # target prefixes can be reached from empty source prefix
        # by inserting every character
        for j in range(0,n):
            d[0][j] = j
    
        for j in range(0,n):
            for i in range(0,m):
                if s[i] == t[j]:
                    substitutionCost = 0
                else:
                    substitutionCost = 1

                d[i][j] =   min(
                                d[i-1][j] + 1,                  # deletion
                                d[i][j-1] + 1,                  # insertion
                                d[i-1][j-1] + substitutionCost  # substitution
                            ) 
        
        return d[m-1][n-1]
        
    def remove_spaced_text(self, text, number_spaces = 0):
        """
            This function will remove excess spaces from a string
            1 2 3 4 5 => 12345 (number_spaces=1)
            a b  c => ab c (number_spaces=1)
        """
        if number_spaces <= 0 or len(text) == 0 or len(text) <= number_spaces:
            return text
        text = text.strip()
        space = ' ' * number_spaces
        arr = []
        for s in text.split(space):
            if(len(s) > 0):
                arr.append(s)
            else:
                arr.append(space)

        return ''.join(arr)

    def replace_string(self, s:str, element_to_replace:str, substitute:str):
        try:
            return s.replace(element_to_replace, substitute)
        except Exception as e:
            raise Exception(str(e))