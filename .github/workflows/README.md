# Workflows

## Development - Build and Unittest

File: [development_pipeline.yml](development_pipeline.yml)

Event: On **Pull Request** → any branch into **develop**

Jobs:

- Build
- Unit Test

### Description:

## Staging - CI/CD Pipeline

File: [staging_pipeline.yml](staging_pipeline.yml)

Event: On **Pull Request** → any branch into **staging**

Jobs:

- Build
- Unit Test
- Deploy

### Description:

## Production - CI/CD Pipeline

File: [production_pipeline.yml](production_pipeline.yml)

Event: On **Pull Request** → any branch into **main**

Jobs:

- Build
- Test
- Deploy

### Description:
