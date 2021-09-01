# Best practices that I used for Github actions
1. No harcoded secrets
2. Not install dependecies unnecessarily
3. Using caching mechanism
4. Limit environment variables to the narrowest possible scope
5. Not using self-hosted runners in a public repository
6. Automate all processes: include tesing, linter, push image to dockerhub
7. Pushing specific branch
8. Pushing image with specified lable (for me it's latest)

# Best practices for Jenkins
1. Using specific image for agent 
2. Run unit tests as part of pipeline
3. Isolate environment using docker
4. Use temporary github token 