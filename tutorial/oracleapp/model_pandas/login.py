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
    
# 한건 행에 대한 딕셔너리 만드는 함수
def getDictType_FetchOne(col_name, row_one) :
    dict_row = {}
    
    for i in range(len(row_one)):
        dict_row[col_name[i].lower()] = row_one[i]
    
    return dict_row



# 회원 상세 조회하기 - 1건 조회
def getMember(id) :
    conn = getConnection()
    cursor = getCursor(conn)
    sql = '''
          SELECT *
            FROM member
           WHERE mem_id = :mem_id
          '''            
    cursor.execute(sql, mem_id=id)
    
    row = cursor.fetchone()
    
    # 컬럼명 추출
    colname = cursor.description
    col = []
    for i in colname :
        col.append(i[0])  
        
    dict_row = getDictType_FetchOne(col, row)
    
    dbclose(cursor, conn)
    
    return dict_row

def getLogin(id,password) :
    conn = getConnection()
    cursor = getCursor(conn)
    sql = '''
          SELECT *
            FROM member
           WHERE mem_id = :mem_id
             AND mem_pass = :mem_pass
          '''            
    cursor.execute(sql, 
                   mem_id=id,
                   mem_pass = password)
    
    row = cursor.fetchone()
    
    # 로그인 정보가 없을때 (로그인 실패)
    if row == None :
        dbclose(cursor, conn)
        return{'rs' : 'no'}
    
    # 컬럼명 추출
    colname = cursor.description
    col = []
    for i in colname :
        col.append(i[0])  
        
    dict_row = getDictType_FetchOne(col, row)
    dict_row['rs'] = 'yes'
    
    dbclose(cursor, conn)
    
    return dict_row