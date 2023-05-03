shopping_bag ={}

print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    quantity = int(input('수량은? '))
    shopping_bag[item] = quantity
    print(f'장바구니에 {item} {quantity}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기: {shopping_bag}')


print('\n[검색]')
s = input('장바구니에서 확인하고자 하는 상품은? ')
if s in shopping_bag :
    print(f'{s}은(는) {shopping_bag[s]}개 담겨 있습니다.')
else :
    print(f'{s}라는 상품은 장바구니에 존재하지 않습니다.')
