FROM alpine:3.14

WORKDIR /app

# Update and install postgresql-client (include psql)
RUN apk update \
    && apk upgrade \
    && apk add --no-cache postgresql-client

# Copy entrypoint.sh
COPY entrypoint.sh /app

# Chmod to entrypoint.sh
RUN chmod +x ./entrypoint.sh

# Run entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]
