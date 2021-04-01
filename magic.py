n = int(input('Введите число в диапазоне [4:1000]: '))
if n < 4 or n > 1000:
    print('Введенное число вне диапазона')
else:
    size = n
    tab = [[0]* size for _ in range(size)]
    tab[0] = [(col + 1)for col in range(size)]
    index = size
    y = 0; x = size - 1; r = size
    while index < size * size:
        r -= 1
        for _ in range(r):
            y += 1
            index += 1; tab[y][x] = index
        for _ in range(r):
            x -= 1
            index += 1; tab[y][x] = index
        if index >= size * size:
            break
        r -= 1
        for _ in range(r):
            y -= 1
            index += 1; tab[y][x] = index
        for _ in range(r):
            x += 1
            index += 1; tab[y][x] = index
    for line in tab:
        print('\t'.join(map(str, line)))