<<<<<<< HEAD
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbf4b971-0097-4e42-a719-f8e5649f3cbe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "****************************************\n",
      "어서오세요, ‘요렇게’에 오신 것을 환영합니다:)\n",
      "Menu\t\t\t\tPrice\n",
      "------------------------------\n",
      "요거트 아이스크림(250g)\t3,000\n",
      "------------------------------\n",
      "\n",
      "No. Topping\t\tPrice\n",
      "------------------------------\n",
      "1     바나나       \t4,000\n",
      "2     딸기        \t5,000\n",
      "3     벌집꿀       \t7,000\n",
      "4     그레놀라      \t7,000\n",
      "5     초코쉘       \t7,000\n",
      "6     요거트 아이스크림 \t3,000\n",
      "------------------------------\n",
      "****************************************\n",
      "\n",
      "========================================\n",
      "현재 장바구니\n",
      "1. 요거트 아이스크림 x 1 = 3,000원\n",
      "----------------------------------------\n",
      "Total = 3,000원\n",
      "메뉴를 확정하려면 o\n",
      "메뉴를 삭제하려면 d\n",
      "메뉴를 추가하려면 a\n",
      "메뉴를 취소하려면 c\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "알파벳을 입력해주세요 :  a\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "메뉴 목록:\n",
      "1. 바나나 : 4,000원\n",
      "2. 딸기 : 5,000원\n",
      "3. 벌집꿀 : 7,000원\n",
      "4. 그레놀라 : 7,000원\n",
      "5. 초코쉘 : 7,000원\n",
      "6. 요거트 아이스크림 : 3,000원\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "추가할 토핑 번호를 골라주세요 :  5\n",
      "수량을 선택해주세요 (남은 수량: 15) :  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "========================================\n",
      "현재 장바구니\n",
      "1. 요거트 아이스크림 x 1 = 3,000원\n",
      "2. 초코쉘 x 4 = 28,000원\n",
      "----------------------------------------\n",
      "Total = 31,000원\n",
      "메뉴를 확정하려면 o\n",
      "메뉴를 삭제하려면 d\n",
      "메뉴를 추가하려면 a\n",
      "메뉴를 취소하려면 c\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "알파벳을 입력해주세요 :  a\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "메뉴 목록:\n",
      "1. 바나나 : 4,000원\n",
      "2. 딸기 : 5,000원\n",
      "3. 벌집꿀 : 7,000원\n",
      "4. 그레놀라 : 7,000원\n",
      "5. 초코쉘 : 7,000원\n",
      "6. 요거트 아이스크림 : 3,000원\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "추가할 토핑 번호를 골라주세요 :  4\n",
      "수량을 선택해주세요 (남은 수량: 11) :   5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "========================================\n",
      "현재 장바구니\n",
      "1. 요거트 아이스크림 x 1 = 3,000원\n",
      "2. 초코쉘 x 4 = 28,000원\n",
      "3. 그레놀라 x 5 = 35,000원\n",
      "----------------------------------------\n",
      "Total = 66,000원\n",
      "메뉴를 확정하려면 o\n",
      "메뉴를 삭제하려면 d\n",
      "메뉴를 추가하려면 a\n",
      "메뉴를 취소하려면 c\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "알파벳을 입력해주세요 :  a\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "메뉴 목록:\n",
      "1. 바나나 : 4,000원\n",
      "2. 딸기 : 5,000원\n",
      "3. 벌집꿀 : 7,000원\n",
      "4. 그레놀라 : 7,000원\n",
      "5. 초코쉘 : 7,000원\n",
      "6. 요거트 아이스크림 : 3,000원\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "추가할 토핑 번호를 골라주세요 :   7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "유효하지 않은 입력입니다.\n",
      "\n",
      "========================================\n",
      "현재 장바구니\n",
      "1. 요거트 아이스크림 x 1 = 3,000원\n",
      "2. 초코쉘 x 4 = 28,000원\n",
      "3. 그레놀라 x 5 = 35,000원\n",
      "----------------------------------------\n",
      "Total = 66,000원\n",
      "메뉴를 확정하려면 o\n",
      "메뉴를 삭제하려면 d\n",
      "메뉴를 추가하려면 a\n",
      "메뉴를 취소하려면 c\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "\n",
    "menu_list = [\n",
    "    {'name': '바나나', 'price': 4000},\n",
    "    {'name': '딸기', 'price': 5000},\n",
    "    {'name': '벌집꿀', 'price': 7000},\n",
    "    {'name': '그레놀라', 'price': 7000},\n",
    "    {'name': '초코쉘', 'price': 7000},\n",
    "    {'name': '요거트 아이스크림', 'price': 3000}\n",
    "]\n",
    "\n",
    "def display_menu():\n",
    "    print('*' * 40)\n",
    "    print('어서오세요, ‘요렇게’에 오신 것을 환영합니다:)')\n",
    "    print(\"Menu\\t\\t\\t\\tPrice\")\n",
    "    print(\"-\" * 30)\n",
    "    print(\"요거트 아이스크림(250g)\\t3,000\")\n",
    "    print(\"-\" * 30)\n",
    "    print(\"\\nNo. Topping\\t\\tPrice\")\n",
    "    print(\"-\" * 30)\n",
    "    for idx, item in enumerate(menu_list, start=1):\n",
    "        print(f\"{idx:<5} {item['name']:<10}\\t{item['price']:,}\")\n",
    "    print(\"-\" * 30)\n",
    "    print(\"*\" * 40)\n",
    "\n",
    "def display_cart(cart, total_price):\n",
    "    print(\"\\n\" + \"=\" * 40)\n",
    "    print(\"현재 장바구니\")\n",
    "    for i, item in enumerate(cart, start=1):\n",
    "        print(f\"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원\")\n",
    "    print(\"-\" * 40)\n",
    "    print(f\"Total = {total_price:,}원\")\n",
    "\n",
    "def add_menu(cart, total_price):\n",
    "    try:\n",
    "        # 현재 아이스크림을 제외한 토핑 수량 합산\n",
    "        current_toppings = sum(item['quantity'] for item in cart if item['name'] != '요거트 아이스크림')\n",
    "        remaining = 15 - current_toppings\n",
    "\n",
    "        if remaining <= 0:\n",
    "            print(\"토핑은 최대 15개까지만 선택할 수 있습니다.\")\n",
    "            return total_price\n",
    "\n",
    "        print(\"\\n메뉴 목록:\")\n",
    "        for i, item in enumerate(menu_list, start=1):\n",
    "            print(f\"{i}. {item['name']} : {item['price']:,}원\")\n",
    "\n",
    "        idx = int(input(\"추가할 토핑 번호를 골라주세요 : \").strip()) - 1\n",
    "\n",
    "        # 기본 아이스크림 중복 추가 방지\n",
    "        if menu_list[idx]['name'] == '요거트 아이스크림':\n",
    "            print(\"요거트 아이스크림은 기본으로 포함되어 있어 중복 추가할 수 없습니다.\")\n",
    "            return total_price\n",
    "\n",
    "        qty = int(input(f\"수량을 선택해주세요 (남은 수량: {remaining}) : \").strip())\n",
    "        if qty <= 0 or qty > remaining:\n",
    "            print(f\"1개 이상, {remaining}개 이하만 선택 가능합니다.\")\n",
    "            return total_price\n",
    "\n",
    "        selected_item = menu_list[idx]\n",
    "\n",
    "        for item in cart:\n",
    "            if item['name'] == selected_item['name']:\n",
    "                item['quantity'] += qty\n",
    "                break\n",
    "        else:\n",
    "            cart.append({'name': selected_item['name'], 'quantity': qty, 'price': selected_item['price']})\n",
    "\n",
    "        total_price += selected_item['price'] * qty\n",
    "    except (ValueError, IndexError):\n",
    "        print(\"유효하지 않은 입력입니다.\")\n",
    "    return total_price\n",
    "\n",
    "def del_menu(cart, total_price):\n",
    "    display_cart(cart, total_price)\n",
    "    idx = int(input(\"삭제할 메뉴의 번호를 골라주세요 : \")) - 1\n",
    "    if 0 <= idx < len(cart):\n",
    "        item = cart[idx]\n",
    "        print(f\"'{item['name']}'의 현재 수량: {item['quantity']}\")\n",
    "        del_qty = int(input(\"몇 개를 삭제하시겠습니까? : \"))\n",
    "\n",
    "        if del_qty >= item['quantity'] or del_qty <= 0:\n",
    "            total_price -= item['price'] * item['quantity']\n",
    "            cart.pop(idx)\n",
    "            print(f\"'{item['name']}' 전체가 장바구니에서 삭제되었습니다.\")\n",
    "        else:\n",
    "            item['quantity'] -= del_qty\n",
    "            total_price -= item['price'] * del_qty\n",
    "            print(f\"'{item['name']}' {del_qty}개가 삭제되었습니다.\")\n",
    "    else:\n",
    "        print(\"올바른 번호를 입력하세요.\")\n",
    "    return total_price\n",
    "\n",
    "def select_pro():\n",
    "    print(\"메뉴를 확정하려면 o\")\n",
    "    print(\"메뉴를 삭제하려면 d\")\n",
    "    print(\"메뉴를 추가하려면 a\")\n",
    "    print(\"메뉴를 취소하려면 c\")\n",
    "    return input(\"알파벳을 입력해주세요 : \").strip().lower()\n",
    "\n",
    "def pay_deci():\n",
    "    return input(\"주문이 확정되었습니다. 결제를 하시겠습니까? (y/n): \")\n",
    "\n",
    "def pay_screen(total_price, num_order):\n",
    "    print(f\"{total_price:,}원 결제하겠습니다. 카드를 삽입해주세요.\")\n",
    "    print(\"결제가 완료되었습니다.\")\n",
    "    print(f\"주문번호는 {num_order}번 입니다.\")\n",
    "\n",
    "def end_screen_delay():\n",
    "    print(\"초기화면으로 돌아갑니다.\")\n",
    "    for i in range(5, 0, -1):\n",
    "        print(f\"{i} \", end='\\r', flush=True)\n",
    "        time.sleep(1)\n",
    "    print(\" \", end='\\r')\n",
    "\n",
    "def main():\n",
    "    num_order = 1\n",
    "    while True:\n",
    "        display_menu()\n",
    "        cart = [{'name': menu_list[5]['name'], 'price': menu_list[5]['price'], 'quantity': 1}]\n",
    "        total_price = 3000\n",
    "        while True:\n",
    "            display_cart(cart, total_price)\n",
    "            choice = select_pro()\n",
    "\n",
    "            if choice == 'o':\n",
    "                break\n",
    "            elif choice == 'd':\n",
    "                total_price = del_menu(cart, total_price)\n",
    "            elif choice == 'a':\n",
    "                total_price = add_menu(cart, total_price)\n",
    "            elif choice == 'c':\n",
    "                print(\"주문이 취소됩니다.\")\n",
    "                end_screen_delay()\n",
    "                break\n",
    "            elif choice == '99':\n",
    "                print(\"관리자 중지입니다.\")\n",
    "                return\n",
    "\n",
    "        if choice in ['c', '99']:\n",
    "            continue\n",
    "        if total_price == 0:\n",
    "            print(\"장바구니가 비어있습니다.\")\n",
    "            end_screen_delay()\n",
    "            continue\n",
    "\n",
    "        if pay_deci() == 'y':\n",
    "            pay_screen(total_price, num_order)\n",
    "            num_order += 1\n",
    "        end_screen_delay()\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f669ad7-b045-4639-9eab-ad0ab0f97207",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
=======
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
>>>>>>> 30c339c5ac65b3491ab7b456d2ab4953ebae0f7b
