import time

menu_list = [
    {'name': '바나나', 'price': 4000},
    {'name': '딸기', 'price': 5000},
    {'name': '벌집꿀', 'price': 7000},
    {'name': '그레놀라', 'price': 7000},
    {'name': '초코쉘', 'price': 7000},
    {'name': '요거트 아이스크림', 'price': 3000}
]

def display_menu():
    print('*' * 40)
    print('어서오세요, ‘요렇게’에 오신 것을 환영합니다:)')
    print("Menu\t\t\t\tPrice")
    print("-" * 30)
    print("요거트 아이스크림(250g)\t3,000")
    print("-" * 30)
    print("\nNo. Topping\t\tPrice")
    print("-" * 30)
    for idx, item in enumerate(menu_list, start=1):
        print(f"{idx:<5} {item['name']:<10}\t{item['price']:,}")
    print("-" * 30)
    print("*" * 40)

def display_cart(cart, total_price):
    print("\n" + "=" * 40)
    print("현재 장바구니")
    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
    print("-" * 40)
    print(f"Total = {total_price:,}원")

def add_menu(cart, total_price):
    print("\n메뉴 목록:")
    for i, item in enumerate(menu_list, start=1):
        print(f"{i}. {item['name']} : {item['price']:,}원")
    idx = int(input("추가할 토핑 번호를 골라주세요 : ")) - 1
    qty = int(input("수량을 선택해주세요 : "))

    selected_item = menu_list[idx]
    for item in cart:
        if item['name'] == selected_item['name']:
            item['quantity'] += qty
            break
    else:
        cart.append({'name': selected_item['name'], 'quantity': qty, 'price': selected_item['price']})

    total_price += selected_item['price'] * qty
    return total_price

def del_menu(cart, total_price):
    display_cart(cart, total_price)
    idx = int(input("삭제할 메뉴의 번호를 골라주세요 : ")) - 1
    if 0 <= idx < len(cart):
        item = cart[idx]
        print(f"'{item['name']}'의 현재 수량: {item['quantity']}")
        del_qty = int(input("몇 개를 삭제하시겠습니까? : "))

        if del_qty >= item['quantity'] or del_qty <= 0:
            total_price -= item['price'] * item['quantity']
            cart.pop(idx)
            print(f"'{item['name']}' 전체가 장바구니에서 삭제되었습니다.")
        else:
            item['quantity'] -= del_qty
            total_price -= item['price'] * del_qty
            print(f"'{item['name']}' {del_qty}개가 삭제되었습니다.")
    else:
        print("올바른 번호를 입력하세요.")
    return total_price

def select_pro():
    print("메뉴를 확정하려면 o")
    print("메뉴를 삭제하려면 d")
    print("메뉴를 추가하려면 a")
    print("메뉴를 취소하려면 c")
    return input("알파벳을 입력해주세요 : ")

def pay_deci():
    return input("주문이 확정되었습니다. 결제를 하시겠습니까? (y/n): ")

def pay_screen(total_price, num_order):
    print(f"{total_price:,}원 결제하겠습니다. 카드를 삽입해주세요.")
    print("결제가 완료되었습니다.")
    print(f"주문번호는 {num_order}번 입니다.")

def end_screen_delay():
    print("초기화면으로 돌아갑니다.")
    for i in range(5, 0, -1):
        print(f"{i} ", end='\r', flush=True)
        time.sleep(1)
    print(" ", end='\r')

def main():
    num_order = 1
    while True:
        display_menu()
        cart = [{'name': menu_list[5]['name'], 'price': menu_list[5]['price'], 'quantity': 1}]
        total_price = 3000
        while True:
            display_cart(cart, total_price)
            choice = select_pro()

            if choice == 'o':
                break
            elif choice == 'd':
                total_price = del_menu(cart, total_price)
            elif choice == 'a':
                total_price = add_menu(cart, total_price)
            elif choice == 'c':
                print("주문이 취소됩니다.")
                end_screen_delay()
                break
            elif choice == '99':
                print("관리자 중지입니다.")
                return

        if choice in ['c', '99']:
            continue
        if total_price == 0:
            print("장바구니가 비어있습니다.")
            end_screen_delay()
            continue

        if pay_deci() == 'y':
            pay_screen(total_price, num_order)
            num_order += 1
        end_screen_delay()

main()
#
# hello
