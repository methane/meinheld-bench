from __future__ import print_function
import subprocess
import time

wrk_command = "wrk -c 20 -d 10 http://localhost:8080/".split()
gunicorn_command = "gunicorn --keep-alive 10 -k meinheld.gmeinheld.MeinheldWorker -b 0.0.0.0:8080 app:application".split()
chaussette_command = "chaussette --host 0.0.0.0 --port 8080 --backend meinheld app.application".split()
circus_command = "circusd circus.ini".split()

print("Gunicorn (1 process)")
gunicorn = subprocess.Popen(gunicorn_command)
time.sleep(1)
subprocess.check_call(wrk_command)
gunicorn.terminate()

print()
print("chaussette (1 process)")
chaussette = subprocess.Popen(chaussette_command)
time.sleep(1)
subprocess.check_call(wrk_command)
chaussette.terminate()

print()
print("Gunicorn (2 processes)")
gunicorn = subprocess.Popen(gunicorn_command + ["-w", "2"])
time.sleep(1)
subprocess.check_call(wrk_command)
gunicorn.terminate()

print()
print("circus+chaussette (2 processes)")
circus = subprocess.Popen(circus_command)
time.sleep(1)
subprocess.check_call(wrk_command)
circus.terminate()
