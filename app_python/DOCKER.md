## Best practices that are used for Dockerfile:
1. Linter by https://github.com/hadolint/hadolint
2. Not using cache when installing dependencies
```
RUN pip install --no-cache-dir -r requirements.txt
```
3. At first install all dependencies from requirements file and then copy source code. After rebuild (for example, when files changed) all dependecies were in cache in image. 
4. Create user and set ownership and permissions as required to avoid rootless container.
5. Use trusted base images (in my case python:3.9-alpine3.14)
6. Using COPY instead of ADD