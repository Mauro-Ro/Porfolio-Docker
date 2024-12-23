import sqlite3 as sql

DATABASE = 'formulario.db'

def create_db():
    with sql.connect(DATABASE) as conn:
        pass



def create_table():
    with sql.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE formulario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            asunto TEXT,
            mensaje TEXT
            )"""
        )
        conn.commit()


def delete_rows(user):
    with sql.connect(DATABASE) as conn:
        cursor = conn.cursor()
        delete = "DELETE FROM formulario WHERE nombre=?"
        cursor.execute(delete, (user,))
        conn.commit()
        print(f"se ah eliminado al usuario {user}")
    