<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#dependencies">Dependencies</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
      <li><a href="#installation-from-repo">Installation from repo</a></li>
      <li><a href="#running-image-from-dockerhub">Running image from dockerhub</a></li>
      </ul>
    </li>
    <li><a href="#testing">Testing</li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
It is a simple Python web application, that shows current time in Moscow.  

## Dependencies
To start the application you need flask, gunicorn. (Other dependecies in file requirements.txt)
<!-- GETTING STARTED -->
## Getting Started
### Installation from repo
1. Clone the repo
```
git clone https://github.com/zavideeva/devops.git
```
2. Run docker-compose file from folder app_python

```
docker-compose up --build
```
3. Open link: http://0.0.0.0:8000 and see an applictaion in use
### Running image from dockerhub
``` 
docker run -p 8000:8000 zavideevaa/app_python
```

## Testing
To run test in folder app/python/test you need pytest. Run in console following:
```
pytest
```
<!-- CONTACT -->
## Contact
Alena Zavideeva - telegram @zavideevaa  
Project link - https://github.com/zavideeva/devops
