
[![Release][badge-release]][release]
![Version][badge-pypi-version]
![Release Date][badge-release-date]
![Python Version][badge-python-version]
![License][badge-license]
![Monthly Downloads][badge-monthly-downloads]
# thing - Thing For Humans™

> Thing for humans, presumably like you!

<!-- project description -->

## Features

<!-- project features --> 

## Installation

### pip

```console
python3 -m pip install thing
```

### uvx
```console
uvx --from thing thing
```

### uv

```console
uvx pip install thing
```

## Usage

```console
thing --help
```


## Development

This project and it's virtual environment is managed using [uv][uv] and
is configured to support automatic activation of virtual environments
using [direnv][direnv]. Development activites such as linting and testing
are automated via [Poe The Poet][poethepoet], run `poe` after cloning
this repo.

### Clone
```console
git clone https://github.com/JnyJny/thing
cd thing
```
### Allow Direnv _optional_ but recommended
```console
direnv allow
```

### Create a Virtual Environment
```console
uv venv
```
### Install Dependencies
```console
uv sync
```
### Run `poe`
```console
poe --help
```

### Release Management

This project uses automated release management with GitHub Actions:

#### Version Bumping
- `poe publish_patch` - Bump patch version, commit, tag, and push
- `poe publish_minor` - Bump minor version, commit, tag, and push  
- `poe publish_major` - Bump major version, commit, tag, and push

#### Release Notes
- `poe changelog` - Generate changelog since last tag
- `poe release-notes` - Generate release notes file

#### Automatic Releases
When you push a version tag (e.g., `v1.0.0`), GitHub Actions will:
1. Run tests across all supported Python versions
2. Build the package
3. Publish to PyPI (if tests pass)
4. Create a GitHub release with auto-generated notes
5. Upload built artifacts to the release

#### MkDocs Documentation
- `poe docs-serve` - Serve documentation locally
- `poe docs-build` - Build documentation
- `poe docs-deploy` - Deploy to GitHub Pages

The template includes MkDocs with material theme and automatic deployment to GitHub Pages.

<hr>

[![gh:JnyJny/python-package-cookiecutter][python-package-cookiecutter-badge]][python-package-cookiecutter]

<!-- End Links -->

[python-package-cookiecutter-badge]: https://img.shields.io/badge/Made_With_Cookiecutter-python--package--cookiecutter-green?style=for-the-badge
[python-package-cookiecutter]: https://github.com/JnyJny/python-package-cookiecutter
[badge-release]: https://github.com/JnyJny/thing/actions/workflows/release.yaml/badge.svg
[release]: https://github.com/JnyJny/thing/actions/workflows/release.yaml
[badge-pypi-version]: https://img.shields.io/pypi/v/thing
[badge-release-date]: https://img.shields.io/github/release-date/JnyJny/thing
[badge-python-version]: https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FJnyJny%2Fthing%2Fmain%2Fpyproject.toml
[badge-license]: https://img.shields.io/github/license/JnyJny/thing
[badge-monthly-downloads]: https://img.shields.io/pypi/dm/thing
[poe]: https://poethepoet.natn.io
[uv]: https://docs.astral.sh/uv/
[direnv]: https://direnv.net
