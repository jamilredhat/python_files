# Import a module
import shopping_module
shopping_module.available_items()
shopping_module.selected_items()
shopping_module.bill_amount(44)

from shopping_module import available_items, bill_amount
available_items()
bill_amount(6565)


# Import a package
import system_scripts.shopping
system_scripts.shopping.selected_items()

# Another way to import a package.
from system_scripts import shopping

shopping.available_items()
shopping.bill_amount(666)