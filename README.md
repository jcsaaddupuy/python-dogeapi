python-dogeapi
==============
Provide a class to access [DogeApi][https://www.dogeapi.com] API.

```sh
pip install python-dogeapi
```

All methods from [the expoesed API][https://www.dogeapi.com/api_documentation] are availables with their argument.

HTTP arguments must be passed as named python arguments.

Examples :

```python
from dogeapi.wow import Doge

print Doge("SUCH ADRESS").get_balance()
addresses = Doge("SUCH ADRESS").get_my_addresses()

for address in addresses :
    print address, Doge("SUCH ADRESS").get_address_received(payment_address = address)

 print Doge("SUCH ADRESS").get_address_by_label(address_label = "main")

print Doge().get_current_block()
print Doge().get_difficulty()

print Doge("SUCH ADRESS").get_new_address(address_label = "WOW SuCH TEST PYTHON API")
print Doge("SUCH ADRESS").withdraw(amount = 5, payment_address = "DFSzxeWRXVALxVUdNF1Dk2WjqbF8b7mWjV")

```

DOGE tip me : DFSzxeWRXVALxVUdNF1Dk2WjqbF8b7mWjV
