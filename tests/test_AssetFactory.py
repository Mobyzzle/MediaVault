from src.asset_factory import AssetFactory
from src.enums import MediaType
from pathlib import Path

hash = "cb1c558d20acdda00efa673899ad79d662626594ecf37b99ba403a16e31aa4bd"
def test_factory_creates_image_asset():
    row = {
        "id":1,
        "media_type":MediaType.IMAGE,
        "title":"Test_Image",
        "file_path":"testFile/test.png",
        "source_url":None,
        "width": 1920,
        "height":1080,
        "file_size": 420691337,
        "thumbnail_path": f"thumbnails/{hash}.webp",
        "aspect_ratio":"16:9",
        "file_hash": hash,

    }

    factory = AssetFactory()
    asset = factory.construct(MediaType.IMAGE,row)

    assert asset.title == "Test_Image"
    assert asset.file_size == 420691337
    assert asset.height == 1080
    assert asset.width == 1920
    assert asset.id == 1

if __name__ == "__main__":
    pass