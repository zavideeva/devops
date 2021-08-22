## Best practices that are used for Dockerfile:
1. Linter by https://github.com/hadolint/hadolint
2. Not using cache when installing dependencies
```
RUN pip install --no-cache-dir -r requirements.txt
```
3. At first install all dependencies from requirements file and then copy source code. After rebuild (for example, when files changed) all dependecies were in cache in image. 
