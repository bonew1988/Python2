from pack import FileGenerator, FileRenamer


directory_to_create = "random_files"
num_files_to_create = 100
allowed_names = ['document', 'image', 'report', 'video']
allowed_extensions = ['txt', 'csv', 'doc', 'pdf', 'jpg', 'png']

FileGenerator.create_random_files(directory_to_create, num_files_to_create,
                                  allowed_names, allowed_extensions)

FileRenamer.rename_files(wanted_name="video", count_nums=3, extension_old=".txt",
                         extension_new=".csv", diapazon=[3, 6], directory="random_files")
