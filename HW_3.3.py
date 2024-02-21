
import re

def normalize_phone(phone_number):
    clear_phone_num = re.sub(r"[^0-9\+]", "", phone_number) # Видаляе непотрібні символи в phone_number та залишае тольки числа та знак +

    count_code = "+38", "+"
    if clear_phone_num.startswith("38"): # Якщо номер телофону починаеться з 38 то додає + на початок
        clear_phone_num = count_code[1] + clear_phone_num
    elif clear_phone_num.startswith("0"): # Якщо номер телофону починаеться з 0 то додає +38 на початок
        clear_phone_num = count_code[0] + clear_phone_num

    return clear_phone_num

print(normalize_phone('380 31 922-2221 '))
print(normalize_phone('+380-31-922-2221-'))
print(normalize_phone('  (031)9222221'))