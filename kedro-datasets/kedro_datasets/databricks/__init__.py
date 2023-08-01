"""Provides interface to Unity Catalog Tables and MLFlow Experiments."""
from typing import Any

import lazy_loader as lazy

# https://github.com/pylint-dev/pylint/issues/4300#issuecomment-1043601901
ManagedTableDataSet: Any

__getattr__, __dir__, __all__ = lazy.attach(
    __name__,
    submod_attrs={
        "managed_table_dataset": ["ManagedTableDataSet"],
        "mlflow_artifact_dataset": ["MLFlowArtifact"],
        "mlflow_dataset_dataset": ["MLFlowDataSet"],
        "mlflow_metrics_dataset": ["MLFlowMetrics"],
        "mlflow_model_metadata_dataset": ["MLFLowModelMetadata"],
        "mlflow_tags_dataset": ["MLFlowTags"],
    },
)
