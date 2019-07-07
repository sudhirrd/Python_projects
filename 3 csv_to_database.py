import MySQLdb
import csv

def solution(host, user, password, databse, tablename, filename):
    my_db = MySQLdb.connect(
        host=host,
        user=user,
        password=password,
        database=databse
    )
    my_cursor = my_db.cursor()

    with open(filename, "r") as file:
        col_numbers = file.readline().split(",")
        col_numbers_1 = file.readline().strip("\n").split(",")

        col_types = ["INT(10)" if val.isnumeric() else "VARCHAR(255)" for val in col_numbers_1]

        query = "CREATE TABLE "+tablename+"("
        for val_1, val_2 in zip(col_numbers, col_types):
            query += "{} {},".format(val_1, val_2)
        query = query[:-1] + ")"

        my_cursor.execute(query)

        reader = csv.reader(file)
        next(reader)
        my_cursor.execute("LOAD DATA LOCAL INFILE '"+filename+"' INTO TABLE "+tablename+" FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS")
        my_db.commit()

# solution("localhost", "root", "", "imdb_db", "temp_table", "imdb.csv")
