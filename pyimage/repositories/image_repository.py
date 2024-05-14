from pyimage.repositories.repository import Repository
from pyimage.models.image import Image


class ImageRepository(Repository):
    def __init__(self):
        super().__init__('images')

    def create_image(self, input_data):
        image = Image(**input_data)

        image_result = self.find_image(image.repo_digest, image.local_digest)

        if len(image_result) > 0:
            return image_result[0].doc_id

        return self.create(image.__dict__)

    def get_image_id(self, img_id):
        image = self.get_id(img_id)
        if image is None or len(image) == 0:
            return None

        return self.get_image_instance(image)

    def find_image_by_repo_digest(self, repo_digest):
        return [Image(**data) for data in self.read(self.get_query().repo_digest == repo_digest)]

    def get_image(self, repo_digest, local_digest):
        image_query = self.get_query()
        return [Image(**data) for data in self.read((
            image_query.repo_digest == repo_digest) | (image_query.local_digest == local_digest))
        ]

    def find_image(self, repo_digest, local_digest):
        image_query = self.get_query()
        return self.read((image_query.repo_digest == repo_digest) | (image_query.local_digest == local_digest))

    def find_image_by_local_digest(self, local_digest):
        return [Image(**data) for data in self.read(self.get_query().repo_digest == local_digest)]

    def find_image_by_repo(self, repo):
        return [Image(**data) for data in self.read(self.get_query().repo == repo)]

    def add_layer_to_image(self, image_id, layer_id):
        image = self.get_image_id(image_id)
        if image is None:
            return None

        if layer_id in image.layer_ids:
            return None

        image.layer_ids.append(layer_id)
        return self.update(self.get_query().doc_id == image_id, {"variable_ids": image.layer_ids})

    def add_variable_to_image(self, image_id, variable_id):
        image = self.get_image_id(image_id)
        if image is None:
            return None

        if variable_id in image.variable_ids:
            return None

        image.variable_ids.append(variable_id)
        return self.update_id(image_id, {"variable_ids": image.variable_ids})

    @staticmethod
    def get_image_instance(img):
        return Image(
            variable_ids=img["variable_ids"],
            layer_ids=img["layer_ids"],
            repo_digest=img["repo_digest"],
            local_digest=img["local_digest"],
            name=img["name"],
            tag=img["tag"],
            repo=img["repo"]
        )
