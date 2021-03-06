import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, "README.md")) as f:
        README = f.read()
except IOError:
    README = ""

# NOTE: a typical webserver is included with framework dependencies if necessary
trigger_extras = {"PyYAML>=5.1", "lxml>=4.3.1", "mock==3.*"}
django_extras = {"Django"} | trigger_extras
falcon_extras = {"falcon", "gunicorn"} | trigger_extras
flask_extras = {"Flask"} | trigger_extras
pyramid_extras = {"pyramid", "waitress"} | trigger_extras
wsgi_extras = trigger_extras

dev_extras = {"WebTest", "gunicorn", "tox"}

all_extras = (
    trigger_extras
    | django_extras
    | falcon_extras
    | flask_extras
    | pyramid_extras
    | wsgi_extras
    | dev_extras
)

setup(
    name="vulnpy",
    version="0.1.0",
    description="Purposely-vulnerable functions for application security testing",
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="security testing",
    author="Contrast Security, Inc.",
    author_email="python@contrastsecurity.onmicrosoft.com",
    url="https://github.com/Contrast-Security-OSS/vulnpy",
    license="MIT",
    include_package_data=True,
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*",
    extras_require={
        "all": all_extras,
        "django": django_extras,
        "falcon": falcon_extras,
        "flask": flask_extras,
        "pyramid": pyramid_extras,
        "wsgi": wsgi_extras,
        "trigger": trigger_extras,
    },
)
