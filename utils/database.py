import mysql.connector
import pandas as pd

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kari9899@",
        database="health_db"
    )

def save_prediction(name, age, disease, risk):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO patients
    (name, age, disease, risk)
    VALUES (%s,%s,%s,%s)
    """

    values = (
        name,
        age,
        disease,
        float(risk)
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()


def get_patient_history():

    conn = connect_db()

    query = """
    SELECT *
    FROM patients
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df