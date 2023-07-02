import logging


def configure_logging(app):
    del app.logger.handlers[:]

    loggers = [app.logger, ]
    handlers = []

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(verbose_formatter(app))
    if (app.config['APP_ENV'] == app.config['APP_ENV_TESTING']) or (
            app.config['APP_ENV'] == app.config['APP_ENV_DEVELOP']):
        console_handler.setLevel(logging.DEBUG)
    elif (app.config['APP_ENV'] == app.config['APP_ENV_LOCAL']) or (
            app.config['APP_ENV'] == app.config['APP_ENV_PRODUCTION']):
        console_handler.setLevel(logging.INFO)
    handlers.append(console_handler)

    if (app.config['APP_ENV'] == app.config['APP_ENV_TESTING']) or (
            app.config['APP_ENV'] == app.config['APP_ENV_DEVELOP']):
        file_handler = logging.FileHandler(app.config['LOG_FILE_API'], encoding="utf-8")
        file_handler.setFormatter(verbose_formatter(app))
        file_handler.setLevel(logging.DEBUG)
        handlers.append(file_handler)
    elif (app.config['APP_ENV'] == app.config['APP_ENV_LOCAL']) or (
            app.config['APP_ENV'] == app.config['APP_ENV_PRODUCTION']):
        file_handler = logging.FileHandler(app.config['LOG_FILE_API'], encoding="utf-8")
        file_handler.setFormatter(verbose_formatter(app))
        file_handler.setLevel(logging.INFO)
        handlers.append(file_handler)

    for logger in loggers:
        for handler in handlers:
            logger.addHandler(handler)
        logger.propagate = False
        logger.setLevel(logging.DEBUG)


def verbose_formatter(app):
    return logging.Formatter(app.config['FTM'], datefmt=app.config['DATE_FMT'])