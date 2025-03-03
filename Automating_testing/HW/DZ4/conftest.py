import pytest
from sshcheckers import ssh_checkout, ssh_getout
import random, string
import yaml
from datetime import datetime


with open('config.yaml') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def create_folders():
    return ssh_checkout(data["ip"], data["user"], data["passwd"], "mkdir {} {} {} {}".format(data["folder_in"], data["folder_in"], data["folder_ext"], data["folder_ext2"]), "")


@pytest.fixture()
def clear_folders():
    return ssh_checkout(data["ip"], data["user"], data["passwd"], "rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_in"], data["folder_ext"], data["folder_ext2"]), "")

@pytest.fixture()
def create_files():
    list_of_files = [ ]
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=data["len_name"]))
        if ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"], filename, data["bs"]), ""):
            list_of_files.append(filename)
    return list_of_files

@pytest.fixture()
def create_subfolder():
    test_file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=data["len_name"]))
    sub_folder_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=data["len_name"]))
    if not ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; mkdir {}".format(data["folder_in"], sub_folder_name), ""):
        return None, None
    if not ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"], sub_folder_name, test_file_name), ""):
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
    stat = ssh_getout(data["ip"], data["user"], data["passwd"],"cat /proc/loadavg")
    ssh_checkout(data["ip"], data["user"], data["passwd"], "echo 'time: {} count:{} size: {} load: {}'>> stat.txt".format(datetime.now().strftime("%H:%M:%S.%f"), data["count"], data["bs"], stat), "")

@pytest.fixture()
def start_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")