import services.database as db
import models.Banco as banco

def Incluir(banco):
    # st.warning('Essa merda não funciona', icon="⚠️")
    sql = "INSERT INTO banco (nome_banco) VALUES (%s)"
    val = [banco.banco]
    db.cursor.execute(sql, val)
    db.db.commit()

def showAll():
    db.cursor.execute("SELECT * FROM banco")
    lista = []

    for row in db.cursor.fetchall():
        lista.append(banco.banco(row[0], row[1]))
    return lista

def Deletar(id):
        db.cursor.execute(f"DELETE FROM banco WHERE id_banco = {id}")
        db.db.commit()