from sqeleton.abcs.database_types import String_UUID

from reladiff.databases.oracle import Dialect


def test_character_key_normalization_preserves_whitespace():
    dialect = Dialect()

    expression = dialect.normalize_uuid('"KEY"', String_UUID())

    assert expression == 'CAST("KEY" AS VARCHAR2(1024))'
    assert "TRIM" not in expression


def test_number_key_normalization_remains_supported():
    dialect = Dialect()
    number_type = dialect.parse_type(("SCHEMA", "TABLE"), "KEY", "NUMBER", numeric_precision=38, numeric_scale=0)

    expression = dialect.normalize_value_by_type('"KEY"', number_type)

    assert expression.startswith('to_char("KEY", \'FM')
    assert "TRIM" not in expression
