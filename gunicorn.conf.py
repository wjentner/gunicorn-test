import multiprocessing

bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2 + 1

# doe not work with gunicorn v20.1.0 anymore
print_config = True

accesslog = '-'

loglevel = 'debug'

# 2 minute timeout for worker because of long query times
timeout = 240
