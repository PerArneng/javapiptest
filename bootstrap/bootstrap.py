from subprocess import call
from pkg_resources import resource_filename
import os
import sys
import os.path

def main():
    main_class = 'com.scalebit.javapiptest.Application'
    jar_name = '${project.build.finalName}.jar'
    jar_path = os.path.abspath(resource_filename('target', jar_name))
    jar_dir = os.path.dirname(jar_path)

    class_path = [jar_path]

    java_args = [
        'java', '-cp', ":".join(class_path), main_class
    ]

    for arg in sys.argv[1:]:
        if ' ' in arg:
            arg = "'%s'" % arg
        java_args.append(arg)

    cmdline_string = " ".join(java_args)

    return call(cmdline_string, shell=True, cwd=jar_dir)

if __name__ == '__main__':
    main()
