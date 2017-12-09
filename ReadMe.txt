Please follow the below instructions to run this project.

1. Install python and scrapy framework

Please refer to the below link to install python and python scapy framework 1.4

https://doc.scrapy.org/en/latest/intro/install.html

After successfully installed, you are ready to run the project

*** If you are using Ubuntu please do the following ****

- Install pip
sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install python-pip

- Install virtualenv
 pip install virtualenv


2. Run scrapy

(Actually to run this project we need one reference file containing Hindi verbs and consonants.
That is named "hindiverb.csv" in root folder and it is loaded in the project.)

Go to the HindiNews folder 

- Use virtualenv
  source hindi/bin/activate
  pip install scrapy

- Run 
	scrapy crawl hindinews