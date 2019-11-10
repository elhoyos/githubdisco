"""
The trace sets of the toggling libraries.

Structure:
 library: string: our own name of the library
 artifacts: string[]: 'package_name,package_manager', library names per package manager
 languages: string: 'language_a,language_b', languages supported by the library
 imports_usages: string[]: names used to import the library
"""

LIBRARIES = [
{
    'library': 'unleash-client-dotnet',
    'artifacts': ['Unleash.FeatureToggle.Client,NuGet'],
    'languages': 'C#,Visual Basic',
    'imports_usages': ['Unleash'],
},
{
    'library': 'unleash-client',
    'artifacts': ['unleash.client,NuGet'],
    'languages': 'C#,Visual Basic',
    'imports_usages': [],
},
{
    'library': 'launchdarkly',
    'artifacts': ['LaunchDarkly.Client,NuGet'],
    'languages': 'C#,Visual Basic',
    'imports_usages': [],
},
{
    'library': 'NFeature',
    'artifacts': ['NFeature,NuGet'],
    'languages': 'C#,Visual Basic',
    'imports_usages': [],
},
{
    'library': 'FeatureToggle',
    'artifacts': ['FeatureToggle,NuGet'],
    'languages': 'C#,Visual Basic',
    'imports_usages': [],
},
{
    'library': 'FeatureSwitcher',
    'artifacts': ['FeatureSwitcher,NuGet'],
    'languages': 'C#,Visual Basic',
    'imports_usages': [],
},
{
    'library': 'nToggle',
    'artifacts': [],
    'languages': 'C#,Visual Basic',
    'imports_usages': [],
},
{
    'library': 'Toggler',
    'artifacts': ['Toggler,NuGet'],
    'languages': 'C#,Visual Basic',
    'imports_usages': [],
},
{
    'library': 'launchdarkly',
    'artifacts': ['github.com/launchdarkly/go-client,Go'],
    'languages': 'Go',
    'imports_usages': ['launchdarkly/go-client'],
},
{
    'library': 'Toggle',
    'artifacts': ['github.com/xchapter7x/toggle,Go'],
    'languages': 'Go',
    'imports_usages': ['xchapter7x/toggle'],
},
{
    'library': 'dcdr',
    'artifacts': ['github.com/vsco/dcdr,Go'],
    'languages': 'Go',
    'imports_usages': ['vsco/dcdr/client'],
},
{
    'library': 'unleash-client-go',
    'artifacts': ['github.com/unleash/unleash-client-go,Go'],
    'languages': 'Go',
    'imports_usages': ['Unleash/unleash-client-go'],
},
{
    'library': 'unleash-client-node',
    'artifacts': ['unleash-client,NPM'],
    'languages': 'JavaScript,TypeScript',
    'imports_usages': [],
},
{
    'library': 'launchdarkly',
    'artifacts': ['ldclient-js,NPM'],
    'languages': 'JavaScript,TypeScript',
    'imports_usages': [],
},
{
    'library': 'ember-feature-flags',
    'artifacts': ['ember-feature-flags,NPM'],
    'languages': 'JavaScript,TypeScript',
    'imports_usages': [],
},
{
    'library': 'feature-toggles',
    'artifacts': ['feature-toggles,NPM'],
    'languages': 'JavaScript,TypeScript',
    'imports_usages': [],
},
{
    'library': 'React Feature Toggles',
    'artifacts': ['@paralleldrive/react-feature-toggles,NPM'],
    'languages': 'JavaScript,TypeScript',
    'imports_usages': [],
},
{
    'library': 'launchdarkly',
    'artifacts': ['ldclient-node,NPM'],
    'languages': 'JavaScript,TypeScript',
    'imports_usages': [],
},
{
    'library': 'flipit',
    'artifacts': ['flipit,NPM'],
    'languages': 'JavaScript,TypeScript',
    'imports_usages': [],
},
{
    'library': 'fflip',
    'artifacts': ['fflip,NPM'],
    'languages': 'JavaScript,TypeScript',
    'imports_usages': [],
},
{
    'library': 'Bandiera',
    'artifacts': ['bandiera-client,NPM'],
    'languages': 'JavaScript,TypeScript',
    'imports_usages': [],
},
{
    'library': 'flopflip',
    'artifacts': ['@flopflip/react-redux,NPM', '@flopflip/react-broadcast,NPM'],
    'languages': 'JavaScript,TypeScript',
    'imports_usages': [],
},
{
    'library': 'launchdarkly',
    'artifacts': ['com.launchdarkly:launchdarkly-android-client,Maven'],
    'languages': 'Kotlin,Java',
    'imports_usages': ['com.launchdarkly.android'],
},
{
    'library': 'toggle',
    'artifacts': ['cc.soham:toggle,Maven'],
    'languages': 'Kotlin,Java',
    'imports_usages': ['cc.soham.toggle.Toggle'],
},
{
    'library': 'unleash-client-java',
    'artifacts': ['no.finn.unleash:unleash-client-java,Maven'],
    'languages': 'Kotlin,Java',
    'imports_usages': ['no.finn.unleash'],
},
{
    'library': 'launchdarkly',
    'artifacts': ['com.launchdarkly:launchdarkly-client,Maven'],
    'languages': 'Kotlin,Java',
    'imports_usages': ['com.launchdarkly.client'],
},
{
    'library': 'Togglz',
    'artifacts': ['org.togglz:togglz-core,Maven'],
    'languages': 'Kotlin,Java',
    'imports_usages': ['org.togglz.core'],
},
{
    'library': 'FF4J',
    'artifacts': ['org.ff4j:ff4j-core,Maven'],
    'languages': 'Kotlin,Java',
    'imports_usages': ['org.ff4j.FF4j', 'org.ff4j.core'],
},
{
    'library': 'Flip',
    'artifacts': ['com.tacitknowledge.flip:core,Maven'],
    'languages': 'Kotlin,Java',
    'imports_usages': ['com.tacitknowledge.flip'],
},
{
    'library': 'launchdarkly',
    'artifacts': ['LaunchDarkly,CocoaPods', 'launchdarkly/ios-client,Carthage'],
    'languages': 'Objective-C,Swift',
    'imports_usages': ['Darkly.h', 'LaunchDarkly'],
},
{
    'library': 'launchdarkly',
    'artifacts': ['launchdarkly/launchdarkly-php,Packagist'],
    'languages': 'PHP',
    'imports_usages': ['LaunchDarkly\\LDClient'],
},
{
    'library': 'Symfony FeatureFlagsBundle',
    'artifacts': ['dzunke/feature-flags-bundle,Packagist'],
    'languages': 'PHP',
    'imports_usages': ['DZunke\\FeatureFlagsBundle\\DZunkeFeatureFlagsBundle'],
},
{
    'library': 'Toggle',
    'artifacts': [],
    'languages': 'PHP',
    'imports_usages': ['Qandidate\\Toggle'],
},
{
    'library': 'rollout',
    'artifacts': ['opensoft/rollout,Packagist'],
    'languages': 'PHP',
    'imports_usages': ['Opensoft\\Rollout'],
},
{
    'library': 'Bandiera',
    'artifacts': ['npg/bandiera-client-php,Packagist'],
    'languages': 'PHP',
    'imports_usages': ['Nature\\Bandiera\\Client'],
},
{
    'library': 'unleash-client-python',
    'artifacts': ['UnleashClient,Pypi'],
    'languages': 'Python',
    'imports_usages': ['UnleashClient'],
},
{
    'library': 'launchdarkly',
    'artifacts': ['ldclient-py,Pypi'],
    'languages': 'Python',
    'imports_usages': ['ldclient'],
},
{
    'library': 'Flask FeatureFlags',
    'artifacts': ['Flask-FeatureFlags,Pypi'],
    'languages': 'Python',
    'imports_usages': ['flask_featureflags'],
},
{
    'library': 'Gutter',
    'artifacts': ['gutter,Pypi'],
    'languages': 'Python',
    'imports_usages': ['gutter.client.default'],
},
{
    'library': 'Feature Ramp',
    'artifacts': ['feature_ramp,Pypi'],
    'languages': 'Python',
    'imports_usages': ['feature_ramp.Feature'],
},
{
    'library': 'flagon',
    'artifacts': ['flagon,Pypi'],
    'languages': 'Python',
    'imports_usages': ['flagon.backends.db_django', 'flagon.feature'],
},
{
    'library': 'Waffle',
    'artifacts': ['django-waffle,Pypi'],
    'languages': 'Python',
    'imports_usages': ['waffle'],
},
{
    'library': 'Gargoyle',
    'artifacts': ['gargoyle,Pypi', 'gargoyle-yplan,Pypi'],
    'languages': 'Python',
    'imports_usages': ['gargoyle.decorators', 'gargoyle'],
},
{
    'library': 'unleash-client-ruby',
    'artifacts': ['unleash,Rubygems'],
    'languages': 'Ruby',
    'imports_usages': ['unleash', 'unleash-context'],
},
{
    'library': 'launchdarkly',
    'artifacts': ['ldclient-rb,Rubygems'],
    'languages': 'Ruby',
    'imports_usages': [],
},
{
    'library': 'rollout',
    'artifacts': ['rollout,Rubygems'],
    'languages': 'Ruby',
    'imports_usages': [],
},
{
    'library': 'FeatureFlipper',
    'artifacts': ['feature_flipper,Rubygems'],
    'languages': 'Ruby',
    'imports_usages': [],
},
{
    'library': 'Flip',
    'artifacts': ['flip,Rubygems'],
    'languages': 'Ruby',
    'imports_usages': ['feature'],
},
{
    'library': 'Setler',
    'artifacts': ['setler,Rubygems'],
    'languages': 'Ruby',
    'imports_usages': [],
},
{
    'library': 'Bandiera',
    'artifacts': ['bandiera-client,Rubygems'],
    'languages': 'Ruby',
    'imports_usages': ['bandiera/client'],
},
{
    'library': 'Feature',
    'artifacts': ['feature,Rubygems'],
    'languages': 'Ruby',
    'imports_usages': [],
},
{
    'library': 'Flipper',
    'artifacts': ['flipper,Rubygems'],
    'languages': 'Ruby',
    'imports_usages': [],
},
{
    'library': 'Bandiera',
    'artifacts': ['com.springernature:bandiera-client-scala_2.12,Maven', 'com.springernature:bandiera-client-scala_2.11,Maven'],
    'languages': 'Scala',
    'imports_usages': ['com.springernature.bandieraclientscala', 'BandieraClient'],
},
]
