import MySQLdb

def solution(host, user, password, databse,filename):
    my_db = MySQLdb.connect(
        host=host,
        user=user,
        password=password,
        database=databse
    )
    my_cursor = my_db.cursor()

    with open(filename, "r") as file:
        col_numbers = file.readline().split(",")

    if (col_numbers[0].isnumeric()):
        my_cursor.execute("CREATE TABLE temp_table({} INT(10)".format(col_numbers[0]))
    else:
        my_cursor.execute("CREATE TABLE temp_table({} VARCHAR(255)".format(col_numbers[0]))

    del col_numbers[0]
    for val in col_numbers:
        if(val.isnumeric()):
            my_cursor.execute("ALTER TABLE temp_table ADD {} INT(10)".format(val))
        else:
            my_cursor.execute("ALTER TABLE temp_table ADD {} VARCHAR(255)".format(val))


# solution("localhost", "root", "", "imdb_db", "temp.csv")