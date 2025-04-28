import unittest
from src.widget import mask_account_card, get_date


class TestWidgetFunctions(unittest.TestCase):
    def test_mask_account_card(self):
        test_cases = [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Счет 73654108430135874305", "Счет **4305"),
            ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
            ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
            ("Счет 64686473678894779589", "Счет **9589"),
            ("Invalid", "Invalid"),
            ("", ""),
        ]

        for input_data, expected in test_cases:
            with self.subTest(input_data=input_data):
                self.assertEqual(mask_account_card(input_data), expected)

    def test_get_date(self):
        self.assertEqual(get_date("2024-03-11T02:26:18.671407"), "11.03.2024")
        self.assertEqual(get_date("invalid-date"), "invalid-date")


if __name__ == "__main__":
    unittest.main()