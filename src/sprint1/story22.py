import unittest


class UniqueIDsValidator(unittest.TestCase):
    def test_empty(self):
        result = test_unique_ids(list())
        self.assertTrue(result)

    def test_another_type(self):
        result = test_unique_ids("Shivani Taneja")
        self.assertFalse(result)

    def test_null(self):
        result = test_unique_ids(None)
        self.assertFalse(result)

    def test_different_ids(self):
        result = test_unique_ids(['@I6000000122550124870@', '@I6000000122550879882@', '@I6000000122551057022@'])
        self.assertTrue(result)

    def test_some_similar_ids(self):
        result = test_unique_ids(['@I6000000122550124870@', '@I6000000122550879882@', '@I6000000122549932921@',
                                 '@I6000000122550124870@'])
        self.assertFalse(result)


def test_unique_ids(list_of_ids):
    if not isinstance(list_of_ids, list):
        return False

    if len(list_of_ids) == 0:
        return True

    print("The original list is : " + str(list_of_ids))

    # Refactored Code
    # using set() + len()
    # to check all unique list elements
    flag = len(set(list_of_ids)) == len(list_of_ids)

    return flag


def s22_test(duplicate_info, all_individuals_ids, all_families_ids, file):
    if not test_unique_ids(all_individuals_ids):
        for individual_id, list_of_names in duplicate_info['INDI'].items():
            if len(list_of_names) > 1:
                file.write(f'\nError US22: {len(list_of_names)} individuals named '
                           f'{list_of_names} are having same '
                           f'unique ID as {individual_id}\n')

    if not test_unique_ids(all_families_ids):
        for family_id, list_of_husband_ids in duplicate_info['FAM'].items():
            if len(list_of_husband_ids) > 1:
                file.write(f'\nError US22: {len(list_of_husband_ids)} families with husband ID '
                           f'{list_of_husband_ids} are having same '
                           f'unique ID as {family_id}\n')

    for individual_id, list_of_names in duplicate_info['INDI'].items():
        if individual_id in duplicate_info['FAM']:
            file.write(f'\nError US22: {individual_id} is being used by both individual and family.\n')

    return file


if __name__ == '__main__':
    unittest.main()
