FROM alpine:3.14

WORKDIR /app

# Update and install postgresql-client (include psql)
RUN apk update \
    && apk upgrade \
    && apk add --no-cache postgresql-client

# Copy entry.sh
COPY entry.sh /app

# Chmod to entry.sh
RUN chmod +x ./entry.sh

# Run entry.sh
ENTRYPOINT ["/app/entry.sh"]
