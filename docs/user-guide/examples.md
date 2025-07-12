# Examples

This page provides practical examples of using Thing For Humans™.

## Basic Usage

### Getting Help

```bash
# Show main help
thing --help

# Show help for a specific command
thing [command] --help
```

### Check Version

```bash
thing --version
```

## Advanced Usage

### Using with Different Log Levels

```bash
# Run with debug logging
thing --log-level DEBUG [command]

# Run with minimal logging
thing --log-level ERROR [command]
```

### Using with Configuration

```bash
# Set configuration via environment variables
export THING_SETTING_NAME=value
thing [command]

# Or create a .env file
echo "THING_SETTING_NAME=value" > .env
thing [command]
```
## Common Workflows

### Example Workflow 1

```bash
# Step 1: Initialize
thing init

# Step 2: Process
thing process --input file.txt

# Step 3: Output
thing output --format json
```

### Example Workflow 2

```bash
# One-liner example
thing process --input file.txt --output result.txt --verbose
```

## Error Handling Examples

### Common Errors

```bash
# File not found
thing process --input nonexistent.txt
# Error: Input file 'nonexistent.txt' not found

# Invalid option
thing --invalid-option
# Error: No such option: --invalid-option
```

### Debugging

```bash
# Run with debug logging to troubleshoot
thing --log-level DEBUG process --input file.txt
```

## Integration Examples

### Use in Scripts

```bash
#!/bin/bash
set -e

# Check if thing is installed
if ! command -v thing &> /dev/null; then
    echo "thing is not installed"
    exit 1
fi

# Run the command
thing process --input "$1" --output "$2"
echo "Processing complete"
```

### Use with Make

```makefile
.PHONY: process
process:
	thing process --input input.txt --output output.txt

.PHONY: clean
clean:
	rm -f output.txt thing.log
```

## Performance Tips

- Use appropriate log levels in production
- Process files in batches when possible
- Use configuration files for repeated settings

## Next Steps

- Learn more about the [API Reference](../reference/)
- Check out the [Contributing Guide](../contributing.md)
- Visit the [GitHub repository](https://github.com/JnyJny/thing)