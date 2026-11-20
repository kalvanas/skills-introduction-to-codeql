/**
 * @name SQL execute() called with a concatenated string
 * @description Building the SQL text by string concatenation is error-prone; pass parameters instead.
 * @kind problem
 * @problem.severity warning
 * @id demo/sql-concat-execute
 */

import python

from Call c, Attribute a, BinaryExpr b
where
  c.getFunc() = a and
  a.getName() = "execute" and
  c.getArg(0) = b and
  b.getOp() instanceof Add
select c, "execute() is called with a concatenated SQL string."
