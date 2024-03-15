# APP configuration
APP_NAME=Flask API Rest Template
APP_ENV=production

# Flask Configuration
API_ENTRYPOINT=app:app
APP_SETTINGS_MODULE=config.ProductionConfig

# API service configuration
API_HOST=0.0.0.0
API_PORT=5000

# Secret key
SECRET_KEY=<your-secret-key>
JWT_SECRET_KEY=<your-jwt-secret-key>

# Database service configuration
DATABASE_URL=sqlite:///production.db

# Deployment platform
PLATFORM_DEPLOY=AWS
