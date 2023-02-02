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
        self.collection.insert_many(data)

    def find_id_list(self):
        # 전체 id 목록 가져오기
        list = [str(x["_id"]) for x in self.collection.find({}, {"_id": 1})]
        return list

    def find_data_by_id(self, id):
        # object id로 데이터 호출
        data = self.collection.find_one({"_id": ObjectId(id)}, {"_id": 0})
        return data
