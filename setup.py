from setuptools import setup, Extension

module1 = Extension('testmodule', sources=['testmodule.c'], py_limited_api=True)
setup (name='TestModule', version='1.0', ext_modules = [module1])
