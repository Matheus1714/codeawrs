from utils.StringHelper.BaseStringHelper import BaseStringHelper
from utils.DateUtil.DateUtil import DateUtil

class BaseDTO:

    string_util = BaseStringHelper()
    date_util = DateUtil()
    
    def get_lower_upper_string_from_dict(self, dict, key, size, variable_init):

        if key.upper() in dict:
            return self.string_util.limit_string_size(dict[key.upper()], size)
        elif key.lower() in dict:
            return self.string_util.limit_string_size(dict[key.lower()], size)
        else:
            return self.string_util.limit_string_size(variable_init, size)

    def get_lower_upper_string_from_dict_no_size(self, dict, key, variable_init):
        if key.upper() in dict:
            return dict[key.upper()]
        elif key.lower() in dict:
            return dict[key.lower()]
        else:
            return variable_init

    def get_lower_upper_integer_from_dict(self, dict, key, variable_init):
        if key.upper() in dict:
            return dict[key.upper()]
        elif key.lower() in dict:
            return dict[key.lower()]
        else:
            return variable_init

    
    def get_lower_upper_float_from_dict(self, dict, key, variable_init):
        if key.upper() in dict:
            return dict[key.upper()]
        elif key.lower() in dict:
            return dict[key.lower()]
        else:
            return variable_init

    def get_lower_upper_date_from_dict(self, dict, key, variable_init):
        date_util = DateUtil()
        if key.upper() in dict:
            try:
                return_value = date_util.str_to_date(dict[key.upper()])
                if return_value is None:
                    raise(BaseException('Not date'))
            except:
                return_value = date_util.str_to_date_written(dict[key.upper()])
                if return_value is None:
                    raise(BaseException('Not date'))
        elif key.lower() in dict:
            try:
                return_value = date_util.str_to_date(dict[key.lower()])
                if return_value is None:
                    raise(BaseException('Not date'))
            except:
                return_value = date_util.str_to_date_written(dict[key.lower()])
                if return_value is None:
                    raise(BaseException('Not date'))
        else:
            return_value = variable_init
        return return_value 

    
    def get_lower_upper_boolean_from_dict(self, dict, key, variable_init):
        if key.upper() in dict:
            return dict[key.upper()]
        elif key.lower() in dict:
            return dict[key.lower()]
        else:
            return variable_init

    def value_or_none(self, my_dict:dict, my_value:str):
        if my_value in my_dict:
            return my_dict[my_value]
        return None
        
    def get_lower_upper_from_dict(self, dict, key, variable_init):
        if key.upper() in dict:
            return dict[key.upper()]
        elif key.lower() in dict:
            return dict[key.lower()]
        else:
            return variable_init
