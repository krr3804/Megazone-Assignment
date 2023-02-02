from pymongo import MongoClient
from bson.objectid import ObjectId


class DAO:
    def __init__(self):
        # 클라이언트 연결
        client = MongoClient(host='localhost', port=27017)
        # 컬렉션 호출
        self.collection = client['db']['manifests']

    def insert_data(self, data):
        # 데이터 삽입
        manifest_id = self.collection.insert_one(data).inserted_id
        return manifest_id

    def find_id_list(self):
        # 전체 id 목록 가져오기
        return self.collection.find({}, {"_id": 1})