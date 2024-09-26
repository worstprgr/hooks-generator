# Hooks Generator for Git
Still WIP

## Usage
```text
usage: main.py [-h] [--target-branch TARGET_BRANCH] hook repository_path

positional arguments:
  hook
  repository_path

options:
  -h, --help            show this help message and exit
  --target-branch TARGET_BRANCH, --tb TARGET_BRANCH

Type `main.py help hooks` to display all supported hooks.
```

### Note
It only works on repos that where created with the `--bare` argument.

### Examples
Creates branch protection.  
| Hook        | Repo Path | Branch to Protect |
|-------------|-----------|-------------------|
| pre-receive | \<path>    | main             |

`python main.py pre-receive /path/to/bare/git/repo --tb main`
