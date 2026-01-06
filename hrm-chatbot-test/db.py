import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=94.249.213.113,1433;"
        "DATABASE=uatclientsmp;"
        "UID=ReadOnlyUser;"
        "PWD=tester#123;"
        "Encrypt=no;"
    )
    return conn


def run_query(sql, params=None):
    conn = get_connection()
    cursor = conn.cursor()

    if params:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)

    rows = cursor.fetchall()
    conn.close()
    return rows
