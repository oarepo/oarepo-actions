from invenio_access.permissions import Permission, any_user, authenticated_user
from invenio_records.api import Record
from invenio_records_rest.utils import allow_all
from oarepo_validate import MarshmallowValidatedRecordMixin, SchemaKeepingRecordMixin

from oarepo_actions.decorators import action

from .constants import SAMPLE_ALLOWED_SCHEMAS, SAMPLE_PREFERRED_SCHEMA
from .marshmallow import SampleSchemaV1


def neco():
    return {"xx": "yy"}
def pf(record = None):
    return Permission(any_user)
class SampleRecord(SchemaKeepingRecordMixin,
                   MarshmallowValidatedRecordMixin,
                   Record):
    ALLOWED_SCHEMAS = SAMPLE_ALLOWED_SCHEMAS
    PREFERRED_SCHEMA = SAMPLE_PREFERRED_SCHEMA
    MARSHMALLOW_SCHEMA = SampleSchemaV1

    @action(url_path="blah", permissions = allow_all)
    def send_email(self):
        return {"title": self["title"]}

    @classmethod
    @action(detail=False, url_path="jej", permissions = allow_all)
    def blah1(cls):
        return neco()

    @classmethod
    @action(detail=False, permissions=pf)
    def blah(cls):
        return neco()

    _schema = "sample/sample-v1.0.0.json"
    def validate(self, **kwargs):
        return super().validate(**kwargs)
