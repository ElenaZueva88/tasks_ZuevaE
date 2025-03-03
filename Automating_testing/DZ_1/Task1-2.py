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
import string


def check_output_for_text(command, search_text, word_mode=False):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout

    if word_mode:
        out = out.translate(str.maketrans('', '', string.punctuation)).split()
        for element in out:
            print(element)

    if result.returncode == 0 and (search_text in out if word_mode else search_text in result.stdout):
        return True
    else:
        return False


if __name__ == '__main__':
    cmd = "cat /etc/os-release"
    search_txt = "LTS"
    is_successful = check_output_for_text(cmd, search_txt, word_mode=True)
    if is_successful:
        print(f'Команда "{cmd}" успешно выполнена, и слово "{search_txt}" найдено.')
    else:
        print("Команда не выполнена успешно или слово не найдено.")