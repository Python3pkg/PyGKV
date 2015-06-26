import subprocess

class Database:
    def __init__(self):
        subprocess.Popen(('git','init'), stdout=subprocess.PIPE)
        self.data = {}

    def set(self, key, value):
        hash = self.hash_object(value)
        self.data[key] = hash

    def hash_object(self, value):
        if not isinstance(value,str):
            value = str(value)
        echo = subprocess.Popen(("echo",value), stdout = subprocess.PIPE)
        output = subprocess.check_output(("git", "hash-object", "-w", "--stdin"), stdin=echo.stdout)
        
        return output
