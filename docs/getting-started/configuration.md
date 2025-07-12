# Configuration

Thing For Humans™ uses Pydantic Settings for configuration management, which allows you to configure the application using environment variables, configuration files, or both.

## Environment Variables

You can configure thing using environment variables:

```bash
export THING_SETTING_NAME=value
thing [command]
```

## Configuration File

You can also use a configuration file. Create a `.env` file in your project directory:

```bash
# .env
THING_SETTING_NAME=value
```

## Available Settings

The following settings are available:

### Logging Settings

- `THING_LOG_LEVEL`: Set the logging level (default: INFO)
- `THING_LOG_FILE`: Path to log file (default: thing.log)
### Application Settings

Add your application-specific settings here.

## Priority Order

Settings are loaded in the following priority order (highest to lowest):

1. Environment variables
2. Configuration file (`.env`)
3. Default values

## Example

```bash
# Set log level to DEBUG
export THING_LOG_LEVEL=DEBUG

# Run the CLI
thing [command]
```

