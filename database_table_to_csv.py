import MySQLdb

def solution(host, user, password, databse, tablename, filename):
    my_db = MySQLdb.connect(
        host=host,
        user=user,
        password=password,
        database=databse
    )
    my_cursor = my_db.cursor()

    with open(filename, "w") as file:
        my_cursor.execute("SHOW COLUMNS FROM "+tablename)
        title = [val[0] for val in my_cursor]
        print(",".join(title), file=file)

        my_cursor.execute("SELECT * FROM "+tablename)
        count_done = 0
        count_error = 0
        for val_1 in my_cursor:
            string = ""
            for val_2 in val_1:
                string += str(val_2) + ","
            string = string[:-1]

            """ Sometimes characters stored in database is not decode by python intepreter at that time it raised
                error and for solution of this problem we use try below """
            try:
                print(string, file=file)
                count_done += 1
            except Exception:
                count_error += 1

        print(count_done," : Record stored")
        print(count_error," : Record not stored")

# solution("localhost", "root", "", "imdb_db", "temp_table", "temp_generate.csv")