from typing import Dict

from src.dto.trained_model import TrainedModel
from src.storage.exceptions import NoTrainedModelFoundError
from src.types.api_key import ApiKey

_trained_models_cache: Dict[ApiKey, TrainedModel] = {}


def get_model(api_key: ApiKey) -> TrainedModel:
    if api_key not in _trained_models_cache:
        raise NoTrainedModelFoundError

    return _trained_models_cache[api_key]


def delete_model(api_key: ApiKey):
    if api_key in _trained_models_cache:
        del _trained_models_cache[api_key]


def save_model(api_key: ApiKey, trained_model: TrainedModel):
    _trained_models_cache[api_key] = trained_model
