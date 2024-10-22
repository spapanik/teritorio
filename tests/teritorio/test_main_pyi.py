import ast


def assert_class_annotations(class_node: ast.ClassDef, expected: set[str]) -> None:
    annotations = {
        node.target.id
        for node in class_node.body
        if isinstance(node, ast.AnnAssign)
        and isinstance(node.target, ast.Name)
        and not node.target.id.startswith("_")
    }
    assert annotations == expected


def test_countries(
    main_classes: dict[str, ast.ClassDef], data_countries: set[str]
) -> None:
    assert_class_annotations(main_classes["Countries"], data_countries)


def test_currencies(
    main_classes: dict[str, ast.ClassDef], data_currencies: set[str]
) -> None:
    assert_class_annotations(main_classes["Currencies"], data_currencies)
