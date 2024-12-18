def get_km_isso(original_value):
    # Преобразование из одного числа в два
    km = original_value >> 16 # Сдвиг на 16 бит вправо
    m = original_value & 0xFFFF # Битовая маска 65535
    print(f'km: {km}, m: {m}')


def get_w_isso(km, m):
    # Обратное преобразование
    reversed_value = (km << 16) | m # Сдвиг на 16 бит влево и побитовое ИЛИ
    print(f'Reversed value: {reversed_value}')
