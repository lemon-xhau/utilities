import re

#2020 check
phone_dict = {
    'Viettel': ['086','097','096','098','032','033','034','035','036','037','038','039'],
    'Vinaphone': ['088','081','094','083','084','085','081','082'],
    'Gmobile': ['099','059'],
    'Mobiphone': ['089','090','093','070','077','079','076','078'],
    'Vietnamobile': ['092','056','058'],
}

def get_number(string):
    string = string.replace('-','').replace('.','').replace(' ','')
    string = string.replace('+84','0')
    return string

def check_phone(text):
    regrex = r'(03|05|07|08|09)+([0-9]{8})\b'
    
    clean_text = get_number(text)
    if len(clean_text) < 10 or len(clean_text) > 11:
        return False
    if not re.search(regrex, clean_text):
        return False

    # if clean_text.startswith('02'): #province number
    #     return True
    # if clean_text.startswith('080'): #post office
    #     return True

    for network, numbers in phone_dict.items(): #mobile number
        if clean_text[0:3] in numbers:
            return True
    return False