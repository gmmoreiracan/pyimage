from containerimage.repositories.repository import Repository
from containerimage.models.variable import EnvironmentVariable


class EnvironmentVariableRepository(Repository):
    def __init__(self):
        super().__init__('environment_variables')

    def create_environment_variable(self, input_variable):
        variable = EnvironmentVariable(**input_variable)

        var_result = self.find_variable(variable.key, variable.value)

        if len(var_result) > 0:
            return var_result[0].doc_id

        return self.create(variable.__dict__)

    def get_variable_id(self, var_id):
        var = self.get_id(var_id)
        if var is None or len(var) == 0:
            return None

        return self.get_variable_instance(var)

    def find_variables_by_key(self, key):
        return [EnvironmentVariable(**data) for data in self.read(self.get_query().key == key)]

    def get_variable(self, key, val):
        variable_query = self.get_query()
        return [
            EnvironmentVariable(**data) for data in self.read(
                (variable_query.key == key) & (variable_query.value == val)
            )
        ]

    def find_variable(self, key, val):
        variable_query = self.get_query()
        return self.read(
            (variable_query.key == key) & (variable_query.value == val)
        )

    def add_image_to_variable(self, variable_id, image_id):
        variable = self.get_variable_id(variable_id)

        if variable is None:
            return None

        if image_id in variable.image_ids:
            return None

        variable.image_ids.append(image_id)
        self.update_id(variable_id, {"image_ids": variable.image_ids})

    @staticmethod
    def get_variable_instance(var):
        return EnvironmentVariable(
            image_ids=var["image_ids"],
            key=var["key"],
            value=var["value"]
        )
