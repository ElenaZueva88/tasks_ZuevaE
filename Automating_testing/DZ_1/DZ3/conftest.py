import pytest
from checkers import checkout, getout
import random, string
import yaml
from datetime import datetime

with open('config.yaml') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def create_folders():
    return checkout("mkdir {} {} {} {}".format(data["folder_in"], data["folder_in"], data["folder_ext"], data["folder_ext2"]), "")


@pytest.fixture()
def clear_folders():
    return checkout("rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_in"], data["folder_ext"], data["folder_ext2"]), "")

@pytest.fixture()
def create_files():
    list_of_files = [ ]
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=data["len_name"]))
        if checkout("cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"], filename, data["bs"]), ""):
            list_of_files.append(filename)
    return list_of_files

@pytest.fixture()
def create_subfolder():
    test_file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=data["len_name"]))
    sub_folder_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=data["len_name"]))
    if not checkout("cd {}; mkdir {}".format(data["folder_in"], sub_folder_name), ""):
        return None, None
    if not checkout("cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"], sub_folder_name, test_file_name), ""):
        return sub_folder_name, None
    else:
        return sub_folder_name, test_file_name

@pytest.fixture(autouse=True)
def print_time():
    print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield
    print("Finish: {}".format(datetime.now().strftime("%H:%M:%S.%f")))

@pytest.fixture(autouse=True)
def stat():
    yield
    stat = getout("cat /proc/loadavg")
    checkout("echo 'time: {} count:{} size: {} load: {}'>> stat.txt".format(datetime.now().strftime("%H:%M:%S.%f"), data["count"], data["bs"], stat), "")