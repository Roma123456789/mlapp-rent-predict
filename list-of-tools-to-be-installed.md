==============================================
List of Tools to be Installed
==============================================
1. For Editor - Visual Studio Code 
   https://code.visualstudio.com/

2. Get a GitHub 
   https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home

3. Get a Docker Hub Account 
   https://hub.docker.com/

4. For Java JDK
   https://www.oracle.com/java/technologies/downloads/#jdk17-windows

5. For Python
   https://www.python.org/

6. Jupyter Lab
   $ pip install jupyterlab
   $ pip install notebook

7. Docker Desktop for Windows
   https://www.docker.com/

8. Install Pandas
   $ pip install pandas

9. Install Sckit Learn
   $ pip install scikit-learn

10. Install Joblib
   $ pip install joblib


###################################
List of Docker Commands
###################################

$ docker images
$ docker ps -a
$ docker build -t <name-of-the-docker-image>
$ docker images
$ docker login
$ docker rmi <<image-id>>
$ docker rm $(docker ps -a)
$ docker rmi $(docker images -a -q)
$ docker push <<image-id>>
$ docker push ssadcloud/mlapp:latest
