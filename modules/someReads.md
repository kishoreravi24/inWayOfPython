# Modules
- Importing a modules, python check first is there any module present or not with the package, if not it checks is there any file present with that name
- How it checks for the module i.e file present or not, which is via sys.path (running directory of the script)
- What if module also present and the file name also present which one it will take, it givese priority to the modules in the directory over modules of the same name in the standard library
- Python stores the compiled versions of the modules in **__pycache__** directory, naming convention would be like module.version.pyc basically caching is for optimizing the module loading by storing compiled versions for faster works

