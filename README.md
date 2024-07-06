Sure! Here's a README for your logging system:

---

# Logging System with Verbosity Levels and Exit Trap

This project provides a customizable logging system in Python that supports different verbosity levels and captures local variables on unhandled exceptions. The system writes log files to a dated folder and can be integrated easily into any Python program.

## Features

- **Dated Log Folders**: Logs are saved in a folder named with the current date.
- **Multiple Verbosity Levels**: Supports `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL` levels.
- **Console and File Logging**: Logs are printed to both the console and a file.
- **Exception Handling**: Captures unhandled exceptions and logs local variables to help trace errors precisely.
- **Exit Trap**: Logs a message when the program exits, capturing any unhandled exceptions.

## Installation

No external libraries are required. The logger uses Python's built-in `logging`, `os`, `sys`, `atexit`, and `traceback` modules.

## Usage

### 1. Initialize Logger

Create an instance of the `Logger` class at the beginning of your program. Set the desired log level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

```python
from logger import MyLogger

# Create a logger instance
logger = MyLogger(log_name='my_application', log_level=logging.INFO).get_logger()
```

### 2. Replace Print Statements

Replace your existing `print` statements with appropriate logger methods (`debug`, `info`, `warning`, `error`, `critical`).

```python
# Example function with debug, info, and error logs
def example_function():
    var1 = "value1"
    var2 = 42

    logger.debug("Debugging variable var1: %s", var1)
    logger.info("Starting the example function.")
    
    try:
        # Simulate an error
        result = var2 / 0
    except ZeroDivisionError as e:
        logger.error("An error occurred: %s", e)

    logger.info("Example function completed.")

# Run the example function
example_function()
```

### 3. Set Log Level

Control the verbosity of your logging output by setting the log level in the `Logger` initialization.

```python
# For detailed debugging output
logger = MyLogger(log_name='my_application', log_level=logging.DEBUG).get_logger()

# For general information and above
logger = MyLogger(log_name='my_application', log_level=logging.INFO).get_logger()
```

### 4. Example Program

Here’s an example program demonstrating the setup and usage:

```python
# Import the Logger class
from logger import Logger

# Create a logger instance
logger = MyLogger(log_name='my_application', log_level=logging.INFO).get_logger()

# Example function with debug, info, and error logs
def example_function():
    var1 = "value1"
    var2 = 42

    logger.debug("Debugging variable var1: %s", var1)
    logger.info("Starting the example function.")
    
    try:
        # Simulate an error
        result = var2 / 0
    except ZeroDivisionError as e:
        logger.error("An error occurred: %s", e)

    logger.info("Example function completed.")

# Run the example function
example_function()
```

## Handling Unhandled Exceptions and Local Variables

The logger captures unhandled exceptions and logs the local variables present at the time of the exception, providing detailed information for debugging.

### Example:

```python
# Example function to test unhandled exceptions and local variables logging
def test_function():
    local_var1 = "test value"
    local_var2 = 42
    raise ValueError("This is a test exception with local variables")

test_function()
```
## Timing of Functions or Steps
### timing.py

```python
import time
from functools import wraps
from contextlib import contextmanager
from MYLogger import Logger

logger = Logger()

def time_function(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()
		elapsed_time = end_time - start_time
		logger.log(f"[{func.__name__}] Elapsed time: {elapsed_time:.4f} seconds")
		return result
	return wrapper

@contextmanager
def time_step(name):
	start_time = time.time()
	try:
		yield
	finally:
		end_time = time.time()
		elapsed_time = end_time - start_time
		logger.log(f"[{name}] Elapsed time: {elapsed_time:.4f} seconds")
```

### Usage

#### Timing Entire Functions

Use the `time_function` decorator to measure and log the execution time of entire functions:
	
```python
from timing import time_function

@time_function
def some_function():
	# Your code here
	time.sleep(2)
	
some_function()
```

#### Timing Individual Steps Within Functions

Use the `time_step` context manager to measure and log the execution time of specific steps within a function:
	
```python
from timing import time_step

def complex_function():
	with time_step("Step 1: Initialization"):
		# Step 1 code
		time.sleep(1)  # Simulating a time-consuming step
		
	with time_step("Step 2: Processing"):
		# Step 2 code
		time.sleep(2)  # Simulating another time-consuming step
		
	with time_step("Step 3: Finalization"):
		# Step 3 code
		time.sleep(1.5)  # Simulating the final step
		
complex_function()
```

#### Combining Both

You can combine both the `time_function` decorator and the `time_step` context manager to get detailed timing logs for both the overall function and individual steps:
	
```python
from timing import time_function, time_step

@time_function
def complex_function():
	with time_step("Step 1: Initialization"):
		# Step 1 code
		time.sleep(1)  # Simulating a time-consuming step
		
	with time_step("Step 2: Processing"):
		# Step 2 code
		time.sleep(2)  # Simulating another time-consuming step
		
	with time_step("Step 3: Finalization"):
		# Step 3 code
		time.sleep(1.5)  # Simulating the final step
		
complex_function()
```



## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License.

---

This README should help you get started with the logging system and integrate it into your Python projects effectively.
