# Fixed Size Hash Table
This is my Python3 implementation of a fixed size hash table for the KPCB Fellows application. The test suite can quickly be run from Command Line using `sh run_tests.sh`.
# Example Usage
Declaring a Hash Table of size 10
-----------------------------------
`sample = HashTable(10)`
Adding a Key-Value pair of ("key", 1)to the Hash Table
-----------------------------------
`sample.set("key", 1)`
Getting the value of "key" from the Table
-----------------------------------
`sample.get("key")`
Deleting the value of "key" from the Table
-----------------------------------
`sample.delete("key")`
Checking the load of an instance of HashTable
---------------------------------------------
`sample.load()`
