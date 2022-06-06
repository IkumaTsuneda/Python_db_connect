import mysql.connector

try:
    cnx = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='python_application'
    )
    cursor = cnx.cursor()
    name = input('山名を入力してください。：')
    kana = input('山名の読み仮名を入力してください。：')
    height = input('標高を入力してください。：')
    location = input('場所を入力してください。')
    params = (name, kana, height, location)

    cursor.execute("INSERT INTO mountain (name, kana, height, location) "
                   + "VALUE (%s, %s, %s, %s)", params)
    for record in cursor:
        print(record)
except mysql.connector.Error:
    print('DB操作エラー')
else:
    cnx.commit()
    cursor.close()
    cnx.close()
