import tables


def test_get_data_person(get_db_session):
    """Get first person from tables.person"""
    data = get_db_session.query(tables.Person).first()
    print(f"First person in database is {data.first_name} {data.second_name}")


# def test_try_to_delete_data(get_db_session, get_delete_method):
#     """Delete row by id in tables.item_type"""
#     get_delete_method(get_db_session, tables.ItemType, (tables.ItemType.item_id == 3))

# def test_add_data_to_db(get_db_session, get_create_method):
#     """Create row in tables.item_type"""
#     data = {'item_type': "MY_NEW_TYPE"}
#     item = tables.ItemType(**data)
#     get_create_method(get_db_session, item)
#     print(item.item_id)


# def test_add_data_to_db_with_builder(get_db_session, get_create_method, get_item_type_generator):
#     """Create row in tables.item_type with builder"""
#     item = tables.ItemType(**get_item_type_generator.build())
#     get_create_method(get_db_session, item)
#     print(item.item_id)


def test_add_data_to_db_with_builder_and_delete(generate_item_type):
    print(f"Add & delete: {generate_item_type.item_id}, {generate_item_type.item_type}")




