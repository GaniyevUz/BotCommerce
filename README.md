# BotCommerce

A complete shop, with payment systems, delivery services and convenient control panel with built-in CRM and Analytics.

## TODO - Required

1. [ ] server
2. [x] github
3. [ ] github actions
4. [ ] test (pytest coverage 80% ^)
5. [ ] docker/docker compose
6. [ ] elasticsearch
7. [x] sentry
8. [ ] security
9. [x] custom admin

## Don't Required

1. [ ] cache
2. [ ] celery
3. [ ] redis
4. [ ] rabbitmq
5. [ ] cron

## NOTE - For teammates

- _Don't forget write tests your codes_
- _Test files must be_ `tests/test_*.py`

## Makefile
- ```make mig``` makemigrations & migrate 
- ```make admin``` create admin superuser
- ```make cl_data``` collect data

## Commands
- ```./manage.py collect_data``` Create Default Objects
