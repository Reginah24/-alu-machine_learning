import subprocess,sys
p=subprocess.Popen([sys.executable, r"C:\Users\hp\OneDrive\Documents\alu-machine_learning\math\linear_algebra\9-let_the_butcher_slice_it.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out,err=p.communicate()
print('STDOUT_REPR:')
print(repr(out))
print('STDERR_REPR:')
print(repr(err))
