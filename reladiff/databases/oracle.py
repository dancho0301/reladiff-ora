from sqeleton.databases import oracle
from .base import ReladiffDialect


class Dialect(oracle.Dialect, oracle.Mixin_MD5, oracle.Mixin_NormalizeValue, ReladiffDialect):
    def normalize_uuid(self, value, coltype):
        """Convert character keys without changing their significant whitespace.

        Sqeleton's Oracle implementation trims values while sampling character
        columns for key types.  Besides changing valid VARCHAR2 keys, Oracle's
        ``TRIM`` turns an all-space value into ``NULL`` and prevents that column
        from being recognised as a key at all.  Oracle comparisons already
        provide the required semantics for CHAR values, so only a cast is
        necessary here.
        """
        return f"CAST({value} AS VARCHAR2(1024))"


class Oracle(oracle.Oracle):
    dialect = Dialect()
