import time
#################메뉴리스트정의
menu_list = [ 
    {'name': '바나나', 'price': 4000},
    {'name': '딸기', 'price': 5000},
    {'name': '벌집꿀', 'price': 7000},
    {'name': '그레놀라', 'price': 7000},
    {'name': '초코쉘', 'price': 7000},
    {'name': '요거트 아이스크림', 'price': 3000}
]
num_order = 1
final_break = False
while True:
    ######################################초기화면 (메뉴판)################################################
    print('*'*40)
    print('어서오세요, ‘요렇게’에 오신것을 환영합니다:)\n')
    print("Menu\t\t\tPrice")
    print("-" * 30)
    print("요거트 아이스크림(250g)\t3,000")
    print("-" * 30)
    print("\nNo.  Topping\t\tPrice")
    print("-" * 30)
    for idx, item in enumerate(menu_list, start=1):
        print(f"{idx:<5} {item['name']:<10}\t{item['price']:,}")
    print("-" * 30)
    print("*" * 40)
    
    ##############기본 상품(요거트 아이스크림) 장바구니에 자동추가
    cart = []
    default_item = menu_list[5]
    cart.append({'name': default_item['name'], 'price': default_item['price'], 'quantity': 1})
    total_price = 3000
    cancle = False
    ###############장바구니 관리 루프 시작
    while True:
       #########장바구니 출력 🔄 중복 제거된 장바구니 출력 블록
        print("\n" + "=" * 40)
        print("현재 장바구니")
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
        print("-" * 40)
        print(f"Total = {total_price:,}원")
      ##########메뉴선택안내
        print("메뉴를 확정하려면 o")
        print("메뉴를 삭제하려면 d")
        print("메뉴를 추가하려면 a")
        print("메뉴를 취소하려면 c")
        ############################# 99번 입력 시 무한루프 끝 #####################################
        select = (input("알파벳을 입력해주세요 : "))
        ####################[2-1]주문 확정
        if select == "o":
            break
        ####################[2-2]메뉴 삭제
        elif select == "d":
           #################삭제할 메뉴 번호 입력받고 수량 삭제 처리
            print("\n" + "=" * 40)
            print("현재 장바구니")
            for i, item in enumerate(cart, start=1):
                print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
            print("-" * 40)
            print(f"Total = {total_price:,}원")
        
            del_no = int(input("삭제할 메뉴의 번호를 골라주세요 : ")) - 1
            if 0 <= del_no < len(cart):
                item = cart[del_no]
                print(f"'{item['name']}'의 현재 수량: {item['quantity']}")
                del_qty = int(input("몇 개를 삭제하시겠습니까? : "))
        
                if del_qty >= item['quantity'] or del_qty <= 0:
                    # 전체 삭제
                    total_price -= item["price"] * item["quantity"]
                    cart.pop(del_no)
                    print(f"'{item['name']}' 전체가 장바구니에서 삭제되었습니다.")
                else:
                    # 일부 수량만 삭제
                    item['quantity'] -= del_qty
                    total_price -= item["price"] * del_qty
                    print(f"'{item['name']}' {del_qty}개가 삭제되었습니다.")
        
            else:
                print("올바른 번호를 입력하세요.")
        ############################# [2-3] 메뉴 추가
        elif select == "a":
     ######################## 메뉴 리스트 보여주고 선택한 토핑 추가
            print("\n메뉴 목록:")
            for i, item in enumerate(menu_list, start=1):
                print(f"{i}. {item['name']} : {item['price']:,}원")
            add_topping = int(input('추가할 토핑 번호를 골라주세요 :')) - 1
            qty = int(input('수량을 선택해주세요 : '))
    
            selected_item = menu_list[add_topping]
            found = False
    
            for item in cart:
                if item['name'] == selected_item['name']:
                    item['quantity'] += qty
                    found = True
                    break
    
            if not found:
                cart.append({'name': selected_item['name'], 'quantity': qty, 'price': selected_item['price']})
    
            total_price += selected_item['price'] * qty
       ###############[2-4]주문 취소
        elif select == "c":
            print("주문이 취소됩니다.")
            cancle = True
            break
        ################# [2-5] 프로그램 종료 명령어
        elif select == "99":
            print("관리자 중지입니다.")
            final_break = True
            break
    ################[3] 외부 루프 종료 조건
    if final_break:
        break
   
    ################# [4] 주문 취소 시 초기화면으로 복귀
    if cancle:
        print("초기화면으로 돌아갑니다.")
        for i in range(5, 0, -1):
            print(f"{i}   ", end='\r', flush=True)
            time.sleep(1)
        print("   ", end='\r')
        continue
   
    #################장바구니가 비어있을 시
    if total_price == 0:
        print("장바구니가 비어있습니다.")
        print("초기화면으로 돌아갑니다.")
        for i in range(5, 0, -1):
            print(f"{i}   ", end='\r', flush=True)
            time.sleep(1)
        print("   ", end='\r')
        continue
    ###################### [5] 결제 여부 확인
    pay = input("주문이 확정되었습니다. 결제를 하시겠습니까? (y/n)")
    if pay == 'y':
        print(f"{total_price:,}원 결제하겠습니다. 카드를 삽입해주세요.")
        print("결제가 완료되었습니다.")
        print(f"주문번호는 {num_order}번 입니다.")
        num_order += 1
        print("초기화면으로 돌아갑니다.")
        for i in range(5, 0, -1):
            print(f"{i}   ", end='\r', flush=True)
            time.sleep(1)
        print("   ", end='\r')
        continue
    else:
        print("초기화면으로 돌아갑니다.")
        for i in range(5, 0, -1):
            print(f"{i}   ", end='\r', flush=True)
            time.sleep(1)
        print("   ", end='\r')
        continue
