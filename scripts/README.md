# Scripts

This directory contains utility scripts for development.

## Available Scripts

### run_tests.py
Run the test suite with various options.

```bash
# Run all tests
python scripts/run_tests.py

# Run tests with verbose output
python scripts/run_tests.py --verbose

# Run tests without coverage
python scripts/run_tests.py --no-cov

# Run tests and generate HTML coverage report
python scripts/run_tests.py --html

# Run specific tests
python scripts/run_tests.py -k "test_read"
```
