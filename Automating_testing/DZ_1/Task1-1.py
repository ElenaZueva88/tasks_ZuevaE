# Содержимое файла /etc/os-release:
# PRETTY_NAME="Ubuntu 22.04.4 LTS"
# NAME="Ubuntu"
# VERSION_ID="22.04"
# VERSION="22.04.4 LTS (Jammy Jellyfish)"
# VERSION_CODENAME=jammy
# ID=ubuntu
# ID_LIKE=debian
# HOME_URL="https://www.ubuntu.com/"
# SUPPORT_URL="https://help.ubuntu.com/"
# BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
# PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
# UBUNTU_CODENAME=jammy

import subprocess


def check_output_for_text(command, search_text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0 and search_text in out:
        return True
    else:
        return False


if __name__ == '__main__':
    cmd = "cat /etc/os-release"
    search_txt = 'PRETTY_NAME="Ubuntu 22.04.4 LTS"'
    is_successful = check_output_for_text(cmd, search_txt)
    if is_successful:
        print(f'Команда "{cmd}" успешно выполнена, и текст "{search_txt}" найден.')
    else:
        print("Команда не выполнена успешно или текст не найден.")
