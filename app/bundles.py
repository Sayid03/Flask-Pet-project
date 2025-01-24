import os 

from flask_assets import Bundle

from .functions import recursive_flaten_iterator


def get_bundle(route, tpl, ext, paths, type=False):
    if route and tpl and ext:
        return {
            'instance': Bundle(*paths, output=get_path(route, tpl, ext, type), filters=get_filter(ext)),
            'name': get_filename(route, tpl, ext, type),
            'dir': os.getcwd()
        }
    

def register_bundle(assets, bundle):
    assets.register(bundle['name'], bundle['instance'])
    return f"Bundle {bundle['name']} registered successfully!"


def register_bundles(assets, bundles):
    for x in recursive_flaten_iterator(bundles):
        for bundle in x:
            register_bundle(assets, bundle)


def get_filename(route, tpl, ext, type):
    if type:
        return f"{route}_{tpl}_{ext}_defer"
    else:
        return f"{route}_{tpl}_{ext}"

  
def get_path(route, tpl, ext, type):
    if type:
        return f"gen/{route}/{tpl}/defer.{ext}"
    else:
        return f"gen/{route}/{tpl}/main.{ext}"


def get_filter(ext):
    return f"{ext}min"


bundles = {
    'post': {
        'all': {
            'css': [get_bundle('post', 'all', 'css', ['css/blocks/table.css'])],
            'js': [get_bundle('post', 'all', 'js', ['js/blocks/js1.js', 'js/blocks/js2.js', 'js/blocks/js3.js'])]
        },
        'create': {},
        'update': {},
    },
    'user': {
        'login': {},
        'register': {},
    },
}