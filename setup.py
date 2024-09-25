from setuptools import find_package,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Adiii',
    author_email='armstersaha8@gmail.com',
    install_requires=["Openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_package()
)