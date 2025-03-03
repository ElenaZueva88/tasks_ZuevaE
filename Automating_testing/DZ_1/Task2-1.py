import subprocess

folder_in = "/home/vp/zerg/tst"
folder_out = "/home/vp/zerg/out"
folder_ext = "/home/vp/zerg/folder1"
sub_folder = "/home/vp/zerg/subfolder"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # Проверка добавления файлов в архив и наличие самого файла с архивом в указанной папке
    res1 = checkout("cd {}; 7z a {}/arx4.7z".format(folder_in, folder_out), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_out), "arx4.7z")
    assert res1 and res2, "test1 - файлы не добавлены в архив или файл с архивом отсутствует в указанной папке"


def test_step2():
    # Проверка распаковки архива и наличие распакованных файлов в указанной папке
    res1 = checkout("cd {}; 7z e arx4.7z -o{} -y".format(folder_out, folder_ext), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_ext), "test1.txt")
    res3 = checkout("ls {}".format(folder_ext), "test2.txt")
    res4 = checkout("ls {}".format(folder_ext), "test3.txt")
    assert res1 and res2 and res3 and res4, "test2 -  ошибка распаковки архива или распакованные файлы отсутствуют в указанной папке"


def test_step3():
    # Проверка тестирование архива на целостность
    assert checkout("cd {}; 7z t arx4.7z".format(folder_out), "Everything is Ok"), "test3 - целостность архива нарушена"


def test_step4():
    # Проверка вывода списка файлов в архиве
    file_names = ["test1.txt", "test2.txt", "test3.txt"]
    all_files_present = True

    for file_name in file_names:
        res = checkout("cd {}; 7z l arx4.7z".format(folder_out), file_name)
        all_files_present = all_files_present and res
        if not res:
            break

    assert all_files_present, "test4 - не все файлы были найдены в архиве"


def test_step5():
    # Проверка разархивирования файлов с сохранением путей
    res1 = checkout("cd {}; 7z x arx5.7z -o{} -y".format(folder_out, sub_folder), "Everything is Ok")
    res2 = checkout("ls {}".format(sub_folder), "test4.txt")
    res3 = checkout("ls {}/sub1".format(sub_folder), "test1.txt")
    res4 = checkout("ls {}/sub2".format(sub_folder), "test2.txt")
    res5 = checkout("ls {}/sub2".format(sub_folder), "test3.txt")
    assert res1 and res2 and res3 and res4 and res5, "test5 - разархивация с сохранением путей не удалась"


def test_step6():
    # Проверка расчета хеша архива и его сравнение с ожидаемым значением команды crc32
    com_7z = "7z h -scrcCRC32 {}/arx4.7z | grep CRC32 | awk '{{print $4}}'".format(folder_out)
    result = subprocess.run(com_7z, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    md_hash = result.stdout.strip().upper()

    com_crc32 = "crc32 {}/arx4.7z".format(folder_out)
    result = subprocess.run(com_crc32, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    res_hash = result.stdout.strip().upper()

    assert res_hash == md_hash, "test6 - расчет хеша файла не совпадает с ожидаемым значением"
