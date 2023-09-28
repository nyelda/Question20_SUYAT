import unittest

def check(name):
    return name == "PEDRO"


def MyTest(unittest):
    def test(self):
        self.assertEqual(check("Daniel"))

if __name__ == '__main__':
    unittest.main()