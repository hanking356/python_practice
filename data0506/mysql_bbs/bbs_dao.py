import pymysql  # alt+Enter


def create(data):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into bbs values (%s, %s, %s, %s)'
    result = cur.execute(sql, data)
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

def update(no, title):
    #1.mysql과 연결
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    #2.스트림 안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    #. sql문을 만들어서 전송함.
    data = (title, no)
    sql = "update bbs set title = %s where no = %s"
    cur.execute(sql, data) #tuple로 넣어주어야 한다.

    #4. auto-commit이 안된다. 수동으로 반영시켜야한다.
    con.commit()
    con.close()

def read(no):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    # 2.스트림 안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    #'select * from member where id ="' + id + '"'
    sql = "select * from bbs where no = %s"
    cur.execute(sql, no)

    row = cur.fetchone()
    # cur.fetchall() : 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(row)
    print(type(row))
    print('title:' + row[1])
    #갖고 올게 없으므로 commit 할필요가 없음
    con.close()

def all():
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    # 2.스트림 안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)


    sql = "select * from bbs"
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