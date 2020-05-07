This is my Project.
I'm creating a web app for my old school.
It's meant for inventory management.

Using Flask with Python, Nginx as first http server and reverse proxy-server,
Gunicorn as second http server meant for serving dynamic content. 
Using SQLAlchemy w/ MySQL as Database.

Server Architecture:
![Screenhshot](Screenshot2020-05-07 at 23.24.44.png)

VM is rented on DigitalOcean and DNS nameserver also configured there.
Domain registered at Namecheap.com

virtual environment in Github included under /SoloProjectProject/venv/bin
virtual environment on ubuntu server under /var/www/flask_app/venv/bin

Link to working project:

soloproject-inventory.com
www.soloproject-inventory.com

(I must start Gunicorn service before one is able to access site.
I tried having it start after boot but I couldn't make it work.)

This is the command that needs to be executed:
'gunicorn --bind=unix:/tmp/gunicorn.sock --workers=3 soloProject:app'
