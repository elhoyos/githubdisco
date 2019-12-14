import unittest
from matchers import MATCHERS, get_regexps, keys_in_template, get_prefixes
from textwrap import dedent

class TestMatchers(unittest.TestCase):

    def _tests_cases(self, tests):
        for test in tests:
            args = { key: value for key, value in test.items() if key in ('lang_family', 'file_descriptor') }
            placeholders = test.get('placeholders')
            fixture = test.get('fixture')
            with self.subTest(**args):
                for regexp in get_regexps(**args, **placeholders):
                    args['regexp'] = regexp
                    fmt_fixture = dedent(fixture.lstrip('\n'))
                    yield fmt_fixture, regexp

                if args.get('regexp') is None:
                    raise LookupError

    def test_match(self):
        tests = [
            {
                'lang_family': 'C#,Visual Basic',
                'file_descriptor': 'json',
                'placeholders': {
                    'package_name': 'My.Package.Client'
                },
                'fixture': '''
                  {
                    "dependencies": {
                      "My.Package.Client": [{}, "version_constraint"]
                    }
                  }
                '''
            },
            {
                'lang_family': 'C#,Visual Basic',
                'file_descriptor': 'config',
                'placeholders': {
                    'package_name': 'My.Package.Client'
                },
                'fixture': '''
                  <packages>
                    <package id="My.Package.Client" version="..." targetFramework="..." />
                  </packages>
                '''
            },
            {
                'lang_family': 'C#,Visual Basic',
                'file_descriptor': 'csproj',
                'placeholders': {
                    'package_name': 'My.Package.Client'
                },
                'fixture': '''
                  <?xml version="1.0" encoding="utf-8"?>
                  <Project ToolsVersion="4.0" DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
                    <PropertyGroup>
                      <Configuration Condition=" '$(Configuration)' == '' ">Debug</Configuration>
                    </PropertyGroup>
                    <ItemGroup>
                      <Reference Include="My.Package.Client, Version=1.1.0.0, Culture=neutral, processorArchitecture=MSIL">
                        <HintPath>..\packages\My.Package.Client.1.1.0\lib\4.0\My.Package.Client.dll</HintPath>
                        <Private>True</Private>
                      </Reference>
                '''
            },
            {
                'lang_family': 'Go',
                'file_descriptor': 'go',
                'placeholders': {
                    'import_or_usage': 'gopkg.in/my/package.v1'
                },
                'fixture': '''
                  import (
                   	"os"
                  	mypackage "gopkg.in/my/package.v1"
                  )
                ''',
            },
            {
                'lang_family': 'JavaScript,TypeScript',
                'file_descriptor': 'json',
                'placeholders': {
                    'artifact_name': 'my-package'
                },
                'fixture': '''
                  {
                    "dependencies": {
                      "foo": "https://github.com/me/not-my-package.git",
                      "my-package": "^3.1.0"
                    }
                  }
                '''
            },
            {
                'lang_family': 'JavaScript,TypeScript',
                'file_descriptor': 'json',
                'placeholders': {
                    'artifact_name': 'my-package'
                },
                'fixture': '''
                  {
                    "devDependencies": {
                      "my-package": "^3.1.0",
                      "foo": "https://github.com/me/not-my-package.git",
                    }
                  }
                '''
            },
            {
                'lang_family': 'JavaScript,TypeScript',
                'file_descriptor': 'js',
                'placeholders': {
                    'artifact_name': 'my-package',
                },
                'fixture': '''
                  const foo = require('foo');
                  const { Strategy, initialize, isEnabled } = require('my-package');
                '''
            },
            {
                'lang_family': 'JavaScript,TypeScript',
                'file_descriptor': 'jsx',
                'placeholders': {
                    'artifact_name': 'my-package'
                },
                'fixture': '''
                  const foo = require("foo");
                  const { Strategy, initialize, isEnabled } = require("my-package");
                '''
            },
            {
                'lang_family': 'JavaScript,TypeScript',
                'file_descriptor': 'ts',
                'placeholders': {
                    'artifact_name': 'my-package'
                },
                'fixture': '''
                  import foo from 'foo';
                  import { Strategy, initialize, isEnabled } from 'my-package';
                '''
            },
            {
                'lang_family': 'JavaScript,TypeScript',
                'file_descriptor': 'tsx',
                'placeholders': {
                    'artifact_name': 'my-package'
                },
                'fixture': '''
                  import foo from "foo"
                  import { Strategy, initialize, isEnabled } from "my-package"
                '''
            },
            {
                'lang_family': 'Java,Kotlin',
                'file_descriptor': 'gradle',
                'placeholders': {
                    'artifact_name': 'com.me:my-library:1.0.0'
                },
                'fixture': '''
                  compile 'com.me:my-library:1.0.0'
                '''
            },
            {
                'lang_family': 'Java,Kotlin',
                'file_descriptor': 'gradle.kts',
                'placeholders': {
                    'artifact_name': 'com.me:my-library:1.0.0'
                },
                'fixture': '''
                  compile 'com.me:my-library:1.0.0'
                '''
            },
            {
                'lang_family': 'Java,Kotlin',
                'file_descriptor': 'gradle.kts',
                'placeholders': {
                    'artifact_name': 'com.me:my-library:1.0.0'
                },
                'fixture': '''
                  implementation 'com.me:my-library:1.0.0'
                '''
            },
            {
                'lang_family': 'Java,Kotlin',
                'file_descriptor': 'java',
                'placeholders': {
                    'import_or_usage': 'com.me.mylibrary'
                },
                'fixture': '''
                  import com.me.mylibrary;
                '''
            },
            {
                'lang_family': 'Java,Kotlin',
                'file_descriptor': 'xml',
                'placeholders': {
                    'group_id': 'com.me',
                    'artifact_id': 'mylibrary'
                },
                'fixture': '''
                  <dependency>
                    <groupId>com.me</groupId>
                    <artifactId>mylibrary</artifactId>
                    <version>0.2</version>
                  </dependency>
                '''
            },
            {
                'lang_family': 'Objective-C,Swift',
                'file_descriptor': 'Podfile',
                'placeholders': {
                  'artifact_name': 'MyLibrary'
                },
                'fixture': '''
                  pod `MyLibrary`, '1.0.0'
                '''
            },
            {
                'lang_family': 'Objective-C,Swift',
                'file_descriptor': 'Podfile',
                'placeholders': {
                  'artifact_name': 'MyLibrary'
                },
                'fixture': '''
                  pod 'MyLibrary', '1.0.0'
                '''
            },
            {
                'lang_family': 'Objective-C,Swift',
                'file_descriptor': 'Podfile',
                'placeholders': {
                  'artifact_name': 'MyLibrary'
                },
                'fixture': '''
                  pod "MyLibrary", '1.0.0'
                '''
            },
            {
                'lang_family': 'Objective-C,Swift',
                'file_descriptor': 'Cartfile',
                'placeholders': {
                  'artifact_name': 'me/my-library'
                },
                'fixture': '''
                  github "me/my-library" "1.0.0"
                '''
            },
            {
                'lang_family': 'Objective-C,Swift',
                'file_descriptor': 'm',
                'placeholders': {
                  'import_or_usage': 'MyLibrary.h'
                },
                'fixture': '''
                  #include "MyLibrary.h"
                '''
            },
            {
                'lang_family': 'Objective-C,Swift',
                'file_descriptor': 'h',
                'placeholders': {
                  'import_or_usage': 'MyLibrary.h'
                },
                'fixture': '''
                  #import "MyLibrary.h"
                '''
            },
            {
                'lang_family': 'Objective-C,Swift',
                'file_descriptor': 'swift',
                'placeholders': {
                  'import_or_usage': 'MyLibrary'
                },
                'fixture': '''
                  import MyLibrary
                '''
            },
            {
                'lang_family': 'PHP',
                'file_descriptor': 'json',
                'placeholders': {
                  'artifact_name': 'me/my-library'
                },
                'fixture': '''
                  {
                    "require": {
                      "me/my-library": "^1.0.0"
                    }
                  }
                '''
            },
            {
                'lang_family': 'PHP',
                'file_descriptor': 'php',
                'placeholders': {
                  'import_or_usage': 'Me\\MyLibrary'
                },
                'fixture': '''
                  use Me\\MyLibrary;
                '''
            },
            {
                'lang_family': 'PHP',
                'file_descriptor': 'php',
                'placeholders': {
                  'import_or_usage': 'Me\\MyLibrary'
                },
                'fixture': '''
                  $lib = new Me\\MyLibrary();
                '''
            },
            {
                'lang_family': 'Python',
                'file_descriptor': 'py',
                'placeholders': {
                  'artifact_name': 'my-library'
                },
                'fixture': '''
                  setup(
                      name='SupportService',
                      packages=find_packages(),
                      include_package_data=True,
                      install_requires=[
                          'redis',
                          'my-library'
                      ]
                  )
                '''
            },
            {
                'lang_family': 'Python',
                'file_descriptor': 'py',
                'placeholders': {
                    'import_or_usage': 'mylibrary'
                },
                'fixture': '''
                  import mylibrary
                '''
            },
            {
                'lang_family': 'Python',
                'file_descriptor': 'py',
                'placeholders': {
                    'import_or_usage': 'mylibrary'
                },
                'fixture': '''
                  from mylibrary.utils import a, b
                '''
            },
            {
                'lang_family': 'Python',
                'file_descriptor': 'py',
                'placeholders': {
                    'django_setup': 'mylibrary'
                },
                'fixture': '''
                  INSTALLED_APPS = (
                      'foo',
                      'mylibrary',
                      'bar',
                  )
                '''
            },
            {
                'lang_family': 'Python',
                'file_descriptor': 'py',
                'placeholders': {
                    'django_setup': 'mylibrary'
                },
                'fixture': '''
                  MIDDLEWARE_CLASSES = (
                      # ...
                      'mylibrary.middleware.MyLibraryMiddleware',
                      # ...
                  )
                '''
            },
            {
                'lang_family': 'Python',
                'file_descriptor': 'py',
                'placeholders': {
                    'django_setup': 'mylibrary'
                },
                'fixture': '''
                  THIRD_PARTY_APPS = (
                      'foo',  # foo
                      'mylibrary',  # mylib
                      'bar',  # bar
                      'baz.bar', # baz.bar
                  )
                '''
            },
            {
                'lang_family': 'Ruby',
                'file_descriptor': 'Gemfile',
                'placeholders': {
                    'artifact_name': 'MyPackage'
                },
                'fixture': '''
                  gem 'MyPackage', '~> 1.1.0'
                '''
            },
            {
                'lang_family': 'Ruby',
                'file_descriptor': 'Gemfile',
                'placeholders': {
                    'artifact_name': 'MyPackage'
                },
                'fixture': '''
                  group :foo, :optional => false do
                    gem "MyPackage"
                    gem "bar"
                  end
                '''
            },
            {
                'lang_family': 'Ruby',
                'file_descriptor': 'rb',
                'placeholders': {
                    'import_or_usage': 'MyPackage'
                },
                'fixture': '''
                  require "MyPackage"
                '''
            },
            {
                'lang_family': 'Scala',
                'file_descriptor': 'scala',
                'placeholders': {
                    'import_or_usage': 'com.me.mylibrary'
                },
                'fixture': '''
                  import com.me.mylibrary._
                '''
            },
            {
                'lang_family': 'Scala',
                'file_descriptor': 'sc',
                'placeholders': {
                    'import_or_usage': 'MyLibrary'
                },
                'fixture': '''
                  val lib = new MyLibrary()
                '''
            },
        ]
        for fixture, regexp in self._tests_cases(tests):
            self.assertRegex(fixture, regexp)

    def test_keys_in_template(self):
        template = {
            'template': '${bar}',
            'prefixes': [''],
        }
        self.assertTrue(keys_in_template(['foo', 'bar'], template))

    def test_keys_not_in_template(self):
        template = {
            'template': '${bar}',
            'prefixes': [''],
        }
        self.assertFalse(keys_in_template(['foo', 'baz'], template))

    def test_get_prefixes(self):
        matcher = {
            'file_descriptors': ['txt'],
            'descriptors_type': 'extension',
            'templates': [
                {
                    'template': '${trace_key}',
                    'prefixes': ['import', 'new'],
                },
            ],
        }
        prefixes_templates = [(prefix, template) for prefix, template in get_prefixes(matcher)]
        self.assertSequenceEqual(prefixes_templates, [
            ('import', matcher.get('templates')[0]),
            ('new', matcher.get('templates')[0])
        ])

if __name__ == '__main__':
    unittest.main()