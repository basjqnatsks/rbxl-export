import rbxlx_export
from time import time
t = time()
rbxlx_export.run('go.rbxlx', output='ExtractedScripts',lua=True, json=False)
print(time()-t)