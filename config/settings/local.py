from .base import *  # noqa

INSTALLED_APPS += [  # noqa
    "django_browser_reload",
]

MIDDLEWARE += ["django_browser_reload.middleware.BrowserReloadMiddleware"]  # noqa
