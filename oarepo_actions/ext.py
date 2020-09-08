import invenio_base
from flask import url_for, abort, Blueprint
from invenio_app.helpers import obj_or_import_string
from invenio_base.signals import app_loaded
import inspect
from .record_action import RecordAction
from .record_action_list import RecordActionList


def function(sender, app=None, **kwargs):
    actions = Blueprint("oarepo_actions", __name__, url_prefix=None, )
    rest_endpoints = app.config["RECORDS_REST_ENDPOINTS"]
    print(list(sorted(rest_endpoints.keys())))
    for endpoint, configuration in rest_endpoints.items():
        if 'record_class' not in configuration:
            continue
        record_class = configuration['record_class']
        record_class = obj_or_import_string(record_class)
        for f in inspect.getmembers(record_class):
            name, function = f
            if hasattr(function, '__action'):
                #print("mam atribut")
                attribut_content = getattr(function, '__action')
                print(attribut_content)
                if 'detail' in attribut_content:
                    if 'url_path' in attribut_content:
                        route_rule = configuration['list_route'] + attribut_content['url_path']
                    else:
                        route_rule = configuration['list_route'] + name
                    actions.add_url_rule(route_rule,
                                         view_func=RecordActionList.as_view(
                                             RecordActionList.view_name.format(endpoint, name),
                                             method=function))
                else:
                    if 'url_path' in attribut_content:

                        if attribut_content['url_path'][1] != '/':
                            route_rule = configuration['item_route'] + '/' + attribut_content['url_path']
                        else:
                            route_rule = configuration['item_route'] + attribut_content['url_path']
                    else:
                        route_rule = configuration['item_route'] + '/' + name
                    actions.add_url_rule(route_rule,
                                         view_func=RecordAction.as_view(RecordAction.view_name.format(endpoint, name),
                                                                        method=name))
    app.register_blueprint(actions)
    print(app.url_map)


class Actions(object):
    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""

        app.extensions['testinvenio-oarepo_actions'] = self
        app_loaded.connect(function)
