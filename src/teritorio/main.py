from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class Singleton(type):
    instance: type[Singleton] | None

    def __init__(
        cls, name: str, bases: tuple[type[Singleton], ...], dict_: dict[str, Any]
    ):
        super().__init__(name, bases, dict_)
        cls.instance = None

    def __call__(cls) -> type[Singleton]:
        if cls.instance is None:
            cls.instance = super().__call__()
        return cls.instance


class DataListIterator(Generic[T]):
    def __init__(self, data: dict[str, T]) -> None:
        self.values = (data[key] for key in sorted(data))

    def __iter__(self) -> DataListIterator[T]:
        return self

    def __next__(self) -> T:
        return next(self.values)


class DataList(Generic[T]):
    _data_path: Path
    _object_class: type[T]

    def __init__(self) -> None:
        with self._data_path.open() as file:
            data = json.load(file, object_hook=_list_to_tuple)

        self._data: dict[str, T] = {}
        for key, raw_obj in data.items():
            obj = self._object_class(**raw_obj)
            self._data[key] = obj
            setattr(self, key, obj)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, key: str) -> T:
        return self._data[key]

    def __iter__(self) -> DataListIterator[T]:
        return DataListIterator(self._data)


@dataclass(frozen=True, order=True)
class Country:
    english_name: str
    french_name: str
    alpha_2_code: str
    alpha_3_code: str
    numeric_code: int


class Countries(DataList[Country], metaclass=Singleton):
    _data_path = Path(__file__).parent.joinpath("_data/country.json")
    _object_class = Country


@dataclass(frozen=True, order=True)
class Currency:
    code: str
    name: str
    entities: tuple[str, ...]
    numeric_code: int
    minor_units: int | None


class Currencies(DataList[Currency], metaclass=Singleton):
    _data_path = Path(__file__).parent.joinpath("_data/currency.json")
    _object_class = Currency


def _list_to_tuple(obj: Any) -> Any:
    if isinstance(obj, list):
        return tuple(obj)
    if isinstance(obj, dict):
        return {key: _list_to_tuple(value) for key, value in obj.items()}
    return obj
