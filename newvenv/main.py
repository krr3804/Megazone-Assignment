from parsers import Parsers
from dao import Dao
import json
import bson
import ruamel.yaml
# 메뉴 선택
while True:
    menu = input("""
1. 데이터 삽입
2. ID 리스트 조회
3. 데이터 조회
4. 종료
메뉴를 선택해주세요: """)
    if menu == '1':
        try:
            # 파일명 콘솔로 입력받기
            file_name = input("파일명 입력: ")
            # yaml -> json 변환
            Parsers().yaml_to_json(file_name)
        except FileNotFoundError:
            # 입력한 파일이 존재하지 않은 경우
            print("파일이 존재하지 않습니다.")
        except (ruamel.yaml.scanner.ScannerError, NameError, ValueError):
            # 입력한 파일의 형식이 올바르지 않은 경우 (1. yaml 파일이 아님 2. yaml 문법에 오류가 있음 3.파일이 비어있음)
            print("잘못된 형식의 파일입니다.")
        else:
            # 데이터 불러오기
            with open('data.json', 'r') as json_file:
                data = json.load(json_file)
            # db에 데이터 삽입
            Dao().insert_data(data)
            print("정상적으로 입력되었습니다.")
    elif menu == '2':
        # id 리스트 출력
        list = Dao().find_id_list()
        # 데이터가 존재하는 경우
        if (len(list) > 0):
            print(*list, sep="\n")
        # DB에 데이터가 없는 경우
        else:
            print("데이터가 존재하지 않습니다.")
    elif menu == '3':
        # 조회할 데이터 id 입력받기
        id = input("ID를 입력해주세요: ")
        try:
            # id로 db에서 데이터 조회
            data = Dao().find_data_by_id(id)
        except bson.errors.InvalidId:
            # ID가 데이터베이스에 존재하지 않는 경우
            print("존재하지 않는 ID입니다.")
        else:
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)
            # json을 yaml data로 변환
            Parsers().json_to_yaml()
    elif menu == '4':
        # 프로그램 종료
        print("프로그램이 종료되었습니다.")
        break
    else:
        # 지정된 메뉴 이외의 값이 입력된 경우
        print("잘못된 입력입니다.")
