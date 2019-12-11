# pylint: disable=anomalous-backslash-in-string

from string import Template

MATCHERS = {
    # Each key represents a language family
    # The language family is a string in which each language
    # is separated by a comma.
    # Languages must adhere to its name in GitHub.
    'C#,Visual Basic': [
        {
            'file_descriptors': ['json'],
            'descriptors_type': 'extension',
            'templates': ['dependencies":[\S\W]*"${package_name}"'],
        },
        {
            'file_descriptors': ['config'],
            'descriptors_type': 'extension',
            'templates': ['(?i:<package\s*id=)"${package_name}'],
        },
        {
            'file_descriptors': ['csproj', 'vbproj'],
            'descriptors_type': 'extension',
            'templates': ['(?i:<PackageReference\s*Include=|<Reference\s*Include=)"${package_name}'],
        },
    ],
    'Go': [
        {
            'file_descriptors': ['go'],
            'descriptors_type': 'extension',
            'templates': ['(?i)${import_or_usage}'],
        },
    ],
    'Java,Kotlin': [
        {
            'file_descriptors': ['gradle', 'gradle.kts'],
            'descriptors_type': 'extension',
            'templates': ['${artifact_name}'],
        },
        {
            'file_descriptors': ['java'],
            'descriptors_type': 'extension',
            'templates': ['import.+${import_or_usage}'],
        },
        {
            'file_descriptors': ['xml'],
            'descriptors_type': 'extension',
            'templates': ['(?i:groupid>${group_id}<\/groupid>\s+<artifactid>${artifact_id}<\/artifactid>)'],
        },
    ],
    'JavaScript,TypeScript': [
        {
            'file_descriptors': ['json'],
            'descriptors_type': 'extension',
            'templates': ['(?:devDependencies|dependencies)":[\S\W]*"${artifact_name}"'],
        },
        {
            'file_descriptors': ['js', 'jsx', 'ts', 'tsx'],
            'descriptors_type': 'extension',
            'templates': ['(?:require.+|import.+|from.+)(?:"|\')${artifact_name}(?:"|\')'],
        },
    ],
    'Objective-C,Swift': [
        {
            'file_descriptors': ['Podfile'],
            'descriptors_type': 'filename',
            'templates': ['pod (?:`|\'|")${artifact_name}(?:`|\'|")'],
        },
        {
            'file_descriptors': ['Cartfile'],
            'descriptors_type': 'filename',
            'templates': ['github "${artifact_name}"'],
        },
        {
            'file_descriptors': ['m', 'h', 'swift'],
            'descriptors_type': 'extension',
            'templates': ['#?(?:import|include) "?${import_or_usage}"?'],
        },
    ],
    'PHP': [
        {
            'file_descriptors': ['json'],
            'descriptors_type': 'extension',
            'templates': ['require":[\S\W]*"${artifact_name}"'],
        },
        {
            'file_descriptors': ['php'],
            'descriptors_type': 'extension',
            'templates': ["(?:use|new) ${import_or_usage}"],
        },
    ],
    'Python': [
        {
            'file_descriptors': ['py'],
            'descriptors_type': 'extension',
            'templates': [
                'install_requires=[\S\W]*(?:"|\')${artifact_name}(?:\[|\s+|~|=|>|<|!|"|\')',
                '(?:import ${import_or_usage}|from ${import_or_usage}[\w\.\-]* import)',
                '(?:INSTALLED_APPS|THIRD_PARTY_APPS|MIDDLEWARE_CLASSES)[\S\W]*(?:"|\')${django_setup}'
            ],
        },
        {
            'file_descriptors': ['txt'],
            'descriptors_type': 'extension',
            'templates': ['(?m:^${artifact_name}[\S\W]+)'],
        },
    ],
    'Ruby': [
        {
            'file_descriptors': ['Gemfile'],
            'descriptors_type': 'filename',
            'templates': ['gem (?:"|\')${artifact_name}(?:"|\')'],
        },
        {
            'file_descriptors': ['rb'],
            'descriptors_type': 'extension',
            'templates': ['require (?:"|\')${import_or_usage}(?:"|\')'],
        }
    ],
    'Scala': [
        {
            'file_descriptors': ['scala', 'sc', 'sbt'],
            'descriptors_type': 'extension',
            'templates': ['(?:import|new).+${import_or_usage}'],
        },
    ]
}

def keys_in_template(keys, template):
    return next((True for key in keys if key in template), False)

def get_regexps(lang_family='', file_descriptor='', **placeholders):
    keys = placeholders.keys()
    for matcher in MATCHERS.get(lang_family):
        if file_descriptor in matcher['file_descriptors']:
            for matcher_template in [template for template in matcher['templates'] if keys_in_template(keys, template)]:
                template = Template(r'' + matcher_template)
                placeholders_regexp = { key: value.replace('\\', '\\\\') for key, value in placeholders.items() }

                try:
                    yield r'' + template.substitute(placeholders_regexp)
                except KeyError:
                    # TODO: Raise the KeyError exception, look for templates in the same family that fit
                    # the placeholders
                    pass
                except:
                    raise