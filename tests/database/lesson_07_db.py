from sqlalchemy.sql.expression import desc

from db import session
import tables


def test_db_is_work():
    result = session.query(tables.Person.id, tables.Person.first_name,
                           tables.Person.second_name).all()
    assert result is not None, "I've got a problem"


def test_db_filtering():
    result = session.query(tables.Person.id, tables.Person.first_name,
                           tables.Person.second_name).filter(tables.Person.id == 1)
    expected = (1, 'dima', 'kalugin')
    assert result[0] == expected, "I've got a problem"


def test_db_subquery():
    sub_result = session.query(tables.Person.id).filter(tables.Person.id > 1).filter(
        tables.Person.id < 3).subquery()
    result = session.query(tables.Person.first_name, tables.Person.second_name).filter(
        tables.Person.id.in_(sub_result))
    expected = ('denis', 'lavrentev')
    assert result[0] == expected, "I've got a problem"


def test_db_desc_sorting():
    result = session.query(tables.Person.id).order_by(desc(tables.Person.id)).all()
    result_list = []
    for i in result:
        result_list.append(i[0])
    expected = [3, 2, 1]
    assert result_list == expected, "I've got a problem"
