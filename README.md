# githubdisco

Discover stuff in GitHub

# Usage

Install scrapy:

```bash
$ pip install scrapy
$ scrapy crawl toggled_repos -o ./results/toggled_repos-`date +%s`.csv -s JOBDIR=crawls/toggled_repos
```

Now, create a `.tokens` file with GitHub tokens to with enough permissions to search through public repositories.

Check the `githubdisco/spiders` specific usages and have fun!

# TODO

* `USER_AGENT` setting from environment
* `FEED_EXPORT_FIELDS` setting per spider
