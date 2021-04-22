import pymysql
# host가 ip역할
con = pymysql.connect(host='localhost', user= 'root', password='1234', port= 3306, db='shop')
print(con)


cur = con.cursor()
print(cur)

sql = 'insert into member values("python1", "python", "python", "python")'
result = cur.execute(sql)
print(result)

con.commit()



