import pymysql  # alt+Enter


def create(id, pw, name, tel):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into member values ("' + id + '","' + pw + '","' + name + '","' + tel + '")'
    result = cur.execute(sql)
    print(result)

    con.commit()
    con.close()

def create2(data):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into member values (%s, %s, %s, %s)'
    result = cur.execute(sql, data)
    print('처리 결과', result, '개')

    con.commit()
    con.close()

def create3(data):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into member values (%s, %s, %s, %s)'
    result = cur.executemany(sql, data)
    print('처리 결과', result, '개')

    con.commit()
    con.close()



def delete(id):
    con = pymysql.connect(host = 'localhost', port= 3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'delete from member where id ="' + id + '"'
    result = cur.execute(sql)
    print(result)

    con.commit()
    con.close()

def update(id, tel):
    #1.mysql과 연결
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    #2.스트림 안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    #. sql문을 만들어서 전송함.
    data = (tel, id)
    sql = "update member set tel = %s where id = %s"
    cur.execute(sql, data) #tuple로 넣어주어야 한다.

    #4. auto-commit이 안된다. 수동으로 반영시켜야한다.
    con.commit()
    con.close()

def read():
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    # 2.스트림 안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    sql = "select * from member where id = 'java'"
    cur.execute(sql)

    row = cur.fetchone()
    # cur.fetchall() : 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(row)
    print(type(row))
    # print(row['id'])
    #갖고 올게 없으므로 commit 할필요가 없음
    con.close()

def read2(id):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    # 2.스트림 안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    #'select * from member where id ="' + id + '"'
    sql = "select * from member where id = %s"
    cur.execute(sql, id)

    row = cur.fetchone()
    # cur.fetchall() : 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(row)
    print(type(row))
    print(row[1])
    #갖고 올게 없으므로 commit 할필요가 없음
    con.close()

def read3():
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    # 2.스트림 안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor(pymysql.cursors.DictCursor)
    print(cur)


    sql = "select * from member"
    cur.execute(sql)

    #row = cur.fetchone()
    rows = cur.fetchall() #조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(rows)
    print(type(rows))
    #print(rows[0])
    for row in rows:
        print(row)

    #갖고 올게 없으므로 commit 할필요가 없음
    con.close()