# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from llama_index.ingestion.client.generated_client.core.datetime_utils import (
    serialize_datetime,
)

from .configured_transformation_item import ConfiguredTransformationItem
from .data_sink_create import DataSinkCreate
from .data_source_create import DataSourceCreate


class PipelineCreate(pydantic.BaseModel):
    """
    Schema for creating a pipeline.
    """

    configured_transformations: typing.Optional[
        typing.List[ConfiguredTransformationItem]
    ] = pydantic.Field(description="List of configured transformations.")
    data_source_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        description="List of data source IDs. When provided instead of data_sources, the data sources will be looked up by ID."
    )
    data_sources: typing.Optional[typing.List[DataSourceCreate]] = pydantic.Field(
        description="List of data sources. When provided instead of data_source_ids, the data sources will be created."
    )
    data_sink_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        description="List of data sink IDs. When provided instead of data_sinks, the data sinks will be looked up by ID."
    )
    data_sinks: typing.Optional[typing.List[DataSinkCreate]] = pydantic.Field(
        description="List of data sinks. When provided instead of data_sink_ids, the data sinks will be created."
    )
    name: str

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
