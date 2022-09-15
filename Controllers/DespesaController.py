import services.database as db
import models.Despesa as despesa

def Incluir(despesa):
    # st.warning('Essa merda não funciona', icon="⚠️")
    sql = "INSERT INTO despesa (banco, valor, finalidade, data, descricao) VALUES (%s, %s, %s, %s, %s)"
    val = (despesa.banco, despesa.valor, despesa.finalidade, despesa.data, despesa.descricao)
    db.cursor.execute(sql, val)
    db.db.commit()

def showAll():
    db.cursor.execute("SELECT * FROM despesa ORDER BY id_despesa DESC")
    lista = []

    for row in db.cursor.fetchall():
        lista.append(despesa.despesa(row[0], row[1], row[2], row[3], row[4], row[5]))
    return lista

def Deletar(id):
        db.cursor.execute(f"DELETE FROM despesa WHERE id_despesa = {id}")
        db.db.commit()

def showTotal():
        db.cursor.execute("SELECT COUNT(id_despesa) from despesa")
        conta = []

        for row in db.cursor.fetchall():
            conta.append(conta)
        return conta