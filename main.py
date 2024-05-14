# main.py
from pyimage import ImageService

if __name__ == "__main__":
    # Create an instance of ImageService
    image_service = ImageService()

    # Example image data
    image_data = {
        'repo_digest': '12345',
        'local_digest': '67890',
        'repo': 'example_repo',
        'name': 'example_image',
        'tag': 'latest',
        'layers': [
            {'media_type': 'type1', 'size': 100, 'command': 'cmd1', 'digest': 'digest1'},
            {'media_type': 'type2', 'size': 200, 'command': 'cmd2', 'digest': 'digest2'}
        ],
        'variables': [
            {'key': 'key1', 'value': 'value1'},
            {'key': 'key2', 'value': 'value2'}
        ]
    }

    # Create an image using ImageService
    image_id = image_service.create_image(image_data)
    print(f"Image created with ID: {image_id}")
