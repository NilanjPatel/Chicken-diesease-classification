import setuptools

with open("README.md","r", encoding="utf-8") as f:
    log_description = f.read()



__version__ = "0.0.0"

REPO_NAME ="cnnClassifire"
AUTHOR_USER_NAME ="Nilanj Patel"
SRC_REPO="cnnClassifire"
AUTHOR_EMAIL="nilanjpatel@yahoo.in"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package to classify chicken disease using CNN",
    long_description=log_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {"":"src"},
    packages=setuptools.find_packages(where="src")
)