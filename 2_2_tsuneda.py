import mysql.connector

try:
    cnx = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='python_application'
    )
    cursor = cnx.cursor()
    name = input('どの山を検索しますか：')
    params = ('%' + name + '%', '%' + name + '%')

    cursor.execute("SELECT * FROM mountain "
                   + "WHERE name LIKE %s OR kana LIKE %s", params)
    for record in cursor:
        print(record)
except mysql.connector.Error:
    print('DB操作エラー')
else:
    cnx.commit()
    cursor.close()
    cnx.close()
