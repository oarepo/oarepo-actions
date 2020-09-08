import json

from flask import current_app
from invenio_records_rest.views import pass_record
from invenio_rest import ContentNegotiatedMethodView


def make_json_response(data):
    response = current_app.response_class(
        json.dumps(data),
        mimetype='application/json')
    response.status_code = 200

    return response

class RecordAction(ContentNegotiatedMethodView):
    view_name = '{0}_{1}'

    def __init__(self, method):
        super().__init__(
            method_serializers={
                'GET': {'application/json' : make_json_response}
            },
            default_method_media_type={
            })
        self.method = method


    @pass_record
    #@need_record_permission('update_permission_factory')
    def get(self, pid, record, **kwargs):
        print(getattr(record, self.method))
        return getattr(record, self.method)()
        # return self.make_response(
        #     pid, record, links_factory=self.links_factory)
