import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("docs_checker", ROOT / "scripts/check_docs.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def test_documentation_links():
    errors = []
    for name in checker.DOCS:
        path = ROOT / name
        if path.exists():
            errors.extend(checker.check_file(path, repository="bmdhodl"))
    assert errors == []


@pytest.mark.parametrize("link", ["[missing](gone.md)", "[heading](other.md#gone)",
                                  "![](other.md)"])
def test_broken_documentation_is_rejected(tmp_path, link):
    (tmp_path / "other.md").write_text("# Existing\n", encoding="utf-8")
    path = tmp_path / "README.md"
    path.write_text("# Test\n" + link, encoding="utf-8")
    assert checker.check_file(path, root=tmp_path)


def test_valid_heading_and_code_example_link_are_accepted(tmp_path):
    (tmp_path / "other.md").write_text("# Existing\n", encoding="utf-8")
    path = tmp_path / "README.md"
    path.write_text("# Test\n[heading](other.md#existing)\n"
                    "```python\n# [example](not-a-real-link)\n```\n", encoding="utf-8")
    assert checker.check_file(path, root=tmp_path) == []
