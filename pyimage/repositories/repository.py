from pyimage.database.database import Database


class Repository:
    def __init__(self, table):
        self.table = Database("image_db.json").get_table(table)

    def get_id(self, id_input):
        return self.table.get(doc_id=id_input)

    def create(self, data):
        return self.table.insert(data)

    def read(self, query):
        return self.table.search(query)

    def update(self, query, data):
        return self.table.update(data, query)

    def update_id(self, table_id, data):
        return self.table.update(data, doc_ids=[table_id])

    def delete(self, query):
        return self.table.remove(query)

    @staticmethod
    def get_query():
        return Database.get_query()
