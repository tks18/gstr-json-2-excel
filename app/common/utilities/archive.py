import shutil
from app.common.threader import threader


def archive_function(path_to_files, file_name):
    shutil.make_archive(base_name=file_name, format="zip", root_dir=path_to_files)
    shutil.rmtree(path_to_files)


def make_archive(path_to_files, file_name):
    archive_thread = threader(
        function=archive_function, path_to_files=path_to_files, file_name=file_name
    )
    archive_thread.start()
    archive_thread.join()
    if archive_thread.error is not None:
        raise archive_thread.error