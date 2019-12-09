# pylint: disable=anomalous-backslash-in-string

from string import Template

MATCHERS = {
    # Each key represents a language family
    # The language family is a string in which each language
    # is separated by a comma.
    # Languages must adhere to its name in GitHub.
    # TODO: separate all languages by a comma
    # TODO: verify GitHub recognizes all language names
    'C#,Visual Basic': [
        {
            'file_descriptors': ['json'],
            'descriptors_type': 'extension',
            'template': 'dependencies":[\S\W]*"${package_name}"',
        },
        {
            'file_descriptors': ['config'],
            'descriptors_type': 'extension',
            'template': '(?i:<package\s*id=)"${package_name}',
        },
        {
            'file_descriptors': ['csproj', 'vbproj'],
            'descriptors_type': 'extension',
            'template': '(?i:<PackageReference\s*Include=|<Reference\s*Include=)"${package_name}',
        },
    ],
    'Go': [
        {
            'file_descriptors': ['go'],
            'descriptors_type': 'extension',
            'template': '(?i)${import_or_usage}',
        },
    ],
    'Java,Kotlin': [
        {
            'file_descriptors': ['gradle', 'gradle.kts'],
            'descriptors_type': 'extension',
            'template': '${artifact_name}',
        },
        {
            'file_descriptors': ['java'],
            'descriptors_type': 'extension',
            'template': 'import.+${import_or_usage}',
        },
        {
            'file_descriptors': ['xml'],
            'descriptors_type': 'extension',
            'template': '(?i:groupid>${group_id}<\/groupid>\s+<artifactid>${artifact_id}<\/artifactid>)',
        },
    ],
    'JavaScript,TypeScript': [
        {
            'file_descriptors': ['json'],
            'descriptors_type': 'extension',
            'template': '(?:devDependencies|dependencies)":[\S\W]*"${artifact_name}"',
        },
        {
            'file_descriptors': ['js', 'jsx', 'ts', 'tsx'],
            'descriptors_type': 'extension',
            'template': '(?:require.+|import.+|from.+)(?:"|\')${artifact_name}(?:"|\')',
        },
    ],
    'Objective-C,Swift': [
        {
            'file_descriptors': ['Podfile'],
            'descriptors_type': 'filename',
            'template': 'pod (?:`|\'|")${artifact_name}(?:`|\'|")',
        },
        {
            'file_descriptors': ['Cartfile'],
            'descriptors_type': 'filename',
            'template': 'github "${artifact_name}"',
        },
        {
            'file_descriptors': ['m', 'h', 'swift'],
            'descriptors_type': 'extension',
            'template': '#?(?:import|include) "?${import_or_usage}"?',
        },
    ],
    'PHP': [
        {
            'file_descriptors': ['json'],
            'descriptors_type': 'extension',
            'template': 'require":[\S\W]*"${artifact_name}"',
        },
        {
            'file_descriptors': ['php'],
            'descriptors_type': 'extension',
            'template': "(?:use|new) ${import_or_usage}",
        },
    ],
    'Python': [
        {
            'file_descriptors': ['py'],
            'descriptors_type': 'extension',
            'template': 'install_requires=[\S\W]*(?:"|\')${artifact_name}(?:\[|\s+|~|=|>|<|!|"|\')',
        },
        {
            'file_descriptors': ['py'],
            'descriptors_type': 'extension',
            'template': '(?:(?:import|from).+${import_or_usage}|(?:INSTALLED_APPS|THIRD_PARTY_APPS|MIDDLEWARE_CLASSES)[\S\W]*(?:"|\')${import_or_usage})',
        },
    ],
    'Ruby': [
        {
            'file_descriptors': ['Gemfile'],
            'descriptors_type': 'filename',
            'template': 'gem (?:"|\')${artifact_name}(?:"|\')',
        },
        {
            'file_descriptors': ['rb'],
            'descriptors_type': 'extension',
            'template': 'require (?:"|\')${import_or_usage}(?:"|\')',
        }
    ],
    'Scala': [
        {
            'file_descriptors': ['scala', 'sc', 'sbt'],
            'descriptors_type': 'extension',
            'template': '(?:import|new).+${import_or_usage}',
        },
    ]
}

def get_regexps(lang_family='', file_descriptor='', **placeholders):
    for matcher in MATCHERS.get(lang_family):
        if file_descriptor in matcher['file_descriptors']:
            template = Template(r'' + matcher['template'])
            placeholders_regexp = { key: value.replace('\\', '\\\\') for key, value in placeholders.items() }

            try:
                yield r'' + template.substitute(placeholders_regexp)
            except KeyError:
                # TODO: Raise the KeyError exception, look for templates in the same family that fit
                # the placeholders
                pass
            except:
                raise