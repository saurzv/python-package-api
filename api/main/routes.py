from flask import Blueprint, request, jsonify
import os

main = Blueprint('main', __name__)


def get_packages(folder_path):
    packages = {}
    requirement_file = os.path.join(folder_path, 'requirements.txt')
    if os.path.exists(requirement_file):
        with open(requirement_file, 'r') as f:
            for package in f.readlines():
                name, version = package.split('==')
                version = version[:-1]
                packages[name] = version
        return packages
    else:
        return {}


@main.route('/api')
def return_packages():
    folder_path = request.args.get('folder_path')
    print(folder_path)
    packages = {}
    for root, dirs, files in os.walk(folder_path):
        packages.update(get_packages(folder_path))

    print(packages)

    res = [{'package_name': name, 'package_version': version}
           for name, version in packages.items()]
    return jsonify(res)
