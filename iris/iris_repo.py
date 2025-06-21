from datetime import timedelta
from feast import BigQuerySource, Entity, Feature, FeatureView, Field, ValueType
from feast.types import Float32, Int64

driver = Entity(name="flower_id", join_keys=["flower_id"], value_type=ValueType.INT64,)

iris_stats_source = BigQuerySource(
    table="project2025blue.feast_iris.project2025bluetable",
    timestamp_field="event_timestamp",
    created_timestamp_column="created",
)

driver_stats_fv = FeatureView(
    name="iris_hourly_classification",
    entities=[driver],
    ttl=timedelta(weeks=52),
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width", dtype=Float32),
    ],
    source=iris_stats_source,
    tags={"team": "iris_classification"},
)
