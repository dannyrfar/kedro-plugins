"""Provides interface to Unity Catalog Tables."""

__all__ = [
    "ManagedTableDataSet",
    "MLFlowArtifact",
    "MLFlowDataSet",
    "MLFlowMetrics",
    "MLFlowModel",
    "MLFlowModelMetadata",
    "MLFlowTags",
]

from contextlib import suppress

with suppress(ImportError):
    from .artifact import MLFlowArtifact
    from .dataset import MLFlowDataSet
    from .managed_table_dataset import ManagedTableDataSet
    from .metrics import MLFlowMetrics
    from .model import MLFlowModel
    from .model_metadata import MLFlowModelMetadata
    from .tags import MLFlowTags
