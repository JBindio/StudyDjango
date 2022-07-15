import pandas as pd
import cx_Oracle as ora

# 오라클 연결 및 접속하기
def getConnection() :
    # 오라클 연결하기
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    
    # 오라클 접속하기
    conn = ora.connect(user = 'busan_06', password = 'dbdb', dsn = dsn, encoding = 'utf-8')
    return conn

# 커서 받기
def getCursor(conn) :
    cursor = conn.cursor()
    return cursor

# 접속 정보 및 커서 반납하기
def dbclose(cursor, conn) :
    # 1.커서 반납
    cursor.close()
    # 2.접속정보 반납
    conn.close()
    
# 주문내역 전체 조회하기
# 여러 행에 대한 딕셔너리 만드는 함수
def getDictTypeFetchAll(col_name, row) :
    list_row = []
    
    for tup in row:
        dict_row = {}
        for i in range(len(tup)):
            dict_row[col_name[i].lower()] = tup[i]
        list_row.append(dict_row)
    
    return list_row

def getCartList() :
    conn = getConnection()
    cursor = getCursor(conn)
    sql = '''
          SELECT *
            FROM cart
          '''            
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    # 컬럼명 추출
    colname = cursor.description
    col = []
    for i in colname :
        col.append(i[0])  
        
    dict_row = getDictTypeFetchAll(col, row)
    
    dbclose(cursor, conn)
    
    return dict_row

# cart_member의 주문내역 전체 조회하기
def getCartMemberList(id):
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = '''
          SELECT *
            FROM cart
           WHERE cart_member = :cart_id
          '''
    cursor.execute(sql,cart_id= id)
    
    row = cursor.fetchall()
    
    dbclose(cursor, conn)
    
    return row


# 주문내역 상세(1건) 조회하기
# 한건 행에 대한 딕셔너리 만드는 함수
def getDictTypeFetchOne(col_name, row_one) :
    dict_row = {}
    
    for i in range(len(row_one)):
        dict_row[col_name[i].lower()] = row_one[i]
    
    return dict_row

# 주문내역 상세 조회하기 함수
def getCart(no, prod) :
    conn = getConnection()
    cursor = getCursor(conn)
    sql = '''
          SELECT *
            FROM cart
           WHERE cart_no = :cart_no
             AND cart_prod = :cart_prod
          '''            
    cursor.execute(sql, cart_no=no, cart_prod=prod)
    
    row = cursor.fetchone()
    # 컬럼명 추출
    colname = cursor.description
    col = []
    for i in colname :
        col.append(i[0])  
        
    dict_row = getDictTypeFetchOne(col, row)
    
    dbclose(cursor, conn)
    
    return dict_row

# 주문내역 입력하기
def setCartInsert(id, prod, qty, desc):
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문번호 생성을 위한 sql문 작성
    sql = '''SELECT DECODE(SUBSTR(MAX(cart_no), 1,8),
                TO_CHAR(SYSDATE,'YYYYMMDD'),
                MAX(cart_no)+1,        
                TO_CHAR(SYSDATE,'YYYYMMDD') ||'00001') as max_no
                FROM cart'''
    # 정렬시 SQL문 추가
    if desc == True:            
        sql +=  ''' ORDER BY mem_id DESC
            '''
                       
    cursor.execute(sql)
    
    max_no = cursor.fetchone()
    no = max_no[0]
    
    # 주문내역 입력을 위한 sql문 작성
    sql = '''INSERT INTO cart(cart_member,cart_no,cart_prod,cart_qty) 
             VALUES (:cart_member, :cart_no, :cart_prod, :cart_qty)'''
    cursor.execute(sql, cart_member = id, 
                        cart_no = no, 
                        cart_prod= prod,
                        cart_qty= qty)
    conn.commit()
    dbclose(cursor, conn)
    
    return 'Y'

# 주문내역 입력하기
def setCartDelete(no, prod):
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문내역 입력을 위한 sql문 작성
    sql = '''DELETE FROM cart
              WHERE cart_no = :cart_no
                AND cart_prod = :cart_prod
          '''
    cursor.execute(sql, cart_no = no, cart_prod= prod)
    conn.commit()
    dbclose(cursor, conn)
    
    return 'Y'

def setCartUpdate(no, prod, qty):
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문내역 입력을 위한 sql문 작성
    sql = '''UPDATE cart 
                SET cart_qty = :cart_qty
              WHERE cart_no = :cart_no
                AND cart_prod = :cart_prod
          '''
    cursor.execute(sql, 
                   cart_no = no, 
                   cart_prod= prod,
                   cart_qty= qty)
    conn.commit()
    dbclose(cursor, conn)
    
    return 'Y'