from pathlib import Path
from src.media_repository import MediaRepository
from src.assets import ImageAsset, MediaAsset
from src.enums import MediaType
from src.asset_factory import AssetFactory
hash = "cb1c558d20acdda00efa673899ad79d662626594ecf37b99ba403a16e31aa4bd"

def test_repository_initializes_temporary_databse(tmp_path):
    db_path = tmp_path / "test.db"

    repository = MediaRepository(db_path)

    assert db_path.exists()



def test_repository_returns_inserted_data(tmp_path):

    db_path = tmp_path / "test.db"

    repository = MediaRepository(db_path)   

    asset = ImageAsset(
        title="Test Image",
        media_type=MediaType.IMAGE,
        file_path=Path("tests/test_image.jpg"),
        width=69,
        height=420,
        thumbnail_path="test_thumbnail/test.png",
        aspect_ratio="2:3",
        file_hash=hash
    )

    stored_asset = repository.insert_asset(asset)

    assert stored_asset["id"] == 1
    assert stored_asset["date_added"] is not None
    assert stored_asset["favourite"] == 0
    assert stored_asset["height"] == 420
    assert stored_asset["width"] ==  69
    assert isinstance(stored_asset["file_path"],str)

