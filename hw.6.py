def display_multiplication_tablea():
    for i in range(2, 10, 4):
        for j in range(1, 10):
            for k in range(0, 4):
                if i + k <= 9:
                    print(f'{i + k} * {j} = {(i + k) * j:2d}', end='\t')
            print()
        print()

display_multiplication_tablea()
