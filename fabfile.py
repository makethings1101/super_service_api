import datetime

from fabric.api import (
    local, )

from fabric.api import (with_settings, hosts, cd, run, env)
# （TODO）等待修改
from fabric.context_managers import lcd


def runtest(coverage=False):
    '''
    test
    '''
    if coverage:
        manage(
            'test --xunit-file=/code/coverage/xunit_report.xml --cover-html-dir=/code/coverage/html'
        )
    else:
        manage('test ')


def runserver(port=7070):
    '''
    start dev django server
    '''
    local(
        'docker-compose run --rm -p {port}:{port} dev python manage.py runserver 0.0.0.0:{port}'.
        format(port=port))


def docker_run(cmd):
    '''
    run shell in docker
    '''
    local('docker-compose run --rm dev {cmd}'.format(cmd=cmd))


def manage(cmd):
    '''
    run django manage command
    '''
    local('docker-compose run --rm dev python manage.py {cmd}'.format(cmd=cmd))


def makemigrations(merge=None):
    '''
    database migrate
    '''
    cmd = 'makemigrations' if merge is None else 'makemigrations --merge'
    manage(cmd)


def migrate(version=None):
    '''
    database migrate
    '''
    migrate_cmd = 'migrate main {0}'.format(version) if version else 'migrate'
    manage(migrate_cmd)


def showmigrations(args=''):
    '''
    show migrations
    '''
    manage('%s %s' % ('showmigrations', args))


def shell():
    '''
    shell
    '''
    manage('shell')


def create_app(name):
    '''
    create django app
    '''
    local('docker-compose run --rm dev django-admin.py startapp {name}'.format(
        name=name))


def create_db(db='report'):
    '''
    create db if db not exists
    '''
    local(
        'docker exec -it mysql mysql -uroot -proot -e "CREATE DATABASE IF NOT EXISTS {db};"'.
        format(db=db))


def clean():
    '''
    clean pyc
    '''
    local("find . -name '*.pyc' -type f -print -exec rm -rf {} \;")