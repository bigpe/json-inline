from unittest import TestCase
import json_inline


class JsonInlineTestCase(TestCase):

    def test_entrypoint_move_by_key(self):
        success = 'success'
        test_struct = {
            'step1': {
                'step2': {
                    'step3': success
                }
            }
        }
        fetch_rule = 'step1.step2.step3'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_list_search_by_key(self):
        success = 'success'
        test_struct = [
                {'item1': 'fail'},
                {'item2': success},
                {'item3': 'fail'}
            ]
        fetch_rule = '?item2.item2'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_list_search_by_key_with_entry_inside(self):
        success = 'success'
        test_struct = [
            {'item1': 'fail'},
            {'item2': success},
            {'item3': 'fail'}
        ]
        fetch_rule = '?+item2'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_list_search_by_key_with_entry_number(self):
        success = 'success'
        test_struct = [
            {'item1': 'fail'},
            {'item2': 'fail'},
            {'item2': success},
            {'item3': 'fail'}
        ]
        fetch_rule = '?item2#2.item2'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_list_search_by_key_with_entry_number_with_entry_inside(self):
        success = 'success'
        test_struct = [
            {'item1': 'fail'},
            {'item2': 'fail'},
            {'item2': success},
            {'item3': 'fail'}
        ]
        fetch_rule = '?+item2#2'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_entrypoint_move_by_index(self):
        success = 'success'
        test_struct = [
            {'item1': 'fail'},
            {'item2': 'fail'},
            {'item2': success},
            {'item3': 'fail'}
        ]
        fetch_rule = '#2.item2'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_list_search_by_key_value(self):
        success = {'item2': 'success'}
        test_struct = [
            {'item1': 'fail'},
            {'item2': 'fail'},
            success,
            {'item3': 'fail'}
        ]
        fetch_rule = '?item2:success'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_list_search_by_key_value_with_entry_number(self):
        success = {'item2': 'success', 'something': 'else'}
        test_struct = [
            {'item1': 'fail'},
            {'item2': 'fail'},
            {'item2': 'success'},
            success,
            {'item3': 'fail'}
        ]
        fetch_rule = '?item2:success#2'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_hardcore(self):
        success = 'success'
        test_struct = [
            {'item1': 'fail'},
            {'item2': 'fail'},
            {'item2': [
                {'item4': 'fail'},
                {'item4': 'fail'},
                {'item5': [
                    {'item7': 'fail'},
                    {'item7': 'fail', 'item9': [
                        {'item10': 'fail'},
                        {'item10': 'fail'},
                        {'item10': 'fail'},
                        {'item10': 'fail'},
                        {'item10': success},
                    ]},
                    {'item8': 'fail'},
                ]},
                {'item5': 'fail'},
                {'item6': 'fail'},
            ]},
            {'item3': 'fail'}
        ]
        fetch_rule = '?+item2#2.?+item5.?item7:fail#2.item9.#4.item10'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_result_not_found(self):
        success = None
        test_struct = [
            {'item1': 'fail'},
            {'item2': 'fail'},
            {'item2': [
                {'item4': 'fail'},
                {'item4': 'fail'},
                {'item5': [
                    {'item7': 'fail'},
                    {'item7': 'fail', 'item9': [
                        {'item10': 'fail'},
                        {'item10': 'fail'},
                        {'item10': 'fail'},
                        {'item10': 'fail'},
                        {'item10': 'fail'},
                    ]},
                    {'item8': 'fail'},
                ]},
                {'item5': 'fail'},
                {'item6': 'fail'},
            ]},
            {'item3': 'fail'}
        ]
        # First Entry (with entry into item2 by key) item2 is string, movement forward restricted
        fetch_rule = '?+item2#1.?+item5.?item7:fail#2.item9.#4.item10'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_list_index_error(self):
        success = None
        test_struct = [
            {'item1': 'fail'},
            {'item2': 'fail'},
            {'item2': 'fail'},
            {'item3': 'fail'}
        ]
        # Try move to not exist list index
        fetch_rule = '#6'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_list_search_key_not_found(self):
        success = None
        test_struct = [
            {'item1': 'fail'},
            {'item2': 'fail'},
            {'item2': 'fail'},
            {'item3': 'fail'}
        ]
        # Try to find not exist key
        fetch_rule = '?item5'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)

    def test_dict_move_to_not_exist_key(self):
        success = None
        test_struct = [
            {'item1': 'fail'},
            {'item2': 'fail'},
            {'item2': 'fail'},
            {'item3': 'fail'}
        ]
        # Try to find not exist key
        fetch_rule = '?item1.item2'
        result = json_inline.fetch(test_struct, fetch_rule)
        self.assertEqual(result, success)



