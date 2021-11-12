# Protocol for gunicorn.

import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1  # Dynamically generates workers.

bind = "0.0.0.0:5000"
reload = True

# logging
accesslog = '-'
errorlog = '-'