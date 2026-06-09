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

    assert "SCU" == folder.name

def test_find_folder_by_path_Clinic_Operations():
    """
    Test to ensure that FFBP can get the name of folder CO
    """
    client = authenticate_box()

    folder = find_folder_by_path(client,[ "SCU", "Clinic Operations" ])

    assert "Clinic Operations" == folder.name

def test_find_folder_by_path_invalid_path():
    """
    Test to see if an error is thrown by FFBP when path is invalid
    """
    client = authenticate_box()

    with pytest.raises(ValueError):
        find_folder_by_path(client,[ "SCU", "Fake Folder" ])

def test_find_FFBP_2025_Trackers_enteries():
    """
    Tests to see if item names in 2025 Tracker folder match those
    found by FFBP
    """
    client = authenticate_box()

    folder = find_folder_by_path(client,[ 
                                         "SCU", 
                                         "Clinic Operations", 
                                         "Saturday Morning Materials",
                                         "Saturday Patient Visit Tracker",
                                         "2025 Trackers"
                                         ])
    file_names_in_2025_folder = [i.name for i in client.folders.get_folder_items(folder.id).entries]

    assert "Patient Visit Tracker (11.22.25).xlsx" in file_names_in_2025_folder
    assert "7.26.25 Patient Visit Tracker.xlsx" in file_names_in_2025_folder
    assert "8.24.25 Patient Visit Tracker BOOTCAMP EXAMPLE.xlsx" in file_names_in_2025_folder
