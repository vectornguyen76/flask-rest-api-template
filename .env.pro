# APP configuration
APP_NAME=Flask API Rest Template
APP_ENV=production

# Flask Configuration
API_ENTRYPOINT=app:app
APP_SETTINGS_MODULE=config.ProductionConfig

# API service configuration
API_HOST=0.0.0.0

# Database service configuration
DATABASE_URL=sqlite:///production.db

# Deployment platform
PLATFORM_DEPLOY=AWS