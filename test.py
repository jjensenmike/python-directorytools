import directorytools as dt
import unittest
from os import getcwd

default_dir = getcwd() + "/testdata"
sub_dir = default_dir + "/secondlevel/thirdlevel1"

file_name = ["test.txt", default_dir + "/test.txt"]
file_names = ["test.csv", [default_dir + "/secondlevel/thirdlevel1/test.csv", default_dir + "/secondlevel/thirdlevel2/test.csv"]]
file_extension1 = ["zip", default_dir + "/secondlevel/test.zip"]
file_extension2 = ["tar.gz", default_dir + "/secondlevel/test.tar.gz"]
file_extensions = ["csv", [default_dir + "/secondlevel/thirdlevel1/test.csv", default_dir + "/secondlevel/thirdlevel2/test.csv"]]
file_partial = ["t.xml", default_dir + "/test.xml"]
file_partials = ["test.t", [default_dir + "/test.txt", default_dir + "/secondlevel/test.tar.gz"]]
missing_file = "test.txt"

folder_name = ["thirdlevel1", default_dir + "/secondlevel/thirdlevel1"]
folder_names = ["secondlevel", [default_dir + "/secondlevel"]]
folder_partial = ["second", default_dir + "/secondlevel"]
folder_partials = ["third", [default_dir + "/secondlevel/thirdlevel1", default_dir + "/secondlevel/thirdlevel2"]]
missing_folder = "fourthlevel"

default_file_list = [default_dir + "/test.txt", default_dir + "/test.xml", default_dir + "/secondlevel/test.zip", default_dir + "/secondlevel/test.tar.gz", default_dir + "/secondlevel/thirdlevel1/test.csv", default_dir + "/secondlevel/thirdlevel2/test.csv"]
sub_dir_file_list = [sub_dir + "/test.csv"]
default_folder_list = [default_dir + "/secondlevel", default_dir + "/secondlevel/thirdlevel1", default_dir + "/secondlevel/thirdlevel2"]

class TestDirectoryTools(unittest.TestCase):

    def testFileSearch(self):
        self.assertEqual(file_name[1], dt.file_by_name(file_name[0], default_dir))
        self.assertEqual(file_names[1], dt.files_by_name(file_names[0], default_dir))
        self.assertEqual(file_extension1[1], dt.file_by_extension(file_extension1[0], default_dir))
        self.assertEqual(file_extension2[1], dt.file_by_extension(file_extension2[0], default_dir))
        self.assertEqual(file_extensions[1], dt.files_by_extension(file_extensions[0], default_dir))
        self.assertEqual(file_partial[1], dt.file_by_partial(file_partial[0], default_dir))
        self.assertEqual(file_partials[1], dt.files_by_partial(file_partials[0], default_dir))
        self.assertIsNone(dt.file_by_name(missing_file, sub_dir))

    def testFolderSearch(self):
        self.assertEqual(folder_name[1], dt.folder_by_name(folder_name[0], default_dir))
        self.assertEqual(folder_names[1], dt.folders_by_name(folder_names[0], default_dir))
        self.assertEqual(folder_partial[1], dt.folder_by_partial(folder_partial[0], default_dir))
        self.assertEqual(folder_partials[1], dt.folders_by_partial(folder_partials[0], default_dir))
        self.assertIsNone(dt.folder_by_name(missing_folder, default_dir))

    def testLists(self):
        self.assertEqual(default_file_list, dt.file_list(default_dir))
        self.assertEqual(sub_dir_file_list, dt.file_list(sub_dir))
        self.assertEqual(default_folder_list, dt.folder_list(default_dir))
        self.assertIsNone(dt.folder_list(sub_dir))

if __name__ == '__main__':
	unittest.main()
