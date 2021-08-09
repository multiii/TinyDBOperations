=============
TinyDBOperations
=============

A python wrapper used to perform additional TinyDB operations

Installation:
=============

Run either of these pip commands in the terminal:

.. code:: bash

    pip install TinyDBOperations
    
.. code:: bash

    python -m pip install TinyDBOperations
    
Usage:
=============

💡 This library requires `tinydb <https://github.com/msiemens/tinydb>`_.

Importing tinydb and inserting a row into a table
------------

.. code:: py
  
  from tinydb import TinyDB, Query
  
  db = TinyDB("database.json")
  
  tab = db.table("table_one")
  
  tab.insert({"id": 0, "1": {"1": 1, "2": 2}, "2": {"1": 1, "2": 4}})
  
Now, to update the values within the dicts
------------

.. code:: py

  from tinydb import TinyDB, Query  
  from tinydb_op import add
  
  db = TinyDB("database.json")
  
  tab = db.table("table_one")
  
  User = Query()
    
  tab.update(add("1", "1", n=1), User.id == 0)
  
Usage of other operators
------------

.. code:: py
  
  from tinydb import TinyDB, Query
  from tinydb_op import exponent, increment
  
  db = TinyDB("database.json")
  
  tab2 = db.table("table_two")
  
  User = Query()
    
  tab2.insert({"id": 0, "list": [1, 2, 3, 4, 5], "dict": {"1": 1, "2": 2, "3": 3}})
  
  for n in range(5):
    tab2.update(exponent("list", n=n), User.id == 0)
    
   _dict = tab2.get(User.id == 0)["dict"]
   
   for key in _dict.keys():
    tab2.update(increment("dict", key), User.id == 0)
