# Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.

- Open brackets must be closed in the correct order.

- Every close bracket has a corresponding open bracket of the same type.

## Examples

**Example 1:**

Input: `s = "()"`

Output: `True`

**Example 2:**

Input: `s = "()[]{}"`

Output: `True`

**Example 3:**

Input: `s = "(]"`

Output: `False`

## Constraints

`1` <= `len(s)` <= `10^4`

`s` consists of parentheses only `'()[]{}'`.