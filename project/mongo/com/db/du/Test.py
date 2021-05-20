#1.获取连接mongoDB  2.获取到数据库的连接  3.获取到集合的连接  4.crud操作  5.关闭mongoDB连接
from pymongo import MongoClient

class MongoTest:
    def __init__(self):
        self.client=MongoClient('localhost',27017)
        self.mongodb=self.client['test']
        self.user=self.mongodb['user']
        print(self.user)
    def insertdata(self):
        try:
            # self.user.insert_one({'name':'咋还','age':18,'sex':'男'})
              self.user.insert_many([
                  {'name':'咋还2','age':19,'sex':'男'},
                  {'name':'咋还3','age':20,'sex':'男'},
                  {'name':'咋还4','age':21,'sex':'男'}
              ])
        except:
              raise
        finally:
              self.client.close()

    def deletedata(self):
        try:
            # self.user.delete_one({'name': '咋还'})
            self.user.delete_many({'name':'咋还'})
        except:
            raise
        finally:
            self.client.close()

    def updatedata(self):
        try:
            #self.user.update({'name':'咋还2'},{'name':'咋还3'})#修改一条
            self.user.update_many({'name':'咋还3'},{'$set':{'name':'咋还4'}})#修改多条
        except:
            raise
        finally:
            self.client.close()
    def selectdata(self):
        try:

            resuleSet=self.user.find({'age':20})
            for item in resuleSet:
                print(item['name'])

        except:
            raise
        finally:
            self.client.close()
if __name__=='__main__':
        t=MongoTest()
        #t.insertdata()
        #t.deletedata()
        #t.updatedata()
        t.selectdata()