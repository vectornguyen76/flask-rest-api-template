# CI/CD Deploy

## Set up Github Actions

1. Create _Secrets_ on Github:

   - **AWS_ACCESS_KEY_ID**: access token
   - **AWS_SECRET_ACCESS_KEY**: secret access
   - **SSH_PRIVATE_KEY**: ssh key pair
   - **DOCKERHUB_USERNAME**: dockerhub username
   - **DOCKERHUB_PASSWORD**: dockerhub password

2. Create _Variables_ on Github:

   - **TAGS**: Tag for resources

     Example:

     ```sh
     [{ "Key": "ApplicationName", "Value": "Template_Application" },
     { "Key": "Creator", "Value": "VectorNguyen" }]
     ```

## Workflows

### Development - Build and Unittest

#### File: [development_pipeline.yml](development_pipeline.yml)

**Event:** On Pull Request → any branch into develop

**Jobs:**

- Install dependencies (caches)
- Run isort
- Run black
- Run flake8
- Build images (caches)
- Push images to Docker Hub

**Description:**
This workflow is triggered on Pull Requests into the develop branch. It ensures a clean and standardized codebase by installing dependencies, checking code formatting with isort, black, and flake8, and finally building and pushing Docker images to Docker Hub.

### Staging - CI/CD Pipeline

#### File: [staging_pipeline.yml](staging_pipeline.yml)

**Event:** On Pull Request → any branch into staging

**Jobs:**

- Install dependencies (caches)
- Run isort
- Run black
- Run flake8
- Build images (caches)
- Push images to Docker Hub
- Create infrastructure
- Configure infrastructure
- Deploy application using Docker Compose
- Clean up following the concept of A/B deploy

**Description:**
This pipeline is designed for the staging environment and is triggered on Pull Requests into the staging branch. It includes steps to ensure code quality, build and push Docker images, create and configure necessary infrastructure, and deploy the application using Docker Compose. The cleanup process follows the A/B deployment concept.

### Production - CI/CD Pipeline

#### File: [production_pipeline.yml](production_pipeline.yml)

**Event:** On Pull Request → any branch into master

**Jobs:**

- Install dependencies (caches)
- Run isort
- Run black
- Run flake8
- Build images (caches)
- Push images to Docker Hub
- Create infrastructure
- Configure infrastructure
- Deploy application using Docker Compose
- Clean up following the concept of A/B deploy

**Description:**
The production pipeline is triggered on Pull Requests into the master branch, indicating changes are ready for deployment to the production environment. It follows a similar process to the staging pipeline but is specifically tailored for the production environment. The cleanup process adheres to the A/B deployment concept, ensuring a smooth transition between versions.
