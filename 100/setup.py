# l = [1]
# p = 0
# s = 0

# 0.5^5/12-0.5^4*71/60+0.5^3*347/60-0.5^2*709/60+0.5*152/15+2

# for _ in range(99):
#     s = s//2*2+2-l[p]
#     s = round(s**5/12-s**4*71/60*+347/60*s**3-709/60*s**2+152/15*s+2)
#     p += s%2
#     l.append(s//4+1)
#     s = s//2*2

# print(l)

# l p s
# [ base/dup [ array/get ] combinator/keep ] combinator/dip base/rot number/-
# l p s-i

import sys
debug = "--debug" in sys.argv

'''
# init
[[[]]][[[[]]]]
[[[[[]]]]][[]][[[[]]]][[]][[[[]]]][[[]]][[[[[]]]]][[[]]]
[[[[]]]][[]]
[[[[]]]][[]]

# begin loop
[

# 2 stuff in first line
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[[[]]]]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[]]]]]

[
# dup
[[[]]][[[]]]

# [ get ]
[
[[[[[]]]]][[[[]]]]
]
# keep
[[[[[[]]]]]][[[[]]]]

]
# rest of first line
[[[[[[]]]]]][[[]]][[[]]][[[[[[[[[[[]]]]]]]]]]][[[[]]]][[[[[[]]]]]]

# big chunk
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[[]]]]]]]]]
[[[]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[[[[[]]]]]]]]]]]]
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[[]]]]]]]]]
[[[]]][[[[[[[]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[[[[[]]]]]]]]]]]]
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]]
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[[]]]]]]]]]
[[[[]]]][[[[[[]]]]]]
[[[]]][[[[[[[]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[[[[[]]]]]]]]]]]]
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[]]]][[[[]]]][[[[]]]][[[[]]]][[[[]]]][[[[]]]][[[[[[[[]]]]]]]]
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[[]]]]]]]]]
[[[[]]]][[[[[]]]]]
[[[]]][[[[[[[]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[[[[[]]]]]]]]]]]]
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[]]]][[[[]]]][[[[[[[[]]]]]]]]
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[[]]]]]]]]]
[[[[]]]][[[[[[]]]]]]
[[[]]][[[[[[[]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[[[[[[[[[[]]]]]]]]]]]]
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]]
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[[[[[[[[]]]]]]]]]
[[[[]]]][[[[[]]]]]
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]]
[[[[]]]][[[[[]]]]]
[[[[]]]][[[[[[[[[[[[[]]]]]]]]]]]]]

# % keep
[
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[[[[]]]]]]]]]]][[[[]]]][[[[[]]]]]
]

[[[[[[]]]]]][[[[]]]]

# appender
[
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[[[]]]]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[[[]]]]][[[]]][[[[[[[[]]]]]]]][[[[[]]]]][[[]]][[[]]][[[[[[[[]]]]]]]]
]
[[[[[[]]]]]][[[[]]]]

# clear bit
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[[[]]]]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]]

]

# 99
[[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[[[[[]]]]]]]][[[[]]]][[]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[]]][[[[]]]][[[[]]]]

# times
[[[[[[]]]]]][[[[[]]]]]
'''

script = '''
base/drop
array/new number/0 number/++ array/push
number/0
number/0

number/0 number/++ number/++ number/floordiv number/0 number/++ number/++ number/* number/0 number/++ number/++ number/+

base/dup

array/get

combinator/keep

combinator/dip base/rot number/-

base/dup number/0 number/++ number/++ number/++ number/++ number/++ number/pow
number/0 number/++ number/++ number/++ number/++ number/0 number/++ number/++ number/++ number/* number/div
base/over number/0 number/++ number/++ number/++ number/++ number/pow
number/0 number/++ number/++ number/++ number/++ number/++ number/++ number/++ number/0 number/++ number/++ number/0 number/++ number/++ number/++ number/++ number/++ number/* number/* number/++ number/*
number/0 number/++ number/++ number/++ number/++ number/++ number/++ number/0 number/++ number/++ number/0 number/++ number/++ number/++ number/++ number/++ number/* number/* number/div
number/-
base/over number/0 number/++ number/++ number/++ number/pow
number/0 number/++ number/++ number/++ number/++ number/++ number/++ number/++ number/0 number/++ number/++ number/0 number/++ number/++ number/++ number/++ number/++ number/* number/* number/0 number/++ number/++ number/++ number/++ number/++ number/* number/-- number/-- number/-- number/*
number/0 number/++ number/++ number/++ number/++ number/++ number/++ number/0 number/++ number/++ number/0 number/++ number/++ number/++ number/++ number/++ number/* number/* number/div
number/+
base/over number/0 number/++ number/++ number/pow
number/0 number/++ number/++ number/++ number/++ number/++ number/++ number/++ number/0 number/++ number/++ number/0 number/++ number/++ number/++ number/++ number/++ number/* number/* number/++ number/0 number/++ number/++ number/0 number/++ number/++ number/++ number/++ number/++ number/* number/* number/-- number/*
number/0 number/++ number/++ number/++ number/++ number/++ number/++ number/0 number/++ number/++ number/0 number/++ number/++ number/++ number/++ number/++ number/* number/* number/div
number/-
base/swap
number/0 number/++ number/++ number/++ number/++ number/++ number/0 number/++ number/++ number/++ number/* number/0 number/++ number/++ number/0 number/++ number/++ number/++ number/++ number/++ number/* number/* number/++ number/++ number/*
number/0 number/++ number/++ number/++ number/++ number/++ number/0 number/++ number/++ number/++ number/* number/div
number/+
number/0 number/++ number/++
number/+
number/round

number/0 number/++ number/++ number/% number/+

combinator/keep

number/0 number/++ number/++ number/++ number/++ number/floordiv number/0 number/++ number/+ base/swapd array/push base/swap

combinator/keep

number/0 number/++ number/++ number/floordiv number/0 number/++ number/++ number/*

number/0 number/++ number/++ number/++ number/++ number/0 number/++ number/++ number/++ number/++ number/++ number/* number/0 number/++ number/++ number/++ number/++ number/++ number/* number/0 number/++ number/++ number/++ number/++ number/++ number/* number/--

combinator/times
'''
# [ number/0 number/++ number/++ number/% number/+ ] combinator/keep
# [ number/0 number/++ number/++ number/++ number/++ number/floordiv number/0 number/++ number/+ base/swapd array/push base/swapd ] combinator/keep
# all [] 99 times

# for _ in range(99):
#     s = s//2*2+2-l[p]
#     s = round(s**5/12-s**4*71/60*+347/60*s**3-709/60*s**2+152/15*s+2)
#     p += s%2
#     l.append(s//4+1)
#     s = s//2*2

import inspect
import dis
import dataclasses
from typing import TypeIs
from collections.abc import Sequence

type Syntax = Empty | Quote | Concat
type Program = Quotation | Call
type Value = Program | int | float | list[Value] | bool

# concrete syntax tree
@dataclasses.dataclass
class Empty:
    def __str__(self) -> str:
        return "[]"

@dataclasses.dataclass
class Quote:
    inner: Syntax
    def __str__(self) -> str:
        return f"[{self.inner}]"

@dataclasses.dataclass
class Concat:
    left: Syntax
    right: Syntax
    def __str__(self) -> str:
        return f"{self.left}[{self.right}]"

# abstract syntax tree
@dataclasses.dataclass
class Quotation:
    words: list[Program]
    def __str__(self) -> str:
        inner = " ".join([str(word) for word in self.words]) 
        if inner:
            return f"[ {inner} ]"
        return "[ ]"
    
@dataclasses.dataclass
class Call:
    namespace: int
    word: int
    def __str__(self) -> str:
        return word_names.get((self.namespace, self.word), f"<unknown word {self.namespace}/{self.word}>")

import sys
sys.setrecursionlimit(2 ** 31 - 1)

def symbolify(syntax: Syntax) -> int:
    match syntax:
        case Empty():
            return 0
        case Quote(inner):
            return 1 + symbolify(inner)
        case _:
            raise TypeError("bad call: namespace/word index must be a simply nested quotation")

def transform(syntax: Syntax) -> list[Program]:
    # print(syntax, repr(syntax))
    match syntax:
        case Empty():
            return [Quotation([])]
        case Quote(inner):
            return [Quotation(transform(inner))]
        case Concat(left, right):
            match left:
                case Concat(left, middle):
                    namespace = symbolify(middle)
                    if namespace == 0:
                        return [*transform(left), *transform(right)]
                    else:
                        word = symbolify(right)
                        return [*transform(left), Call(namespace, word)]
                case _:
                    # print(syntax, repr(syntax))
                    raise SyntaxError("bad call: both namespace and word indices are required syntax")

word_names = {
    (1, 0): "base/swap",
    (1, 1): "base/dup",
    (1, 2): "base/drop",
    (1, 3): "base/call",
    (1, 4): "base/quote",
    (1, 5): "base/over",
    (1, 6): "base/swapd",
    (1, 7): "base/dupd",
    (1, 8): "base/nip",
    (1, 9): "base/rot",
    (1, 10): "base/-rot",
    (2, 0): "number/0",
    (2, 1): "number/++",
    (2, 2): "number/--",
    (2, 3): "number/+",
    (2, 4): "number/-",
    (2, 5): "number/neg",
    (2, 6): "number/*",
    (2, 7): "number/div",
    (2, 8): "number/floordiv",
    (2, 9): "number/%",
    (2, 10): "number/pow",
    (2, 11): "number/round",
    (3, 0): "array/new",
    (3, 1): "array/push",
    (3, 2): "array/get",
    (3, 3): "array/iota",
    (3, 4): "array/map",
    (4, 0): "combinator/2dup",
    (4, 1): "combinator/dip",
    (4, 2): "combinator/keep",
    (4, 3): "combinator/times",
    (5, 0): "boolean/t",
    (5, 1): "boolean/f",
    (5, 2): "boolean/if",
    (6, 0): "io/.",
}

def generate_calls(names: str):
    out = ""
    for chunk in names.split("\n"):
        for name in filter(None, chunk.split()):
            rev = {name: indices for indices, name in word_names.items()}
            namespace, word = rev[name]
            out += "[" * (namespace + 2) + "]" * (namespace + 2) + "[" * (word + 2) + "]" * (word + 2)
        out += "\n"
    return out

# print(generate_calls(script))
# print(generate_calls("number/--"))
# 1/0

@dataclasses.dataclass
class Expect:
    name: str
    def quotation(self, x: Value) -> TypeIs[Quotation]:
        match x:
            case Quotation():
                return True
            case other:
                raise TypeError(f"bad call: {self.name} must be called with a quotation, not {other}")
    def integer(self, x: Value) -> TypeIs[int]:
        match x:
            case int():
                return True
            case other:
                raise TypeError(f"bad call: {self.name} must be called with an integer, not {other}")
    def number(self, x: Value) -> TypeIs[int | float]:
        match x:
            case int() | float():
                return True
            case other:
                raise TypeError(f"bad call: {self.name} must be called with a number, not {other}")
    def array(self, x: Value) -> TypeIs[list[Value]]:
        match x:
            case list():
                return True
            case other:
                raise TypeError(f"bad call: {self.name} must be called with an array, not {other}")
    def boolean(self, x: Value) -> TypeIs[bool]:
        match x:
            case bool():
                return True
            case other:
                raise TypeError(f"bad call: {self.name} must be called with a boolean, not {other}")

