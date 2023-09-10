# How to deploy Flask on Google Cloud GCP Compute Engine with Gunicorn + Nginx + systemd

- source : [https://alex-volkov.medium.com/how-to-deploy-flask-on-google-cloud-gcp-compute-engine-with-gunicorn-nginx-systemd-96da1f32a11a](https://alex-volkov.medium.com/how-to-deploy-flask-on-google-cloud-gcp-compute-engine-with-gunicorn-nginx-systemd-96da1f32a11a)

## 0. Install python virtual environment

```
sudo apt install python3.8-venv
python -m venv app-env
# app-env is your environment name
source app-env/bin/activate
```

## 1. Install Gunicorn

```
pip3 install gunicorn
```

## 2. Navigate to app folder and add wsgi.py file

```python
from app import app

if __name__ == "__main__":
    app.run()
```

## 3. Configure NGINX routing

```
#install nginx
sudo apt-get install nginx

#navigate to the routing configuration folder
cd /etc/nginx/sites-available/

#create new site to route. I called it "music-app", you can use any name.
sudo touch music-app

#open file in vim editor
sudo vi music-app
```

## 4. Add this configuration to the file

- You can also copy and paste from nginx_config file

```
server {
  listen 80;
  server_name <external_server_ip>;
  location / {
    proxy_pass http://<internal_server_ip>:5000;
  }
}
```

## 5. Add symlink

```
cd /etc/nginx/sites-enabled
sudo ln -s /etc/nginx/sites-available/music-app

#restart nginx
sudo systemctl restart nginx
```

## 6. Add systemd service

```
cd /etc/sytemd/system

sudo vi music-app.service

# and copy and paste music-app.service in the folder
```

## 7. Enable system service

```
sudo systemctl enable music-app
sudo systemctl start music-app
```
