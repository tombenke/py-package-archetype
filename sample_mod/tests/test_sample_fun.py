"""Test the sample_mod module"""
import unittest

from sample_mod import sample_fun


class SampleModTestCase(unittest.TestCase):
    """The sample_mod test cases"""

    def test_sample_fun(self) -> None:
        """Test the sample_fun function"""
        self.assertEqual(
            "Hello py-package-archetype!", sample_fun("py-package-archetype")
        )
