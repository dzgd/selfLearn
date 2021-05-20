import pymongo

client = pymongo.MongoClient(host='127.0.0.1', port=27017)

# 查询所有的数据库
# print(client.list_database_names())
# print(client.database_names())

# 查询所有集合
# 步骤:
# 1.先进入数据库(两种方式)
# sc = client.school
sc = client['test']
print(sc)
# 2.再查询所有集合
print(sc.list_collection_names())
# sc.create_collection("xiaoming")
sc.xiaoming.insert_one({"name":"胖子","age":18})
