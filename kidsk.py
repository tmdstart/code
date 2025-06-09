import time

membership_dict = {}

menu_list = [
    {'name': '바나나', 'price': 4000},
    {'name': '딸기', 'price': 5000},
    {'name': '벌집꿀', 'price': 7000},
    {'name': '그레놀라', 'price': 7000},
    {'name': '초코쉘', 'price': 7000},
    {'name': '요거트 아이스크림', 'price': 3000}
]

def get_valid_number_input(msg, min_no = 1, max_no = 5):
    # 숫자체크
    try: 
        number = int(input(msg).strip())
        if number < min_no:
            print(f"{min_no} 이상 숫자를 입력하세요")
            return None
        elif number > max_no:
            print(f"{max_no} 이하 숫자를 입력하세요")
            return None
        else:
            return number
    except ValueError:
        print("숫자를 입력하세요")
        return None

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
    current_total = sum(item['quantity'] for item in cart)
    remaining = 16 - current_total
    
    if remaining <= 0:
        print("장바구니에는 최대 15개까지만 담을 수 있습니다.")
        return total_price

    print("\n메뉴 목록:")
    for i, item in enumerate(menu_list, start=1):
        print(f"{i}. {item['name']} : {item['price']:,}원")
    idx = get_valid_number_input("추가할 토핑 번호를 골라주세요 : ", 1, len(menu_list))
    if idx:
        idx -= 1
        qty = get_valid_number_input(f"수량을 선택해주세요 (남은 수량: {remaining}) : ",1,remaining)
        if qty:
            selected_item = menu_list[idx]
            for item in cart:
                if item['name'] == selected_item['name']:
                    item['quantity'] += qty
                    if item['quantity'] > 15:
                        item['quantity'] = 15
                    break
            else:
                cart.append({'name': selected_item['name'], 'quantity': qty, 'price': selected_item['price']})
    
            total_price += selected_item['price'] * qty
    return total_price

def del_menu(cart, total_price):
    display_cart(cart, total_price)
    idx = get_valid_number_input("삭제할 메뉴의 번호를 골라주세요 : ",1,len(cart))
    if idx:
        idx -= 1
        item = cart[idx]
        print(f"'{item['name']}'의 현재 수량: {item['quantity']}")
        del_qty = get_valid_number_input("몇 개를 삭제하시겠습니까? : ", 1, item['quantity'])
        if del_qty:
            item['quantity'] -= del_qty
            total_price -= item['price'] * del_qty
            print(f"'{item['name']}' {del_qty}개가 삭제되었습니다.")
    return total_price


def search_ice(cart):
    yoaitem = input("찾고 싶은 간식을 입력하세요: ")
    # 카트의 'name' 값과 비교
    found = any(item['name'] == yoaitem for item in cart)
    print("있어요" if found else "없어요")



def select_pro():
    print("메뉴를 확정하려면 o")
    print("메뉴를 삭제하려면 d")
    print("메뉴를 추가하려면 a")
    print("메뉴를 취소하려면 c")
    return input("알파벳을 입력해주세요 : ").lower().strip()

def pay_deci():
    return input("주문이 확정되었습니다. 결제를 하시겠습니까? (y/n): ").lower().strip()

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

def pay_screen(total_price, num_order):
    phone = None
    used_point = 0

    use_point = input("포인트를 사용하시겠습니까? (y/n): ").lower().strip()
    if use_point == 'y':
        phone = input("전화번호를 입력해주세요 (- 없이): ").strip()
        if phone in membership_dict:
            available = membership_dict[phone]
            print(f"현재 {available}포인트가 있습니다.")
            while True:
                try:
                    used_point = int(input("사용할 포인트를 입력해주세요: "))
                    if used_point > available:
                        print("포인트가 부족합니다.")
                    elif used_point > total_price:
                        print("결제 금액보다 많은 포인트는 사용할 수 없습니다.")
                    else:
                        membership_dict[phone] -= used_point
                        total_price -= used_point
                        print(f"{used_point}포인트를 사용하여 {total_price}원을 결제합니다.")
                        break
                except ValueError:
                    print("숫자를 입력해주세요.")
        else:
            print("해당 번호로 적립된 포인트가 없습니다.")

    print(f"{total_price:,}원 결제하겠습니다. 카드를 삽입해주세요.")
    print("결제가 완료되었습니다.")

    # 포인트를 사용하지 않았을 때만 적립
    if used_point == 0:
        mem = input("포인트 적립 하시겠습니까? (y/n): ").lower().strip()
        if mem == 'y':
            if not phone:
                phone = input("전화번호를 입력해주세요 (- 없이): ").strip()
            point = int(total_price * 0.1)
            membership_dict[phone] = membership_dict.get(phone, 0) + point
            print(f"{phone} 번호에 {point}포인트가 적립되어 총 {membership_dict[phone]}포인트가 있습니다.")
    else:
        print("포인트를 사용하셨기 때문에 이번 결제는 적립되지 않습니다.")

    print(f"주문번호는 {num_order}번 입니다.")


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
            elif choice == 'w':
                search_ice()
            elif choice == 'c':
                print("주문이 취소됩니다.")
                end_screen_delay()
                break
            elif choice == '99':
                print("관리자 중지입니다.")
                return
            else:
                print("입력이 올바르지 않습니다.")

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