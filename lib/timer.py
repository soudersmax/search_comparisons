import time


def timed_function(function_name, target, search_list):

    tic = time.perf_counter()
    function_name(target, search_list)
    toc = time.perf_counter()

    timer = toc - tic
    form_time = float(f'{timer:0.4f}')

    print(f'{function_name} completed in {form_time} seconds.')
    return form_time

