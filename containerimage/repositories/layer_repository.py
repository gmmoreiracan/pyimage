from containerimage.repositories.repository import Repository
from containerimage.models.layer import Layer


class LayerRepository(Repository):
    def __init__(self):
        super().__init__('layers')

    @staticmethod
    def get_layer_instance(layer):
        return Layer(
            image_ids=layer["image_ids"],
            media_type=layer["media_type"],
            size=layer["size"],
            digest=layer["digest"],
            command=layer["command"]
        )

    def create_layer(self, input_layer):
        layer = Layer(**input_layer)

        layer_res = self.find_layer(layer.media_type, layer.digest)

        if len(layer_res) > 0:
            return layer_res[0].doc_id

        return self.create(layer.__dict__)

    def find_layers_by_media_type(self, media_type):
        return [Layer(**data) for data in self.read(self.get_query().media_type == media_type)]

    def get_layer(self, media_type, digest):
        layer_query = self.get_query()
        return [Layer(**data) for data in self.read(
            (layer_query.media_type == media_type) & (layer_query.digest == digest)
        )]

    def find_layer(self, media_type, digest):
        layer_query = self.get_query()
        return self.read(
            (layer_query.media_type == media_type) & (layer_query.digest == digest)
        )

    def get_layer_id(self, layer_id):
        layer = self.get_id(layer_id)
        if layer is None or len(layer) == 0:
            return None

        return self.get_layer_instance(layer)

    def add_image_to_layer(self, layer_id, image_id):
        layer = self.get_layer_id(layer_id)
        if layer is None:
            return None

        if image_id in layer.image_ids:
            return None

        layer.image_ids.append(image_id)

        return self.update_id(layer_id, {"image_ids": layer.image_ids})
