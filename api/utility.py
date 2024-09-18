import datetime
from functools import wraps


def time_it(func):
    """Decorator that logs how long a function takes to complete."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        try:
            return func(*args, **kwargs)
        finally:
            time_length = datetime.datetime.now() - start
            call_args = ', '.join([str(a) for a in args]) if args else ''
            call_args += ', '.join([f"{key}={kwargs[key]}" for key in kwargs]) if kwargs else ''
            if len(call_args) > 25:
                call_args = f"{call_args[0:25]}..."
            print(f"[Call to {func.__name__}({call_args}) completed in {time_length}.]")

    return wrapper
