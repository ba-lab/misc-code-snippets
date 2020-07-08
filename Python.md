# Python

### A sample code
```python
#!/usr/bin/python
import sys
import os

if len(sys.argv) != 2:
        sys.stderr.write('Usage: ' + sys.argv[0] + ' <log-file-directory>\n')
        sys.exit(1)

file_path = sys.argv[1]

project_root  = "/home/" + "badri"

f = open(file_fragfold, 'r')
lines = f.readlines()
f.close()

for i in range(0,len(lines)):
	lines[i] = lines[i].strip()
	os.system(script + " " + file_in + " " + file_out)
	if (wt == 0):
		print(wt)
```

---
### Some hammers and screwdrivers <img src="tools.png" alt="drawing" width="40"/>

```python
print(x.shape)

print(len(x))

print(x.ndim)

print(x.dtypes)

print(type(x))

np.set_printoptions(precision = 2) # does not work for too wide array
np.set_printoptions(formatter = {'float': '{: 0.1f}'.format})
```

---
### How to change plotsize in matplotlib?
```python
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = ((16,16))
plt.matshow(y, cmap='gray')
plt.show()
```

---
### How to confirm the dimensions of tensors?
```python
def abc(x, y):
   assert len(x.shape) == 2
   assert x.shape == y.shape
```

