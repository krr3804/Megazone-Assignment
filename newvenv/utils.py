import ruamel.yaml
import json


def yaml_to_json():
    # 파일명을 입력으로 받음
    file_name = input("파일명 입력: ")
    yaml = ruamel.yaml.YAML(typ='safe')
    # YAML 파일에서 데이터를 로드해 파이썬 자료형에 담음
    with open(file_name) as yaml_in:
        yaml_obj = yaml.load(yaml_in)
    # json파일로 데이터를 변환해서 반환
    with open('data.json', 'w') as json_data:
        json.dump(yaml_obj, json_data)
