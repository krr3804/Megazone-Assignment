from utils import yaml_to_json
from dao import DAO
import json

# 메뉴 선택
while True:
    menu = input("""
1. 데이터 삽입
2. ID 리스트 조회
3. 데이터 조회
4. 종료
메뉴를 선택해주세요: 
""")
    if (menu == '1'):
        try:
            # yaml -> json 변환
            yaml_to_json()
        except FileNotFoundError:
            print("파일이 존재하지 않습니다.")
        else:
            # 데이터 불러오기
            with open('data.json') as json_file:
                data = json.load(json_file)
            # db에 데이터 삽입
            DAO().insert_data(data)
            print("정상적으로 삽입되었습니다.")
    elif (menu == '2'):
        # id 리스트 출력
        for x in DAO().find_id_list():
            print(x["_id"])
    elif (menu == '3'):
        # 조회할 데이터 id 입력받기
        continue
    elif (menu == '4'):
        # 프로그램 종료
        break
    else:
        print("잘못된 입력입니다.")
