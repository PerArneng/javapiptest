from subprocess import call
import os
from pkg_resources import resource_filename

def main():
    # the @ variable subst is because of the spring boot filtering pattern that it sets
    # in the maven parent
    jar_path = os.path.abspath(resource_filename('target', '@project.build.finalName@.jar'))
    call("java -jar %s" % jar_path, shell=True)
