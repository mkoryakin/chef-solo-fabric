from fabric.api import run, env, sudo
from fabric.contrib.project import rsync_project

env.hosts = [
'ec2-54-72-67-27.eu-west-1.compute.amazonaws.com'
]

env.user = 'ubuntu'
env.key_filename = '/root/.ssh/aws.pem'
env.path = '/tmp/'

def hello(name="world"):
    print("Hello %s!" % name)

def pkg_version(*packages):
    run('which %s' % ' '.join(packages) )

def apt_update():
    sudo("aptitude update")

def apt_safe_upgrade():
    sudo("aptitude -y safe-upgrade")

def start():
    hello("User, now we will start system upgrade process")
    apt_update()
    apt_safe_upgrade()

def rvm_install():
    sudo("\curl -sSL https://get.rvm.io | bash -s stable")

def ruby_install():
     sudo("rvm install 2.1.1")
     sudo("rvm --default use 2.1.1")
     run("ruby -v")

def chef_install():
     sudo("gem update --no-rdoc --no-ri")
     sudo("gem install ohai chef --no-rdoc --no-ri"
