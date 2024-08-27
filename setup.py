from setuptools import setup

setup(
    name='my_project',
    version='0.1',
    install_requires=[
        'fastapi',
        'pydantic',
        'spacy',
        'uvicorn',
        'setuptools',
    ],
    extras_require={
        'model': [
            'pt-core-news-lg @ https://github.com/explosion/spacy-models/releases/download/pt_core_news_lg-3.5.0/pt_core_news_lg-3.5.0-py3-none-any.whl'
        ]
    },
)
