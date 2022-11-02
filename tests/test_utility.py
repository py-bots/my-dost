from dost.utility import *
import sys
import unittest


sys.path.insert(0, 'dost')


class tests(unittest.TestCase):
    def test_pause(self):
        import time
        sleep_time=3
        start = time.time()
        pause_program(sleep_time)
        end = time.time()
        self.assertGreaterEqual(end - start, sleep_time)


    def test_clipboard_set(self):
        clipboard_set_data("Hello World")

    def test_clipboard_get(self):
        clipboard_set_data("Hello World")
        self.assertEqual(str(clipboard_get_data()), "Hello World")

    def test_formats(self):
        GetClipboardFormats()

    def test_clear(self):
        clear_output()

    def test_uninstall_module(self):
        uninstall_module("requests")

    def test_install_module(self):
        install_module("requests")

    def test_text_from_image(self):
        self.assertEqual(image_to_text("tests\demo2.png"), "File\n")


if __name__ == '__main__':
    unittest.main()
