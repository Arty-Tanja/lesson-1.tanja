from sqlalchemy import create_engine, inspect, text

my_connection = create_engine("postgresql://postgres:0000@localhost:5432/postgres")

sql_queries = {
    "insert": text("""INSERT INTO subject (subject_id, subject_title) VALUES
                    (:id, :title)"""),
    "update by id": text("""UPDATE subject SET subject_title = :title WHERE
                          subject_id = :id"""),
    "delete": text("DELETE FROM subject WHERE subject_id = :id"),
    "select max": text("SELECT MAX(subject_id) FROM subject"),
    "select by id": text("SELECT * FROM subject WHERE subject_id = :id")
}


def test_db_connection():
    insp = inspect(my_connection)
    names = insp.get_table_names()
    assert names[0] == "users"


def test_add_new():
    new_title = "chinese"
    with my_connection.connect() as conn:
        max_id = conn.execute(sql_queries["select max"])
        new_id = max_id.fetchall()[0][0] + 1
        conn.execute(sql_queries["insert"], [{"id": new_id, "title": new_title}])
        conn.commit()
        result = conn.execute(sql_queries["select by id"], [{"id": new_id}])
        assert result.fetchall()[0][1] == new_title
        conn.execute(sql_queries["delete"], [{"id": new_id}])
        conn.commit()


def test_updating():
    new_title = "korean"
    updated_title = "japanese"
    with my_connection.connect() as conn:
        max_id = conn.execute(sql_queries["select max"])
        new_id = max_id.fetchall()[0][0] + 1
        conn.execute(sql_queries["insert"], [{"id": new_id, "title": new_title}])
        conn.commit()
        conn.execute(sql_queries["update by id"],
                     [{"id": new_id, "title": updated_title}])
        conn.commit()
        result = conn.execute(sql_queries["select by id"], [{"id": new_id}])
        assert result.fetchall()[0][1] == updated_title
        conn.execute(sql_queries["delete"], [{"id": new_id}])
        conn.commit()


def test_deleting():
    new_title = "british english"
    with my_connection.connect() as conn:
        max_id = conn.execute(sql_queries["select max"])
        max_id_old = max_id.fetchall()[0][0]
        new_id = max_id_old + 1
        conn.execute(sql_queries["insert"], [{"id": new_id, "title": new_title}])
        conn.commit()
        conn.execute(sql_queries["delete"], [{"id": new_id}])
        conn.commit()
        max_id_again = conn.execute(sql_queries["select max"])
        assert max_id_again.fetchall()[0][0] == max_id_old
