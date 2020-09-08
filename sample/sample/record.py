from invenio_records.api import Record
from oarepo_validate import MarshmallowValidatedRecordMixin, SchemaKeepingRecordMixin

from oarepo_actions.decorators import action

from .constants import SAMPLE_ALLOWED_SCHEMAS, SAMPLE_PREFERRED_SCHEMA
from .marshmallow import SampleSchemaV1


class SampleRecord(SchemaKeepingRecordMixin,
                   MarshmallowValidatedRecordMixin,
                   Record):
    ALLOWED_SCHEMAS = SAMPLE_ALLOWED_SCHEMAS
    PREFERRED_SCHEMA = SAMPLE_PREFERRED_SCHEMA
    MARSHMALLOW_SCHEMA = SampleSchemaV1

    @action(url_path="blah")
    def send_email(self):
        return {"title": self["title"]}

    @classmethod
    @action(detail=False, url_path="jej")
    def blah1(cls):
        return {"xx": "yy"}

    _schema = "sample/sample-v1.0.0.json"
    def validate(self, **kwargs):
        return super().validate(**kwargs)
