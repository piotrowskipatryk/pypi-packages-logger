# PyPI logger
### A simple app with newest packages index. Database is updated once a day.

PACKAGES_ON_SITE <-- environmental variable to set packages displayed on one page

Linux:
export PACKAGES_ON_SITE=7

To rebuild elasticsearch:
docker-compose run web ./manage.py search_index --rebuild
(make sure that docker-compose is already running becouse of elasticsearch)

## API
API is available at /api/
Search example: /api/packages/?search=title|text_to_find
