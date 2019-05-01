---
draft: True
revision: 1
template: base.html
title: A Python Descriptor Guide
tags: []
---

This guide compiles my understanding about [Python descriptor protocol](TODO:link) with the main resource is [Descriptor HowTo Guide](https://docs.python.org/3/howto/descriptor.html) by Raymond Hettinger. If you have a solid knowledge of the Python data model, use Raymond's guide instead for more concise explanation.

Resources:
- https://docs.python.org/3/howto/descriptor.html
- https://dev.to/dawranliou/writing-descriptors-in-python-36
- https://www.python.org/dev/peps/pep-0487/
- https://docs.python.org/3/reference/datamodel.html#object.__get__

TODO:
- define what's descriptor
x    - `__getattr__` vs `__getattribute__`
- Summarize the protocol
- Show how descriptors are called
- Examine a custom descriptor
- Examine several builtin descriptors
- when to use descriptor
- examples
- What is "binding behavior", and why a descriptor is an object with "binding behavior"?
- Learn more about object's dictionary (`obj.__dict__`)
- How descriptor is "the force" behind properties, methods, static methods, class methods, and `super()`
- How descriptor simplifies the underlying C-code

Q: `__getattr__` vs `__getattribute__`
A: `__getattribute__` is the dunder method for attribute access. 
`__getattr__` is called only when an overloaded of `__getattribute__` explicitly calls `__getattr__` or raises `AttributeError`


# Definition
Define: a descriptor is an object with "binding behavior", or whose attribute access has been *overridden* by a method of the Descriptor protocol.
My word: a descriptor is an object which defines one of the "descriptor methods"

The default behavior for attribute access is to get, set, and delete from an object's dictionary.
For example, when you call `obj.x`, it looks up in a lookup chain, starting from `obj.__dict__['x']`, then `type(obj).__dict__['x']`, and to super class of `type(obj)` through the base class of `type(obj)`

If an object implements `__get__`, that default behavior is overridden

# The protocol
Descriptor protocol:
When an object defines one of following, you have a descriptor:
`__get__(self, obj, type=None)`
`__set__(self, obj, value) --> None`
`__delete__(self, obj) --> None`

When an object defines both `__get__` and `__set__` we have a *data descriptor*

To define a read-only data descriptor, raises `AttributeError` inside `__set__`

# Invoking Descriptor
Let's have an object `d` who defines the descriptor `__get__` method, and `foo` is an arbitrary object. You can call `foo.__get__(obj)`

But a more common way is to invoke automatically on attribute access: `foo.d`
If foo is an object: prioritize data descriptors over instance variables over non-data descriptors
If foo is a class: ...
[INSERT FLOW CHART HERE]()

[INSERT invoke_descriptor.py example here]()


