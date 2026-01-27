import psycopg
conninfo = "dbname=postgres user=postgres password=Naveen_2026@ host=127.0.0.1 port=5432"
with psycopg.connect(conninfo) as conn:
    with conn.cursor() as curr:
        curr.execute("select version()")
        for row in curr.fetchall():
            print(row)