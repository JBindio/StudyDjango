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

# 여러 행에 대한 딕셔너리 만드는 함수
def getDictTypeFetchAll(row,col_list) :
    
    list_dict_row = []
    for tup in row:
        dict_row = {}
        for i in range(len(tup)):
            dict_row[col_list[i].lower()] = tup[i]
        list_dict_row.append(dict_row)
        
    return list_dict_row
    
    
# 주문내역 전체 조회하기
def getLprodList():
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = '''
          SELECT *
            FROM lprod
          '''
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    # 컬럼 추출
    colname = cursor.description
    col = []
    for i in colname :
        col.append(i[0]) 
    
    dbclose(cursor, conn)
    
    list_dict_row = getDictTypeFetchAll(row,col)
    
    return list_dict_row

# 주문내역 상세(1건) 조회하기
# 한건 행에 대한 딕셔너리 만드는 함수

def getDictTypeFetchOne(col_list,row):
    dict_row = {}
    for i in range(len(row)):
        dict_row[col_list[i].lower()] = row[i]
    
    return dict_row

# 주문내역 상세 조회하기 함수
def getLprod(id) :
    conn = getConnection()
    cursor = getCursor(conn)
    sql = '''
          SELECT *
            FROM lprod
           WHERE lprod_gu = :lprod_pk
          '''            
    cursor.execute(sql, lprod_pk=id)
    
    row = cursor.fetchone()
    # 컬럼명 추출
    colname = cursor.description
    col = []
    for i in colname :
        col.append(i[0])  
        
    dict_row = getDictTypeFetchOne(col, row)
    
    dbclose(cursor, conn)
    
    return dict_row