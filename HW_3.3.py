import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    count_code = "+38", "+"
    clear_phone_num = re.sub(r"[^0-9\+]", "", phone_number)
    if clear_phone_num.startswith("38"):
        clear_phone_num = count_code[1] + clear_phone_num
    elif clear_phone_num.startswith("0"):
        clear_phone_num = count_code[0] + clear_phone_num

    return clear_phone_num

normalized_numbers = [normalize_phone(number) for number in raw_numbers]
print(normalized_numbers)
