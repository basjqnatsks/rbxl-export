# About  rbxl-export
rbxl-export is a small and helpful tool written in Python. It allows you to easily convert a Roblox model to a file/folder structure, which is ideal to upload to Github or other code sharing services. This also allows for pulling files for a ROJO directory.
it's intended to make sharing code easier. 
Please use the PYPI Version

Prerequisites
First, install Python if you haven't already.
To install the package, run the following command to get it from PYPI:
## Installation
Install the package using pip:

 ```bash
pip install rbxlx-export
```




 ```py
import rbxlx_export
rbxlx_export.run('go.rbxlx', output='ExtractedScripts',lua=True, json=False)
```
