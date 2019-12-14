# pylint: disable=anomalous-backslash-in-string

import re
from string import Template

MATCHERS = {
    # Each key represents a language family
    # The language family is a string in which each language
    # is separated by a comma.
    'C#,Visual Basic': [
        {
            'file_descriptors': ['json'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': 'dependencies":[\S\W]*"${package_name}"',
                    'prefixes': ['dependencies'],
                }
            ],
        },
        {
            'file_descriptors': ['config'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': '(?i:<package\s*id=)"${package_name}',
                    'prefixes': ['package'],
                },
            ],
        },
        {
            'file_descriptors': ['csproj', 'vbproj'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': '(?i:<PackageReference\s*Include=|<Reference\s*Include=)"${package_name}',
                    'prefixes': ['Reference'],
                },
            ],
        },
    ],
    'Go': [
        {
            'file_descriptors': ['go'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': '(?i)${import_or_usage}',
                    'prefixes': ['import'],
                },
            ],
        },
    ],
    'Java,Kotlin': [
        {
            'file_descriptors': ['gradle', 'gradle.kts'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': '${artifact_name}',
                    'prefixes': [''], # No prefixes, artifact names are specific enough
                },
            ],
        },
        {
            'file_descriptors': ['java'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': 'import.+${import_or_usage}',
                    'prefixes': ['import'],
                },
            ],
        },
        {
            'file_descriptors': ['xml'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': '(?i:groupid>${group_id}<\/groupid>\s+<artifactid>${artifact_id}<\/artifactid>)',
                    'prefixes': ['groupid'],
                },
            ],
        },
    ],
    'JavaScript,TypeScript': [
        {
            'file_descriptors': ['json'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': '(?:devDependencies|dependencies)":[\S\W]*"${artifact_name}"',
                    'prefixes': ['dependencies'],
                },
            ],
        },
        {
            'file_descriptors': ['js', 'jsx', 'ts', 'tsx'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': '(?:require.+|import.+|from.+)(?:"|\')${artifact_name}(?:"|\')',
                    'prefixes': ['require', 'import', 'from'],
                },
            ],
        },
    ],
    'Objective-C,Swift': [
        {
            'file_descriptors': ['Podfile'],
            'descriptors_type': 'filename',
            'templates': [
                {
                    'template': 'pod (?:`|\'|")${artifact_name}(?:`|\'|")',
                    'prefixes': ['pod'],
                },
            ],
        },
        {
            'file_descriptors': ['Cartfile'],
            'descriptors_type': 'filename',
            'templates': [
                {
                    'template': 'github "${artifact_name}"',
                    'prefixes': ['github'],
                },
            ],
        },
        {
            'file_descriptors': ['m', 'h', 'swift'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': '#?(?:import|include) "?${import_or_usage}"?',
                    'prefixes': ['import', 'include'],
                },
            ],
        },
    ],
    'PHP': [
        {
            'file_descriptors': ['json'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': 'require":[\S\W]*"${artifact_name}"',
                    'prefixes': ['require'],
                },
            ],
        },
        {
            'file_descriptors': ['php'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': '(?:use|new) ${import_or_usage}',
                    'prefixes': ['use', 'new'],
                },
            ],
        },
    ],
    'Python': [
        {
            'file_descriptors': ['py'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': 'install_requires=[\S\W]*(?:"|\')${artifact_name}(?:\[|\s+|~|=|>|<|!|"|\')',
                    'prefixes': ['install_requires'],
                },
                {
                    'template': '(?:import ${import_or_usage}|from ${import_or_usage}[\w\.\-]* import)',
                    'prefixes': ['import', 'from'],
                },
                {
                    'template': '(?:INSTALLED_APPS|THIRD_PARTY_APPS|MIDDLEWARE_CLASSES)[\S\W]*(?:"|\')${django_setup}',
                    'prefixes': ['INSTALLED_APPS', 'THIRD_PARTY_APPS', 'MIDDLEWARE_CLASSES'],
                },
            ],
        },
    ],
    'Ruby': [
        {
            'file_descriptors': ['Gemfile'],
            'descriptors_type': 'filename',
            'templates': [
                {
                    'template': 'gem (?:"|\')${artifact_name}(?:"|\')',
                    'prefixes': ['gem'],
                },
            ],
        },
        {
            'file_descriptors': ['rb'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': 'require (?:"|\')${import_or_usage}(?:"|\')',
                    'prefixes': ['require'],
                },
            ],
        }
    ],
    'Scala': [
        {
            'file_descriptors': ['scala', 'sc', 'sbt'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': '(?:import|new).+${import_or_usage}',
                    'prefixes': ['import', 'new'],
                },
            ],
        },
    ]
}

def keys_in_template(keys, template):
    """
    Returns a boolean indicating when at least one key is in the template
    """
    return next((True for key in keys if key in template['template']), False)

def get_regexps(lang_family='', file_descriptor='', **placeholders):
    keys = placeholders.keys()
    for matcher in MATCHERS.get(lang_family):
        if file_descriptor in matcher['file_descriptors']:
            for matcher_template in [template['template'] for template in matcher['templates'] if keys_in_template(keys, template)]:
                template = Template(r'' + re.sub(r'\$(\))?$', r'$$\1', matcher_template))
                placeholders_regexp = { key: value.replace('\\', '\\\\') for key, value in placeholders.items() }

                try:
                    yield r'' + template.substitute(placeholders_regexp)
                except KeyError:
                    # TODO: Raise the KeyError exception, look for templates in the same family that fit
                    # the placeholders
                    pass
                except:
                    raise

def get_prefixes(matcher):
    """
    Yields tuples with a prefix and a template with all the
    templates of a matcher
    """ 
    for template in matcher.get('templates'):
        for prefix in template.get('prefixes'):
            yield prefix, template