def execute(stack: list[Value], program: Sequence[Value]):
    for chunk in program:
        match chunk:
            case Call(namespace, word):
                name = word_names.get((namespace, word))
                # print(*stack, sep=" ", end=" ; ")
                # print(name)
                expect = Expect(name or f"<unknown word {namespace}/{word}>")
                try:
                    match name:
                        case "base/swap":
                            right, left = stack.pop(), stack.pop()
                            stack.append(right)
                            stack.append(left)
                        case "base/dup":
                            x = stack.pop()
                            stack.append(x)
                            stack.append(x)
                        case "base/drop":
                            stack.pop()
                        case "base/call":
                            quot = stack.pop()
                            if expect.quotation(quot):
                                execute(stack, quot.words)
                        case "base/over":
                            x = stack.pop()
                            y = stack.pop()
                            stack.append(y)
                            stack.append(x)
                            stack.append(y)
                        case "base/swapd":
                            x = stack.pop()
                            y = stack.pop()
                            z = stack.pop()
                            stack.append(y)
                            stack.append(z)
                            stack.append(x)
                        case "base/dupd":
                            x = stack.pop()
                            y = stack.pop()
                            stack.append(y)
                            stack.append(y)
                            stack.append(x)
                        case "base/nip":
                            x = stack.pop()
                            y = stack.pop()
                            stack.append(x)
                        case "base/rot":
                            x = stack.pop()
                            y = stack.pop()
                            z = stack.pop()
                            stack.append(y)
                            stack.append(x)
                            stack.append(z)
                        case "base/-rot":
                            x = stack.pop()
                            y = stack.pop()
                            z = stack.pop()
                            stack.append(x)
                            stack.append(z)
                            stack.append(y)
                        case "number/0":
                            stack.append(0)
                        case "number/++":
                            x = stack.pop()
                            if expect.number(x):
                                stack.append(x + 1)
                        case "number/--":
                            x = stack.pop()
                            if expect.number(x):
                                stack.append(x - 1)
                        case "number/+":
                            x = stack.pop()
                            if expect.number(x):
                                y = stack.pop()
                                if expect.number(y):
                                    stack.append(y + x)
                        case "number/-":
                            x = stack.pop()
                            if expect.number(x):
                                y = stack.pop()
                                if expect.number(y):
                                    stack.append(y - x)
                        case "number/neg":
                            x = stack.pop()
                            if expect.number(x):
                                stack.append(-x)
                        case "number/*":
                            x = stack.pop()
                            if expect.number(x):
                                y = stack.pop()
                                if expect.number(y):
                                    stack.append(y * x)
                        case "number/div":
                            x = stack.pop()
                            if expect.number(x):
                                y = stack.pop()
                                if expect.number(y):
                                    stack.append(y / x)
                        case "number/floordiv":
                            x = stack.pop()
                            if expect.number(x):
                                y = stack.pop()
                                if expect.number(y):
                                    stack.append(y // x)
                        case "number/%":
                            x = stack.pop()
                            if expect.number(x):
                                y = stack.pop()
                                if expect.number(y):
                                    stack.append(y % x)
                        case "number/pow":
                            x = stack.pop()
                            if expect.number(x):
                                y = stack.pop()
                                if expect.number(y):
                                    stack.append(y ** x)
                        case "number/round":
                            x = stack.pop()
                            if expect.number(x):
                                stack.append(round(x))
                        case "array/new":
                            stack.append([])
                        case "array/push":
                            x = stack.pop()
                            arr = stack.pop()
                            if expect.array(arr):
                                stack.append([*arr, x])
                        case "array/get":
                            i = stack.pop()
                            if expect.integer(i):
                                arr = stack.pop()
                                if expect.array(arr):
                                    x = arr[i]
                                    stack.append(arr)
                                    stack.append(x)
                        case "array/iota":
                            i = stack.pop()
                            if expect.integer(i):
                                stack.append(list(range(i)))
                        case "array/map":
                            quot = stack.pop()
                            if expect.quotation(quot):
                                arr = stack.pop()
                                if expect.array(arr):
                                    mapped: list[Value] = []
                                    for x in arr:
                                        s = [x]
                                        execute(s, quot.words)
                                        mapped.append(s.pop())
                                    stack.append(mapped)
                        case "combinator/2dup":
                            x = stack.pop()
                            y = stack.pop()
                            stack.append(x)
                            stack.append(y)
                            stack.append(x)
                            stack.append(y)
                        case "combinator/dip":
                            quot = stack.pop()
                            if expect.quotation(quot):
                                x = stack.pop()
                                execute(stack, quot.words)
                                stack.append(x)
                        case "combinator/keep":
                            quot = stack.pop()
                            if expect.quotation(quot):
                                x = stack.pop()
                                stack.append(x)
                                execute(stack, quot.words)
                                stack.append(x)
                        case "combinator/times":
                            x = stack.pop()
                            if expect.integer(x):
                                quot = stack.pop()
                                if expect.quotation(quot):
                                    for _ in range(x):
                                        execute(stack, quot.words)
                        case "boolean/t":
                            stack.append(True)
                        case "boolean/f":
                            stack.append(False)
                        case "boolean/if":
                            false = stack.pop()
                            if expect.quotation(false):
                                true = stack.pop()
                                if expect.quotation(true):
                                    bool = stack.pop()
                                    if expect.boolean(bool):
                                        if bool:
                                            execute(stack, true.words)
                                        else:
                                            execute(stack, false.words)
                        case "io/.":
                            x = stack.pop()
                            print(x)
                        case _:
                            raise ValueError(f"bad call: namespace/word index {namespace}/{word} out of range")
                except IndexError as e:
                    raise IndexError(f"bad call: not enough values on the stack for {name}") from e
            case value:
                stack.append(value)

# obligatory suspicious first line
# you've learned to skip past these by now, right? ^-^
@type.__call__
class poy:
    def __enter__(self):
        f = inspect.currentframe().f_back # type: ignore
        insts = list(dis.get_instructions(f.f_code)) # type: ignore
        start = 0
        for i, inst in enumerate(insts):
            if inst.baseopname == "BUILD_LIST":
                start = i
                break
        insts = insts[start:-20]
        syntax: list[Syntax] = []
        for inst in insts:
            match (inst.baseopname, inst.arg):
                case ("BUILD_LIST", 0):
                    syntax.append(Empty())
                case ("BUILD_LIST", 1):
                    syntax.append(Quote(syntax.pop()))
                case ("BINARY_SUBSCR", None):
                    right, left = syntax.pop(), syntax.pop()
                    syntax.append(Concat(left, right))
        
        program = transform(syntax[0])
        if debug:
            print("PROGRAM:", *program, sep=" ")
        stack = []
        execute(stack, program)
        if debug:
            print("STACK:", *stack, sep=" ")

    def __exit__(*_):
        return True
