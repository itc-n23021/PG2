def is_phone_number(text):
    if len(text) != 13:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 8):
        if not text[i].isdecimal():
            return False
    if text[8] != '-':
        return False
    for i in range(9, 13):
        if not text[i].isdecimal():
            return False
    return True

message = '明日の朝10時頃に、415-5555-1111に電話してください。オフィスは415-5555-9999です。'
for i in range(len(message)):
    chunk = message[i:i+13]
    if is_phone_number(chunk):
        print('電話番号が見つかりました: ' + chunk)
print('完了')