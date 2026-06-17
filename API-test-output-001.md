# RR API Test Output - 001

**Date**: 2026-04-29T15:06:51+02:00
**Model**: Qwen/Qwen2.5-72B-Instruct
**Scenario**: tech_guides
**Prompt**: Write a concise tech guide about Python decorators, including a simple example
**Temperature**: 0.7
**Max Tokens**: 500

---

### Understanding Python Decorators

Python decorators are a powerful tool for modifying or extending the behavior of functions or methods without altering their actual code. They allow you to add functionality in a clean and reusable way.

#### How Decorators Work

A decorator is a function that takes another function as an argument and extends its behavior. The decorator itself returns a new function that can be used in place of the original one.

Here’s a step-by-step breakdown:

1. **Define the Decorator Function**: This function will take another function as an argument.
2. **Define the Wrapper Function**: Inside the decorator, define a wrapper function that adds the desired functionality.
3. **Return the Wrapper Function**: The decorator should return this wrapper function.
4. **Apply the Decorator**: Use the `@decorator_name` syntax to apply the decorator to the target function.

#### Simple Example

Let’s create a decorator that logs the arguments and the result of a function.

```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        # Log the function call details
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Log the result
        print(f"{func.__name__} returned: {result}")
        
        return result
    
    return wrapper

# Apply the decorator to a function
@log_function_call
def add(a, b):
    return a + b

# Test the decorated function
add(3, 4)
```

#### Explanation

- **Decorator Definition**: `log_function_call` is the decorator. It takes a function `func` as an argument.
- **Wrapper Function**: `wrapper` is defined inside `log_function_call`. It logs the function call details, calls the original function, logs the result, and returns the result.
- **Applying the Decorator**: The `@log_function_call` syntax is used to apply the decorator to the `add` function.
- **Function Call**: When `add(3, 4)` is called, the decorator logs the call and the result.

#### Key Points

- **Reusability**: Decorators can be reused across multiple functions.
- **Non-Intrusive**: They do not alter the original function's code.
- **Enhancement**: They can add features like logging, timing, or
