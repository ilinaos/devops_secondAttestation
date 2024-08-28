import psycopg2 as ps

conn = None
try:
    conn = ps.connect(
        dbname="ilina",
        user="postgres",
        password="password",
        host="db",
        port="5432"
    )

    cur = conn.cursor()

    query_min = """SELECT name, surname, age, city 
                    FROM test_table 
                    WHERE length(name) < 6 
                    ORDER BY age 
                    LIMIT 1"""
    query_max = """SELECT name, surname, age, city 
                    FROM test_table 
                    WHERE length(name) < 6 
                    ORDER BY age DESC
                    LIMIT 1"""

    cur.execute(query_min)
    min_age_person = cur.fetchone()
    cur.execute(query_max)
    max_age_person = cur.fetchone()
    print("Запись с минимальным возрастом:\n", *min_age_person)
    print("Запись с максимальным возрастом:\n", *max_age_person)

except (Exception, ps.Error) as error:
    print(error)


finally:
    if conn:
        conn.close()
