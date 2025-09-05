
# LangExtract

LangExtract is a tool for extracting and analyzing programming languages used in a codebase by leveraging LLMs.

https://github.com/google/langextract

You need an LLM to use it.

It uses few shot prompting to identify entities to extract from code snippets.

It supports multiple languages and

### Ollama Installation Instructions

```shell
brew services start ollama
```

```shell
ollama run gpt-oss:20b "say hello in one short line"
ollama run gemma2:2b "say hello in one short line"
```

web-ui does not work with Python 3.13. use Python 3.12 or lower.

```shell
source .venv/bin/activate
open-webui serve --port 3000 # it takes a while to load the model
```

open http://localhost:3000
create a new account (PW: abc)

select gpt-oss:20b model from local models

lastly, run the python programs that extracts the languages.

```shell
uv run sample1.py
```

to see the results in a browser:
open sample1.html