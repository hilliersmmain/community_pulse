# Deployment Guide

This guide provides instructions for deploying Community Pulse to various platforms.

---

## Table of Contents

1. [Local Development](#local-development)
2. [Docker Deployment](#docker-deployment)
3. [Streamlit Cloud](#streamlit-cloud)
4. [Heroku Deployment](#heroku-deployment)
5. [AWS EC2 Deployment](#aws-ec2-deployment)

---

## Local Development

### Quick Start

```bash
# Clone repository
git clone https://github.com/hilliersmmain/community_pulse.git
cd community_pulse

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

### Development Mode

For development with auto-reload:

```bash
streamlit run app.py --server.runOnSave=true
```

---

## Docker Deployment

### Build and Run

```bash
# Build Docker image
docker build -t community-pulse:latest .

# Run container
docker run -d \
  --name community-pulse \
  -p 8501:8501 \
  -v $(pwd)/data:/app/data \
  community-pulse:latest
```

### Using Docker Compose

For development with hot-reload:

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Production Docker Deployment

```bash
# Build for production
docker-compose -f docker-compose.yml build

# Run in production mode
docker-compose -f docker-compose.yml up -d

# Monitor health
docker-compose ps
```

---

## Streamlit Cloud

### Prerequisites

- GitHub account
- Community Pulse repository forked or cloned to your account

### Deployment Steps

1. **Visit Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io/)
   - Sign in with your GitHub account

2. **Create New App**
   - Click "New app" button
   - Select your repository: `hilliersmmain/community_pulse`
   - Set main file path: `app.py`
   - Choose branch: `main` (or your preferred branch)

3. **Configure Settings** (Optional)
   - **Python version:** 3.9
   - **Additional packages:** Already in `requirements.txt`

4. **Advanced Settings** (Optional)
   ```toml
   [theme]
   primaryColor = "#FF4B4B"
   backgroundColor = "#FFFFFF"
   secondaryBackgroundColor = "#F0F2F6"
   textColor = "#262730"
   font = "sans serif"
   ```

5. **Deploy**
   - Click "Deploy" button
   - Wait 2-5 minutes for initial deployment
   - Your app will be available at: `https://<your-app-name>.streamlit.app`

### Post-Deployment

- **Custom Domain:** Configure through Streamlit Cloud settings
- **Secrets Management:** Use Streamlit Secrets for API keys
- **Monitoring:** View logs and metrics in Streamlit Cloud dashboard

### Troubleshooting

**Issue:** Deployment fails with dependency error
```bash
# Solution: Ensure requirements.txt has exact versions
pip freeze > requirements.txt
```

**Issue:** App crashes on startup
```bash
# Check logs in Streamlit Cloud console
# Verify all required files are committed to Git
```

---

## Heroku Deployment

### Prerequisites

- Heroku account
- Heroku CLI installed

### Setup Files

1. **Create `setup.sh`:**

```bash
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

2. **Create `Procfile`:**

```
web: sh setup.sh && streamlit run app.py
```

### Deployment Commands

```bash
# Login to Heroku
heroku login

# Create new app
heroku create community-pulse-app

# Add buildpack
heroku buildpacks:set heroku/python

# Deploy
git push heroku main

# Open app
heroku open

# View logs
heroku logs --tail
```

### Environment Variables

```bash
# Set environment variables
heroku config:set STREAMLIT_SERVER_HEADLESS=true
heroku config:set STREAMLIT_SERVER_PORT=$PORT
```

---

## AWS EC2 Deployment

### Launch EC2 Instance

1. **Instance Configuration:**
   - AMI: Ubuntu Server 22.04 LTS
   - Instance Type: t2.micro (free tier) or t2.small
   - Security Group: Allow inbound on ports 22 (SSH), 80 (HTTP), 8501 (Streamlit)

2. **Connect to Instance:**

```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

### Install Dependencies

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3.9
sudo apt install python3.9 python3.9-venv python3-pip -y

# Install Nginx (optional, for reverse proxy)
sudo apt install nginx -y

# Install Docker (optional)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### Deploy Application

#### Option 1: Direct Python Deployment

```bash
# Clone repository
git clone https://github.com/hilliersmmain/community_pulse.git
cd community_pulse

# Create virtual environment
python3.9 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run with nohup
nohup streamlit run app.py --server.port=8501 --server.address=0.0.0.0 &
```

#### Option 2: Docker Deployment

```bash
# Clone repository
git clone https://github.com/hilliersmmain/community_pulse.git
cd community_pulse

# Build and run with Docker Compose
sudo docker-compose up -d
```

### Setup Nginx Reverse Proxy (Optional)

Create `/etc/nginx/sites-available/community-pulse`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site:

```bash
sudo ln -s /etc/nginx/sites-available/community-pulse /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Setup Systemd Service (Production)

Create `/etc/systemd/system/community-pulse.service`:

```ini
[Unit]
Description=Community Pulse Streamlit App
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/community_pulse
Environment="PATH=/home/ubuntu/community_pulse/venv/bin"
ExecStart=/home/ubuntu/community_pulse/venv/bin/streamlit run app.py --server.port=8501 --server.address=0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable community-pulse
sudo systemctl start community-pulse
sudo systemctl status community-pulse
```

---

## Environment Variables

For all deployment methods, you can configure:

```bash
# Streamlit settings
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true

# Python settings
PYTHONUNBUFFERED=1

# Application settings
MAX_UPLOAD_SIZE_MB=50
LOG_LEVEL=INFO
```

---

## Monitoring & Maintenance

### Health Checks

```bash
# Check if app is running
curl http://localhost:8501/_stcore/health

# Docker health check
docker inspect --format='{{.State.Health.Status}}' community-pulse
```

### Logs

```bash
# Docker logs
docker logs -f community-pulse

# Systemd logs
sudo journalctl -u community-pulse -f

# Application logs
tail -f /var/log/community-pulse/app.log
```

### Backup

```bash
# Backup data directory
tar -czf data-backup-$(date +%Y%m%d).tar.gz data/

# Backup to S3 (AWS)
aws s3 cp data-backup-*.tar.gz s3://your-bucket/backups/
```

---

## Troubleshooting

### Common Issues

**Port Already in Use:**
```bash
# Find process using port 8501
lsof -i :8501
# Kill process
kill -9 <PID>
```

**Memory Issues:**
```bash
# Increase swap space (Linux)
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

**Permission Denied:**
```bash
# Fix file permissions
sudo chown -R $USER:$USER /home/ubuntu/community_pulse
chmod +x app.py
```

---

## Security Checklist

- [ ] Enable HTTPS (Let's Encrypt)
- [ ] Configure firewall (UFW or Security Groups)
- [ ] Set up regular backups
- [ ] Enable automatic security updates
- [ ] Use environment variables for secrets
- [ ] Implement rate limiting
- [ ] Enable monitoring and alerts

---

## Performance Optimization

1. **Caching:** Enable Streamlit caching for expensive operations
2. **CDN:** Use CloudFront or similar for static assets
3. **Database:** Migrate to PostgreSQL for large datasets
4. **Load Balancing:** Use AWS ELB for high traffic
5. **Auto-scaling:** Configure based on CPU/memory usage

---

## Support

For deployment issues:
- Check [GitHub Issues](https://github.com/hilliersmmain/community_pulse/issues)
- Review [Streamlit Documentation](https://docs.streamlit.io/)
- Consult cloud provider documentation

---

**Last Updated:** December 2025  
**Version:** 1.0
