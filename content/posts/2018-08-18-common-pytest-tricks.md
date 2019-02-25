---
draft: True
revision: 2
template: base.html
title: setUp() and tearDown() in pytest
tags: ['python', 'testing', 'pytest']
---

In a JUnit inspired test framework like Python's unittest, `setUp()` is where you can configure preconditions for a test, and `tearDown()` is for cleaning up the test. pytest is my choice for test runner because of its smart test dicovering, simple interface and especially seamless integration with existing unittest code. pytest can be just a runner for an existing unittest code base.

But what if I don't use unittest and write tests using pytest's features only, can I still have something similar to `setUp()` and `tearDown()`?

The answer is Fixtures

A fixture is a function decorated with `@pytest.fixture`. The fixture's function name can be passed as a argument to a test function. When the test function invoke that argument, the return value of the fixture will be used.

Here's how to use pytest fixtures. Let's assume that you need to set up a database connection for a test. Simply write a db_conn function which returns a database connection, and decorate it with `@pytest.fixture`.
```python
@pytest.fixture
def db_conn():
    conn = psycopg2.connect("dbname=test user=postgres")
    return conn
```

That's how you set up a db connection for test cases. To use it, simply pass the fixture name, `db_conn`, as a parameter of your test function. Whenever the test is executed, a db connection will be created beforehand.
```python  
def test_foo(db_conn):
    result = db_conn.execute(a_sql_statement)
    assert result == expected_value
```

But how about cleaning up?

In the same test fixture, use yield instead of return to return the set up. Every line after that will be treated as clean up code.

This gist shows how to close a database connection after running a test

```python
@pytest.fixture
def db_conn():
    psycopg2.connect("dbname=test user=postgres")
    yield conn
    # start cleaning up
    conn.close()
    
def test_foo(db_conn):
    result = db_conn.execute(a_sql_statement)
    assert result == expected_value
```

## Discussion
You may ask why I want to ditch unittest TestCase if it's compatible with pytest? There are two reasons.

The first one is a little bit silly: I don't like writing Python's method name in camelCase. setUp, tearDown, and assertXXX make unittest look like a Java orphan in the Python world.

The second reason is a little bit reasonable: Writing tests in pytest is simpler. Just write a function test_this_feature and you're all done. That makes your test code less boilerplate. No more long test classes.

These advantages may not be enough for a switch. One thing you may consider is that writing pytest tests enables advanced features like fixtures, markers, plugins. However, I can't answer if these features are useful enough. I'll comeback this topic after having enough experience with pytest capabilities.
