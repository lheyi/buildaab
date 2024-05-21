import os
import shutil
import random
import string
import tempfile
from zipfile import ZipFile


def generate_file_name(min_len=5, max_len=12, suffix=""):
    """
    生成一个随机文件名。

    参数:
        min_len (int): 文件名最小长度。
        max_len (int): 文件名最大长度。
        suffix (str): 文件后缀。

    返回:
        str: 生成的文件名。
    """
    legal_chars = string.ascii_letters + string.digits + '_-'
    length = random.randint(min_len, max_len)
    return (''.join(random.choice(legal_chars) for _ in range(length))) + suffix


def create_zip_with_random_files(base_dir):
    """
    创建一个包含随机文件的.zip文件。

    参数:
        base_dir (str): 创建.zip文件的基础目录。

    返回:
        str: 生成的.zip文件的路径。
    """
    # 创建临时目录
    temp_dir = tempfile.mkdtemp(dir=base_dir)

    try:
        # 生成随机.zip文件名
        zip_file_name = generate_file_name(suffix=".zip")
        zip_file_path = os.path.join(base_dir, zip_file_name)

        # 创建.zip文件
        with ZipFile(zip_file_path, 'w') as zipf:
            for foldername, subfolders, filenames in os.walk(temp_dir):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    zipf.write(file_path, os.path.relpath(file_path, temp_dir))

    finally:
        # 清理临时目录
        shutil.rmtree(temp_dir)

    return zip_file_path
