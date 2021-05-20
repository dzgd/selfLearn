import pymysql
def showDB():
    try:
        con = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="dujin",
                                   charset="utf8")
        cursor = con.cursor()
        cursor.execute("select * from phones ")
        rows = cursor.fetchall()
        for row in rows:
            print("%-8s %-16s %-8s %-16s " % (row[0], row[1], row[2], row[3]))

        con.close()
    except Exception as err:
        print(err)

showDB()