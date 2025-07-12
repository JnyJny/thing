# Installation

Thing For Humans™ requires Python 3.8 or later.

## Install from PyPI

The easiest way to install thing is from PyPI:

```bash
pip install thing
```

## Install from Source

You can also install from source:

```bash
git clone https://github.com/JnyJny/thing.git
cd thing
pip install -e .
```

## Development Installation

For development, we recommend using `uv`:

```bash
git clone https://github.com/JnyJny/thing.git
cd thing
uv sync
```

This will install all dependencies including development tools.

## Verify Installation

After installation, verify that thing is working:

```bash
thing --version
```

You should see the version number displayed.

## Next Steps

Now that you have thing installed, check out the [Quick Start](quickstart.md) guide to learn how to use it.