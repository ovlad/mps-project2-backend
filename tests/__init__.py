import unittest

def fsuite():
    """Return a test suite that contains all tests."""
    
    from test.functional import test_register_functional
    from test.functional import test_roles_functional
    from test.functional import test_hospital_functional
    from test.functional import test_transfusion_center_functional
    from test.functional import test_login_functional
    
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_register_functional.suite())
    test_suite.addTest(test_roles_functional.suite())
    test_suite.addTest(test_hospital_functional.suite())
    test_suite.addTest(test_transfusion_center_functional.suite())
    test_suite.addTest(test_login_functional.suite())

    return test_suite

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(fsuite())
    return test_suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
