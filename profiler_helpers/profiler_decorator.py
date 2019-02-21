#!/usr/bin/env python3
"""
    Purpose:
        Library for Profiling Python Functions. Will provide a decorator for
        python callables and injecting it as a parameter into a fuction
        that will profile the performance.
"""

# Python Library Imports
import cProfile
import io
import logging
import pstats
import wrapt


def profiler_decorator():
    """
    Purpose:
        Decorator for profling a python callable
    Args:
        N/A
    Returns:
        decorator (function): function decorating another function
    """

    @wrapt.decorator
    def wrapped_fuction(f, instance, args, kwargs):
        """
        Purpose:
            Wrap a function call and profile it using python's profiling
            libraries
        Args:
            f (function/method): function being profiled
            instance: pass in self when wraping class method.
                default is None when wraping function.
            args (Tuple): List of arguments
            kwargs (Dict): Dictionary of named arguments
        Return:
            output (Object): Output of the wrapped method to return
        """
        logging.info("Profiling Function")

        try:
            # Set Up Profiler
            profiler = cProfile.Profile()
            profiler.enable()

            output = f(*args, **kwargs)

            # Disabling Profilers
            profiler.disable()

            string_io = io.StringIO()
            sort_by = "cumulative"

            profiler_stats =\
                pstats.Stats(profiler, stream=string_io).sort_stats(sort_by)
            profiler_stats.print_stats()

            logging.info(f"Function Results: {string_io.getvalue()}")

        except Exception as err:
            logging.info(f"Exception Profiling Function: {err}")
            raise err

        return output

    return wrapped_fuction
