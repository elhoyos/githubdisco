import unittest
from unittest.mock import patch
from tracesets import TRACESETS, traces_in_template, regexps

class TestTraceSets(unittest.TestCase):
    
    def test_traces_in_template(self):
        traceset = {
            'traces': [
                {
                    'foo': 'bar'
                },
                {
                    'baz': 'bar'
                },
            ]
        }

        values = [value for value in traces_in_template(traceset, '${bar}')]
        self.assertSequenceEqual(values, [])

    def test_traces_in_template_unique_values(self):
        traceset = {
            'traces': [
                {
                    'foo': 'bar'
                },
                {
                    'baz': 'bar'
                },
            ]
        }

        values = [value for value in traces_in_template(traceset, '${foo}')]
        self.assertSequenceEqual(values, ['bar'])

    @patch('matchers.MATCHERS', {
        'my_lang_family': [
            {
                'file_descriptors': ['txt'],
                'descriptors_type': 'extension',
                'template': '${foo}',
            },
        ]
    })
    def test_regexps(self):
        traceset = {
            'lang_family': 'my_lang_family',
            'traces': [
                {
                    'foo': 'bar',
                    'baz': 'no_problem'
                },
            ]
        }

        regular_expressions = [regexp for regexp in regexps(traceset, ['txt'])]
        self.assertSequenceEqual(regular_expressions, [r'bar'])

    @patch('matchers.MATCHERS', {
        'my_lang_family': [
            {
                'file_descriptors': ['java'],
                'descriptors_type': 'extension',
                'template': '${foo}',
            },
        ]
    })
    def test_regexps_diff_file_descriptor(self):
        traceset = {
            'lang_family': 'my_lang_family',
            'traces': [
                {
                    'foo': 'bar'
                },
            ]
        }

        regular_expressions = [regexp for regexp in regexps(traceset, ['txt'])]
        self.assertSequenceEqual(regular_expressions, [])

    @patch('matchers.MATCHERS', {
        'my_lang_family': [
            {
                'file_descriptors': ['java', 'txt'],
                'descriptors_type': 'extension',
                'template': '${foo}',
            },
        ]
    })
    def test_regexps_secondary_file_descriptor(self):
        traceset = {
            'lang_family': 'my_lang_family',
            'traces': [
                {
                    'foo': 'bar'
                },
            ]
        }

        regular_expressions = [regexp for regexp in regexps(traceset, ['txt'])]
        self.assertSequenceEqual(regular_expressions, [r'bar'])


if __name__ == '__main__':
    unittest.main()