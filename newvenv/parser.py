import ruamel.yaml
import json
import sys
import fnmatch


class Parser:
    def __init__(self):
        self.yaml = ruamel.yaml.YAML(typ='safe')

    def yaml_to_json(self, file_name):
        # YAML 형식의 파일이 아닐 경우 예외를 던짐
        if fnmatch.fnmatch(file_name, '*.yaml') | fnmatch.fnmatchcase(file_name, '*.yml'):
            with open(file_name, 'r') as yaml_file, open('data.json', 'w') as json_file:
                # YAML 파일에서 데이터를 로드해 파이썬 자료형에 담음
                yaml_objs = list(self.yaml.load_all(yaml_file))
                # yaml 파일이 비어있는 경우 예외를 던짐
                if not yaml_objs:
                    raise ValueError()
                else:
                    # json파일로 데이터를 변환해서 반환
                    json.dump(yaml_objs, json_file)
        else:
            raise NameError()

    def json_to_yaml(self):
        with open('data.json', 'r') as json_file, open('data.yaml', 'w') as yaml_file:
            # data.json의 데이터를 불러와 저장
            json_data = json.load(json_file)
            # 저장된 json 데이터를 yaml 파일로 변환
            self.yaml.dump(json_data, yaml_file)

        # 콘솔에 출력
        self.yaml.dump(json_data, sys.stdout)
