python-dogeapi
==============
Python module for dogeapi.com

Provide a class to access [DogeApi](https://www.dogeapi.com) API.

```sh
pip install python-dogeapi
```

All methods from [the exposed API](https://www.dogeapi.com/api_documentation) are availables with their argument.

HTTP arguments must be passed as named python arguments.

Examples :

```python
from dogeapi.wow import Doge

print Doge("SUCH API KEY").get_balance()
addresses = Doge("SUCH API KEY").get_my_addresses()

for address in addresses :
    print address, Doge("SUCH API KEY").get_address_received(payment_address = address)

 print Doge("SUCH API KEY").get_address_by_label(address_label = "main")

print Doge().get_current_block()
print Doge().get_difficulty()

print Doge("SUCH API KEY").get_new_address(address_label = "WOW SuCH TEST PYTHON API")
print Doge("SUCH API KEY").withdraw(amount = 5, payment_address = "VERY SHIBE")

```

DOGE tip me : DFSzxeWRXVALxVUdNF1Dk2WjqbF8b7mWjV

