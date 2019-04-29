---
draft: True
revision: 2
template: base.html
title: Some pytest Features
tags: ['python', 'testing', 'pytest']
---

Some useful pytest features I've learnt.

# setUp and tearDown()
In [unittest](https://docs.python.org/3/library/unittest.html), `setUp()` configures preconditions for a test, and `tearDown()` cleans up them after the test is run. How to accomplish similar behaviors when using pytest?

The answer is Fixtures

Fixture is a function, decorated with `@pytest.fixture`, whose function name can be passed as an argument to a test function. When the test function body invoke that argument, the return value of the fixture will be used.

Let's make an example. Let's say you're writing integration tests that requires a database connection to a Postgresql database. How to write reusable "setup" to supply a database connection to every test function? First, write a function decorated with `@pytest.fixture`. The return value will be the connection object that test functions can use:
```python
@pytest.fixture
def db_conn():
    conn = psycopg2.connect("dbname=test user=postgres")
    return conn
```

Now you have a fixture that returns a database connection, but how to use it in test functions?. To use a fixture in a test, you need to add the fixture name as an argument to the test. In our example, test functions need to have `db_conn` as an argument. 
```python  
def test_foo(db_conn):
    result = db_conn.execute(a_sql_statement)
    assert result == expected_value
```
When the tests are executed, a db connection for each test will be created beforehand.

But how about cleaning up?

In the same test fixture, use yield instead of return to return the set up. We can add clean up code after a `yield`:

```python
@pytest.fixture
def db_conn():
    print("Begin setup")
    psycopg2.connect("dbname=test user=postgres")
    print("End setup")

    yield conn

    # begin cleaning up
    print("Begin cleaup")
    conn.close()
    print("End cleanup")
    
def test_foo(db_conn):
    result = db_conn.execute(a_sql_statement)
    assert result == expected_value
```
