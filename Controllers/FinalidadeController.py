import services.database as db
import models.Finalidade as finalidade

def Incluir(finalidade):
    # st.warning('Essa merda não funciona', icon="⚠️")
    sql = "INSERT INTO finalidade (nome_finalidade) VALUES (%s)"
    val = [finalidade.finalidade]
    db.cursor.execute(sql, val)
    db.db.commit()

def showAll():
    db.cursor.execute("SELECT * FROM finalidade")
    lista = []

    for row in db.cursor.fetchall():
        lista.append(finalidade.finalidade(row[0], row[1]))
    return lista

def Deletar(id):
        db.cursor.execute(f"DELETE FROM finalidade WHERE id_finalidade = {id}")
        db.db.commit()