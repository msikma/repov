repov
=====

This is a simple script that retrieves basic version information from
the Git repository state using a synchronous call. This can be used to
print version numbers for staging (non-live) purposes.

This is the Python version of the
[same package for Node/Javascript](https://github.com/msikma/repo-v), by the 
same author.


Installing
----------

This package is [available on PyPI](https://pypi.python.org/pypi/repov/0.4):

    pip install repov

The source is [available on Github](https://github.com/msikma/repov).


Usage
-----

Import the module and run `repov.get_version()` to get started:

```python
import repov
version = repov.get_version()
print(version)  # e.g. master-27-7072898
```

In this example, we're on the master branch, the 27th commit, identified
by the short hash `7072898`.

You can pass a template to `get_version()` to get customized output. Use a
string as argument containing the variables you want in between % signs.
The default template is `%branch-any%-%count%-%hash%`. Any variable that
is for some reason unavailable will be replaced with `(unknown)`:

```python
repov.get_version('%branch%')       # master
repov.get_version('%branch-any%')   # (depends on situation, see below)
repov.get_version('%branch-all%')   # HEAD, origin/master, master
repov.get_version('%count%')        # 27
repov.get_version('%count-hex%')    # 1b
repov.get_version('%hash%')         # 7072898
repov.get_version('%hash-full%')    # 7072898a6a04f867c7d7b8a8aa4249a8d408bc0a
repov.get_version('%foobar%')       # (unknown)
```

The `%branch-any%` variable is the most versatile. The following is returned
depending on the situation:

* local branch: **master**
* remote tracking branch (in sync): **master**
* remote tracking branch (not in sync): **remotes/origin/feature-foo**
* tag: **v1.2.3**
* general detached head: **v1.0.6-5-g2393761**

If the `git` command itself is unusable for some reason, all variables
will become `(unknown)`.

### Advanced

To change the Git command:

```python
repov.Parser.git_cmd = '../../some/path/git'
```

To change the fallback string used for variables that couldn't be
computed:

```python
repov.Parser.unknown_segment = '(N/A)'  # default: '(unknown)'
```

You can also add your own Git commands to run using
`repoV.repov_parser.merge_git_args()`. See the included `defaults.py` file 
for an example of how to do this.


License
-------

MIT licensed.
