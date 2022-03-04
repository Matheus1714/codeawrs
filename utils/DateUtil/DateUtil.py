import datetime
from pytz import timezone

class DateUtil:


    time_zone:timezone

    months_portuguese_english = {
        "janeiro":"January",
        "fevereiro":"February",
        "março":"March",
        "abril":"April",
        "maio":"May",
        "junho":"June",
        "julho":"July",
        "agosto":"August",
        "setembro":"September",
        "outubro":"October",
        "novembro":"November",
        "dezembro":"December"
    }

    months_portuguese_abrev_english = {
        "jan":"January",
        "fev":"February",
        "mar":"March",
        "abr":"April",
        "mai":"May",
        "jun":"June",
        "jul":"July",
        "ago":"August",
        "set":"September",
        "out":"October",
        "nov":"November",
        "dez":"December"
    }

    months_abrev_english = {
        "jan":"January",
        "feb":"February",
        "mar":"March",
        "apr":"April",
        "may":"May",
        "jun":"June",
        "jul":"July",
        "aug":"August",
        "sep":"September",
        "oct":"October",
        "nov":"November",
        "dec":"December"
    }

    def __init__(self) -> None:
        self.time_zone = timezone('America/Sao_Paulo')


    def date_to_str(self, date_obj):

        """
            Converts date object to string in the formar dd/mm/yyyy
        """

        if isinstance(date_obj, str):
            return date_obj

        return date_obj.strftime('%d/%m/%Y')

    def str_to_date(self, date_str):

        """
            Get a date in the str format and converts it to an date python object.
            Possible formats:
            - dd/mm/yyyy
            - dd/mm/yy
            - dd/mm/yyyy HH:MM
            - dd/mm/yyyy HH:MM:SS
            - dd/mm/yy   HH:MM
            - dd-mm-yyyy
            - dd-mm-yy
            - dd-mm-yyyy HH:MM
            - dd-mm-yy   HH:MM
        """

        if isinstance(date_str, datetime.datetime):
            return date_str

        try: #01/02/2010
            date=datetime.datetime.strptime(date_str, '%d/%m/%Y')
            return date
        except:
            pass
        try: #01/02/2010 01:10
            date=datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M') 
            return date
        except:
            pass
        try: #01/02/10 01:10
            date=datetime.datetime.strptime(date_str, '%d/%m/%y %H:%M') 
            return date
        except:
            pass
        try: #22/03/2021 16:35:48
            date=datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S') 
            return date
        except:
            pass
        try: #01/02/10
            date=datetime.datetime.strptime(date_str, '%d/%m/%y')       
            return date
        except:
            pass
        try: #01-02-2010
            date=datetime.datetime.strptime(date_str, '%d-%m-%Y')
            return date
        except:
            pass
        try: #01-02-10 01:10
            date=datetime.datetime.strptime(date_str, '%d-%m-%y %H:%M') 
            return date
        except:
            pass
        try: #01-02-2010 01:10
            date=datetime.datetime.strptime(date_str, '%d-%m-%Y %H:%M') 
            return date
        except:
            pass
        try: #01-02-10
            date=datetime.datetime.strptime(date_str, '%d-%m-%y')       
            return date
        except:
            pass
        
        return None

    def str_to_date_written(self, date_str):

        if isinstance(date_str, datetime.datetime):
            return date_str

        #has portuguese month written
        if " de " in date_str:
            date_str = date_str.replace(" de "," ")
        

        ################################
        # mes por extenso em portugues #
        ################################
        if ''.join(filter(str.isalpha, date_str)).lower() in self.months_portuguese_english:

            try:
                date = datetime.datetime.strptime(
                    date_str.replace(
                        ''.join(filter(str.isalpha, date_str)), 
                        self.months_portuguese_english[''.join(filter(str.isalpha, date_str)).lower()]
                    ).strip(),
                    '%d %B %Y'
                )
                return date
            except:
                pass

            try:
                date = datetime.datetime.strptime(
                    date_str.replace(
                        ''.join(filter(str.isalpha, date_str)), 
                        self.months_portuguese_english[''.join(filter(str.isalpha, date_str)).lower()]
                    ).strip(),
                    '%d-%B-%Y'
                )
                return date
            except:
                pass

            try:
                date = datetime.datetime.strptime(
                    date_str.replace(
                        ''.join(filter(str.isalpha, date_str)), 
                        self.months_portuguese_english[''.join(filter(str.isalpha, date_str)).lower()]
                    ).strip(),
                    '%d %B, %Y'
                )
                return date
            except:
                pass
            return None
        
        ###################################
        # mes por abreviação em portugues #
        ###################################
        
        if ''.join(filter(str.isalpha, date_str)).lower() in self.months_portuguese_abrev_english:
            try:
                date = datetime.datetime.strptime(
                    date_str.replace(
                        ''.join(filter(str.isalpha, date_str)), 
                        self.months_portuguese_abrev_english[''.join(filter(str.isalpha, date_str)).lower()]
                    ).strip(),
                    '%d %B %Y'
                )
                return date
            except:
                pass
            
            try:
                date = datetime.datetime.strptime(
                    date_str.replace(
                        ''.join(filter(str.isalpha, date_str)), 
                        self.months_portuguese_abrev_english[''.join(filter(str.isalpha, date_str)).lower()]
                    ).strip(),
                    '%d-%B-%Y'
                )
                return date
            except:
                pass

            try:
                date = datetime.datetime.strptime(
                    date_str.replace(
                        ''.join(filter(str.isalpha, date_str)), 
                        self.months_portuguese_english[''.join(filter(str.isalpha, date_str)).lower()]
                    ).strip(),
                    '%d %B, %Y'
                )
                return date
            except:
                pass
            return None

        ################################
        # mes por abreviação em inglês #
        ################################
        
        if ''.join(filter(str.isalpha, date_str)).lower() in self.months_abrev_english:
            try:
                date = datetime.datetime.strptime(
                    date_str.replace(
                        ''.join(filter(str.isalpha, date_str)), 
                        self.months_abrev_english[''.join(filter(str.isalpha, date_str)).lower()]
                    ).strip(),
                    '%d %B %Y'
                )
                return date
            except:
                pass
            
            try:
                date = datetime.datetime.strptime(
                    date_str.replace(
                        ''.join(filter(str.isalpha, date_str)), 
                        self.months_abrev_english[''.join(filter(str.isalpha, date_str)).lower()]
                    ).strip(),
                    '%d-%B-%Y'
                )
                return date
            except:
                pass

            try:
                date = datetime.datetime.strptime(
                    date_str.replace(
                        ''.join(filter(str.isalpha, date_str)), 
                        self.months_abrev_english[''.join(filter(str.isalpha, date_str)).lower()]
                    ).strip(),
                    '%d %B, %Y'
                )
                return date
            except:
                pass
            return None
        return None

    def is_bigger_date(self, date1, date2, *args, **kwargs):
        
        """
            Returns: 
                - True if date1>date2
                - False if date1==date2 or date2>date1
            args:
                - date1: string or datetime object
                - date2: string or datetime object
            kwargs:
                - date1_tz: time zone. Will be None if not passed.
                - date2_tz: time zone. Will be None if not passed. 
                - be_equal: bool. Default is False

                If timezone1 != timezone2 will raise error                
        """
        date1_tz = None if 'date1_tz' not in kwargs else kwargs['date1_tz']
        date2_tz = None if 'date2_tz' not in kwargs else kwargs['date2_tz']
        be_equal = False if 'be_equal' not in kwargs else kwargs['be_equal']
        
        if date1_tz != date2_tz:
            raise(Exception("Cant compare time compare different time zones. Deinfed timezones incorrectly."))
        if isinstance(date1,str):
            date1 = self.str_to_date(date1)
        if isinstance(date2,str):
            date2 = self.str_to_date(date2)
        if (not be_equal  and date1.astimezone(date1_tz) > date2.astimezone(date2_tz)) or\
        (be_equal  and date1.astimezone(date1_tz) >= date2.astimezone(date2_tz)):
            return True
        return False

    def date_difference(self, date1, date2, *args, **kwargs):
        
        """
            Returns: 
                - timedelta object, always positive
            args:
                - date1: string or datetime object
                - date2: string or datetime object
            kwargs:
                - date1_tz: time zone. Will be None if not passed.
                - date2_tz: time zone. Will be None if not passed. 
                
                If timezone1 != timezone2 will raise error                
        """
        date1_tz = None if 'date1_tz' not in kwargs else kwargs['date1_tz']
        date2_tz = None if 'date2_tz' not in kwargs else kwargs['date2_tz']
        if date1_tz != date2_tz:
            raise(Exception("Cant compare time compare different time zones. Deinfed timezones incorrectly."))
        if isinstance(date1,str):
            date1 = self.date_to_str(date1)
        if isinstance(date2,str):
            date2 = self.date_to_str(date2)
        if self.is_bigger_date(date1.astimezone(date1_tz), date2.astimezone(date2_tz)):
            return date1.astimezone(date1_tz) - date2.astimezone(date2_tz)
        return date2.astimezone(date2_tz) - date1.astimezone(date1_tz)

    def is_smaller_date(self, date1, date2, *args, **kwargs):
        return self.is_bigger_date(date2, date1, *args, **kwargs)
    
    def is_date_between(self, date: datetime.datetime, date_smaller: datetime.datetime, date_bigger: datetime.datetime)->bool:
        
        return self.is_bigger_date(date, date_smaller) and self.is_smaller_date(date,date_bigger)

    
    def today_is_weekend(self):
                
        weekno = datetime.datetime.today().weekday()

        if weekno < 5:
            return False
        else:  # 5 Sat, 6 Sun
            return True
    
    def is_weekend(self, date:datetime.datetime):

        weekno = date.weekday()

        if weekno < 5:
            return False
        else:  # 5 Sat, 6 Sun
            return True
    
    def hour_rounder(self):
        # Rounds to nearest hour by adding a timedelta hour if minute >= 30
        t = datetime.datetime.now()
        return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
                +datetime.timedelta(hours=t.minute//30))
    
    def is_same_day(self, date1:datetime.datetime, date2:datetime.datetime)->bool:
        datetz_1 = None
        datetz_2 = None
        same_day = date1.astimezone(datetz_1).date()== date2.astimezone(datetz_2).date()
        return same_day
    
    def is_date_string(self, date_str:str)->bool:
        is_date_obj = self.str_to_date(date_str) is not None
        return is_date_obj
    
    def is_same_datetime(self,date1:datetime.datetime, date2:datetime.datetime)->bool:
        datetz_1 = None
        datetz_2 = None
        return date1.astimezone(datetz_1).date()== date2.astimezone(datetz_2).date()