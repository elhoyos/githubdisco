from matchers import get_regexps

TRACESETS = [
    {
        'library': 'unleash-client-dotnet',
        'lang_family': 'C#,Visual Basic',
        'traces': [
            {
                'package_name': 'Unleash.FeatureToggle.Client',
            }
        ]
    },
    {
        'library': 'unleash-client',
        'lang_family': 'C#,Visual Basic',
        'traces': [
            {
                'package_name': 'unleash.client',
            }
        ]
    },
    {
        'library': 'launchdarkly',
        'lang_family': 'C#,Visual Basic',
        'traces': [
            {
                'package_name': 'LaunchDarkly.Client',
            }
        ]
    },
    {
        'library': 'NFeature',
        'lang_family': 'C#,Visual Basic',
        'traces': [
            {
                'package_name': 'NFeature',
            }
        ]
    },
    {
        'library': 'FeatureToggle',
        'lang_family': 'C#,Visual Basic',
        'traces': [
            {
                'package_name': 'FeatureToggle',
            }
        ]
    },
    {
        'library': 'FeatureSwitcher',
        'lang_family': 'C#,Visual Basic',
        'traces': [
            {
                'package_name': 'FeatureSwitcher',
            }
        ]
    },
    {
        'library': 'nToggle',
        'lang_family': 'C#,Visual Basic',
        'traces': [
            {
                'package_name': 'nToggle',
            }
        ]
    },
    {
        'library': 'Toggler',
        'lang_family': 'C#,Visual Basic',
        'traces': [
            {
                'package_name': 'Toggler',
            }
        ]
    },
    {
        'library': 'launchdarkly',
        'lang_family': 'Go',
        'traces': [
            {
                'import_or_usage': 'launchdarkly/go-client',
            }
        ]
    },
    {
        'library': 'Toggle',
        'lang_family': 'Go',
        'traces': [
            {
                'import_or_usage': 'xchapter7x/toggle',
            }
        ]
    },
    {
        'library': 'dcdr',
        'lang_family': 'Go',
        'traces': [
            {
                'import_or_usage': 'vsco/dcdr/client',
            }
        ]
    },
    {
        'library': 'unleash-client-go',
        'lang_family': 'Go',
        'traces': [
            {
                'import_or_usage': 'Unleash/unleash-client-go',
            }
        ]
    },
    {
        'library': 'launchdarkly',
        'lang_family': 'Java,Kotlin',
        'traces': [
            {
                'artifact_name': 'com.launchdarkly:launchdarkly-android-client',
            },
            {
                'import_or_usage': 'com.launchdarkly.android',
            },
            {
                'group_id': 'com.launchdarkly',
                'artifact_id': 'launchdarkly-android-client',
            }
        ]
    },
    {
        'library': 'toggle',
        'lang_family': 'Java,Kotlin',
        'traces': [
            {
                'artifact_name': 'cc.soham:toggle',
            },
            {
                'import_or_usage': 'cc.soham.toggle.Toggle',
            },
            {
                'group_id': 'cc.soham',
                'artifact_id': 'toggle',
            }
        ]
    },
    {
        'library': 'unleash-client-java',
        'lang_family': 'Java,Kotlin',
        'traces': [
            {
                'artifact_name': 'no.finn.unleash:unleash-client-java',
            },
            {
                'import_or_usage': 'no.finn.unleash',
            },
            {
                'group_id': 'no.finn.unleash',
                'artifact_id': 'unleash-client-java',
            }
        ]
    },
    {
        'library': 'launchdarkly',
        'lang_family': 'Java,Kotlin',
        'traces': [
            {
                'artifact_name': 'com.launchdarkly:launchdarkly-client',
            },
            {
                'import_or_usage': 'com.launchdarkly.client',
            },
            {
                'group_id': 'com.launchdarkly',
                'artifact_id': 'launchdarkly-client',
            }
        ]
    },
    {
        'library': 'Togglz',
        'lang_family': 'Java,Kotlin',
        'traces': [
            {
                'artifact_name': 'org.togglz:togglz-core',
            },
            {
                'import_or_usage': 'org.togglz.core',
            },
            {
                'group_id': 'org.togglz',
                'artifact_id': 'togglz-core',
            },
            {
                'group_id': 'org.togglz',
                'artifact_id': 'togglz-servlet',
            },
            {
                'group_id': 'org.togglz',
                'artifact_id': 'togglz-cdi',
            },
            {
                'group_id': 'org.togglz',
                'artifact_id': 'togglz-spring-web',
            },
            {
                'group_id': 'org.togglz',
                'artifact_id': 'togglz-spring-boot-starter',
            }
        ]
    },
    {
        'library': 'FF4J',
        'lang_family': 'Java,Kotlin',
        'traces': [
            {
                'artifact_name': 'org.ff4j:ff4j-core',
            },
            {
                'import_or_usage': 'org.ff4j.FF4j',
            },
            {
                'import_or_usage': 'org.ff4j.core',
            },
            {
                'group_id': 'org.ff4j',
                'artifact_id': 'ff4j-core',
            },
            {
                'group_id': 'org.ff4j',
                'artifact_id': 'ff4j-web',
            }
        ]
    },
    {
        'library': 'Flip',
        'lang_family': 'Java,Kotlin',
        'traces': [
            {
                'artifact_name': 'com.tacitknowledge.flip:core',
            },
            {
                'import_or_usage': 'com.tacitknowledge.flip',
            },
            {
                'group_id': 'com.tacitknowledge.flip',
                'artifact_id': 'core',
            },
            {
                'group_id': 'com.tacitknowledge.flip',
                'artifact_id': 'servlet',
            },
            {
                'group_id': 'com.tacitknowledge.flip',
                'artifact_id': 'spring',
            }
        ]
    },
    {
        'library': 'unleash-client-node',
        'lang_family': 'JavaScript,TypeScript',
        'traces': [
            {
                'artifact_name': 'unleash-client',
            }
        ]
    },
    {
        'library': 'launchdarkly',
        'lang_family': 'JavaScript,TypeScript',
        'traces': [
            {
                'artifact_name': 'ldclient-js',
            }
        ]
    },
    {
        'library': 'ember-feature-flags',
        'lang_family': 'JavaScript,TypeScript',
        'traces': [
            {
                'artifact_name': 'ember-feature-flags',
            }
        ]
    },
    {
        'library': 'feature-toggles',
        'lang_family': 'JavaScript,TypeScript',
        'traces': [
            {
                'artifact_name': 'feature-toggles',
            }
        ]
    },
    {
        'library': 'React Feature Toggles',
        'lang_family': 'JavaScript,TypeScript',
        'traces': [
            {
                'artifact_name': '@paralleldrive/react-feature-toggles',
            }
        ]
    },
    {
        'library': 'launchdarkly',
        'lang_family': 'JavaScript,TypeScript',
        'traces': [
            {
                'artifact_name': 'ldclient-node',
            }
        ]
    },
    {
        'library': 'flipit',
        'lang_family': 'JavaScript,TypeScript',
        'traces': [
            {
                'artifact_name': 'flipit',
            }
        ]
    },
    {
        'library': 'fflip',
        'lang_family': 'JavaScript,TypeScript',
        'traces': [
            {
                'artifact_name': 'fflip',
            }
        ]
    },
    {
        'library': 'Bandiera',
        'lang_family': 'JavaScript,TypeScript',
        'traces': [
            {
                'artifact_name': 'bandiera-client',
            }
        ]
    },
    {
        'library': 'flopflip',
        'lang_family': 'JavaScript,TypeScript',
        'traces': [
            {
                'artifact_name': '@flopflip/react-redux',
            },
            {
                'artifact_name': '@flopflip/react-broadcast',
            }
        ]
    },
    {
        'library': 'launchdarkly',
        'lang_family': 'Objective-C,Swift',
        'traces': [
            {
                # CocoaPods
                'artifact_name': 'LaunchDarkly',
            },
            {
                # Carthage
                'artifact_name': 'launchdarkly/ios-client',
            },
            {
                'import_or_usage': 'Darkly.h',
            },
            {
                'import_or_usage': 'LaunchDarkly',
            }
        ]
    },
    {
        'library': 'launchdarkly',
        'lang_family': 'PHP',
        'traces': [
            {
                'artifact_name': 'launchdarkly/launchdarkly-php',
            },
            {
                'import_or_usage': 'LaunchDarkly\\LDClient',
            }
        ]
    },
    {
        'library': 'Symfony FeatureFlagsBundle',
        'lang_family': 'PHP',
        'traces': [
            {
                'artifact_name': 'dzunke/feature-flags-bundle',
            },
            {
                'import_or_usage': 'DZunke\\FeatureFlagsBundle\\DZunkeFeatureFlagsBundle',
            }
        ]
    },
    {
        'library': 'Toggle',
        'lang_family': 'PHP',
        'traces': [
            {
                'import_or_usage': 'Qandidate\\Toggle',
            }
        ]
    },
    {
        'library': 'rollout',
        'lang_family': 'PHP',
        'traces': [
            {
                'artifact_name': 'opensoft/rollout',
            },
            {
                'import_or_usage': 'Opensoft\\Rollout',
            }
        ]
    },
    {
        'library': 'Bandiera',
        'lang_family': 'PHP',
        'traces': [
            {
                'artifact_name': 'npg/bandiera-client-php',
            },
            {
                'import_or_usage': 'Nature\\Bandiera\\Client',
            }
        ]
    },
    {
        'library': 'unleash-client-python',
        'lang_family': 'Python',
        'traces': [
            {
                'artifact_name': 'UnleashClient',
            },
            {
                'import_or_usage': 'UnleashClient',
            },
        ]
    },
    {
        'library': 'launchdarkly',
        'lang_family': 'Python',
        'traces': [
            {
                'artifact_name': 'ldclient-py',
            },
            {
                'import_or_usage': 'ldclient',
            },
        ]
    },
    {
        'library': 'Flask FeatureFlags',
        'lang_family': 'Python',
        'traces': [
            {
                'artifact_name': 'Flask-FeatureFlags',
            },
            {
                'import_or_usage': 'flask_featureflags',
            },
        ]
    },
    {
        'library': 'Gutter',
        'lang_family': 'Python',
        'traces': [
            {
                'artifact_name': 'gutter',
            },
            {
                'import_or_usage': 'gutter.client.default',
            }
        ]
    },
    {
        'library': 'Feature Ramp',
        'lang_family': 'Python',
        'traces': [
            {
                'artifact_name': 'feature_ramp',
            },
            {
                'import_or_usage': 'feature_ramp.Feature',
            }
        ]
    },
    {
        'library': 'flagon',
        'lang_family': 'Python',
        'traces': [
            {
                'artifact_name': 'flagon',
            },
            {
                'import_or_usage': 'flagon.backends.db_django',
            },
            {
                'import_or_usage': 'flagon.feature',
            },
            {
                'django_setup': 'flagon.backends.db_django',
            },
        ]
    },
    {
        'library': 'Waffle',
        'lang_family': 'Python',
        'traces': [
            {
                'artifact_name': 'django-waffle',
            },
            {
                'import_or_usage': 'waffle',
            },
            {
                'django_setup': 'waffle',
            },
            {
                'django_setup': 'waffle.middleware.WaffleMiddleware',
            },
        ]
    },
    {
        'library': 'Gargoyle',
        'lang_family': 'Python',
        'traces': [
            {
                'artifact_name': 'gargoyle'
            },
            {
                'artifact_name': 'gargoyle-yplan',
            },
            {
                'import_or_usage': 'gargoyle.decorators',
            },
            {
                'django_setup': 'gargoyle',
            }
        ]
    },
    {
        'library': 'unleash-client-ruby',
        'lang_family': 'Ruby',
        'traces': [
            {
                'artifact_name': 'unleash',
            },
        ]
    },
    {
        'library': 'launchdarkly',
        'lang_family': 'Ruby',
        'traces': [
            {
                'artifact_name': 'ldclient-rb',
            },
        ]
    },
    {
        'library': 'rollout',
        'lang_family': 'Ruby',
        'traces': [
            {
                'artifact_name': 'rollout',
            },
        ]
    },
    {
        'library': 'FeatureFlipper',
        'lang_family': 'Ruby',
        'traces': [
            {
                'artifact_name': 'feature_flipper',
            },
        ]
    },
    {
        'library': 'Flip',
        'lang_family': 'Ruby',
        'traces': [
            {
                'artifact_name': 'flip',
            },
        ]
    },
    {
        'library': 'Setler',
        'lang_family': 'Ruby',
        'traces': [
            {
                'artifact_name': 'setler',
            },
        ]
    },
    {
        'library': 'Bandiera',
        'lang_family': 'Ruby',
        'traces': [
            {
                'artifact_name': 'bandiera-client',
            },
            {
                'import_or_usage': 'bandiera/client'
            },
        ]
    },
    {
        'library': 'Feature',
        'lang_family': 'Ruby',
        'traces': [
            {
                'artifact_name': 'feature',
            },
        ]
    },
    {
        'library': 'Flipper',
        'lang_family': 'Ruby',
        'traces': [
            {
                'artifact_name': 'flipper',
            },
        ]
    },
    {
        'library': 'Bandiera',
        'lang_family': 'Scala',
        'traces': [
            {
                'import_or_usage': 'com.springernature.bandieraclientscala',
            },
            {
                'import_or_usage': 'BandieraClient',
            }
        ]
    }
]


def traces_in_template(traceset, matcher_template):
    """
    Yields unique traceset values of a library that are present in a
    matcher template.
    """
    seen = set()
    for dict_items in [trace.items() for trace in traceset.get('traces')]:
        for key, value in dict_items:
            if key in matcher_template and value not in seen:
                seen.add(value)
                yield value

def regexps(traceset, file_descriptors=list()):
    """
    Yields the regular expressions of all the matchers that could apply
    to the traceset and a file descriptors list
    """ 
    lang_family = traceset.get('lang_family')
    traces = traceset.get('traces')
    file_descriptor = file_descriptors[0]
    for placeholders in traces:
        for regexp in get_regexps(lang_family, file_descriptor, **placeholders):
            yield regexp