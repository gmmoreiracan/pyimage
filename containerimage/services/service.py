# services/image_service.py
from containerimage.repositories.image_repository import ImageRepository
from containerimage.repositories.layer_repository import LayerRepository
from containerimage.repositories.variable_repository import EnvironmentVariableRepository
from containerimage.schemas.image_schema import ImageSchema


class ImageService:
    def __init__(self):
        self.image_repo = ImageRepository()
        self.layer_repo = LayerRepository()
        self.variable_repo = EnvironmentVariableRepository()

    def create_image(self, image_data):
        # Validate input data
        image_schema = ImageSchema(**image_data)
        if image_schema:
            # Save image to repository
            image_stub = dict(image_schema)

            image_stub.pop("layers", None)
            image_stub.pop("variables", None)

            image_id = self.image_repo.create_image(image_stub)

            # Update references in associated layers and environment variables
            if hasattr(image_schema,"layers"):
                for layer_data in image_schema.__dict__['layers']:
                    layer_id = self.layer_repo.create_layer(layer_data)
                    self.layer_repo.add_image_to_layer(layer_id, image_id)
                    self.image_repo.add_layer_to_image(image_id, layer_id)

            if hasattr(image_schema,"variables"):
                for variable_data in image_schema.__dict__['variables']:
                    variable_id = self.variable_repo.create_environment_variable(variable_data)
                    self.variable_repo.add_image_to_variable(variable_id, image_id)
                    self.image_repo.add_variable_to_image(image_id, variable_id)

            return image_id
        else:
            # Handle validation errors
            raise ValueError("Invalid image data")

    # Other methods...
