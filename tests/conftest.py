import ast
import json
from pathlib import Path

import pytest

SRC_ROOT = Path(__file__).parents[1].joinpath("src", "teritorio")
DATA_ROOT = SRC_ROOT.joinpath("_data")


@pytest.fixture
def main_classes() -> dict[str, ast.ClassDef]:
    pyi_ast = ast.parse(SRC_ROOT.joinpath("main.pyi").read_text())
    return {node.name: node for node in pyi_ast.body if isinstance(node, ast.ClassDef)}


@pytest.fixture
def data_countries() -> set[str]:
    with DATA_ROOT.joinpath("country.json").open() as file:
        data = json.load(file)
    return set(data)


@pytest.fixture
def data_currencies() -> set[str]:
    with DATA_ROOT.joinpath("currency.json").open() as file:
        data = json.load(file)
    return set(data)
