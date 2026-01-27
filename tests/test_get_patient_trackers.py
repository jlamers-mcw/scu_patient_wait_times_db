import pytest

from src.get_patient_trackers import authenticate_box, find_folder_by_path

def test_authenticate_box():
    """
    Test to ensure that authenticate_box() can connect
    """

    client = authenticate_box()

    assert True


def test_find_folder_by_path_SCU():
    """
    Test to ensure that FFBP can get the name of folder in root
    """
    client = authenticate_box()

    folder = find_folder_by_path(client,[ "SCU" ])

    assert "SCU" == folder.get().name
