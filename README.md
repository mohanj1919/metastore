# metastore

## metastore API

1.Develop a REST API for representing Meta-Data with end points (GET, POST, PUT ,DELETE etc.). For example GET on /api/v1/location returns all location objects
a./api/v1/location, 
b./api/v1/location/{location_id}/department
c./api/v1/location/{location_id}/department/{department_id}/category
d./api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory
e./api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory/{subcategory_id}

2.Persist the data in your favorite DB - relational or non-relational (You are expected to install, configure, populate the DB). You may feel free to qualify object representations with additional attributes to enhance modeling (For e.g. Location object attributes = locationid, location description)

3.Write a api endpoint that takes input meta-data and returns all the SKU rows in the "Data" that matches with the input meta-data. 
For example, for input meta-data (Perimeter, Bakery, Bakery Bread, Bagels) , return the rows with SKUs 1 & 14 (The actual data given to you might contain more rows)

### Sample data

META DATA:

```Location,Department,Category,SubCategory
Perimeter,Bakery,Bakery Bread,Bagels
Perimeter,Bakery,Bakery Bread,Baking or Breading Products
Perimeter,Bakery,Bakery Bread,English Muffins or Biscuits
Perimeter,Bakery,Bakery Bread,Flatbreads
Perimeter,Bakery,In Store Bakery,Breakfast Cake or Sweet Roll
Perimeter,Bakery,In Store Bakery,Cakes
Perimeter,Bakery,In Store Bakery,Pies
Perimeter,Bakery,In Store Bakery,Seasonal
Center,Dairy,Cheese,Cheese Sauce
Center,Dairy,Cheese,Specialty Cheese
Center,Dairy,Cream or Creamer,Dairy Alternative Creamer
Center,Dairy,Cream or Creamer,Whipping Creams
Center,Dairy,Cultured,Cottage Cheese
Center,Dairy,Refrigerated Baking,Refrigerated Breads
Center,Dairy,Refrigerated Baking,Refrigerated English Muffins and Biscuits
Center,Dairy,Refrigerated Baking,Refrigerated Hand Held Sweets
Center,Dairy,Refrigerated Baking,Refrigerated Pie Crust
Center,Dairy,Refrigerated Baking,Refrigerated Sweet Breakfast Baked Goods
Perimeter,Deli and Foodservice,Self Service Deli Cold,Beverages
Perimeter,Deli and Foodservice,Service Deli,Cheese All Other
Perimeter,Deli and Foodservice,Service Deli,Cheese American
Perimeter,Floral,Bouquets and Cut Flowers,Bouquets and Cut Flowers
Perimeter,Floral,Gifts,Gifts
Perimeter,Floral,Plants,Plants
Center,Frozen,Frozen Bake,Bread or Dough Products Frozen
Center,Frozen,Frozen Bake,Breakfast Cake or Sweet Roll Frozen
Center,Frozen,Frozen Breakfast,Frozen Breakfast Entrees
Center,Frozen,Frozen Breakfast,Frozen Breakfast Sandwich
Center,Frozen,Frozen Breakfast,Frozen Egg Substitutes
Center,Frozen,Frozen Breakfast,Frozen Syrup Carriers
Center,Frozen,Frozen Desserts or Fruit and Toppings,Pies Frozen
Center,Frozen,Frozen Juice,Frozen Apple Juice
Center,Frozen,Frozen Juice,Frozen Fruit Drink Mixers
Center,Frozen,Frozen Juice,Frozen Fruit Juice All Other
Center,GM,Audio Video,Audio
Center,GM,Audio Video,Video DVD
Center,GM,Audio Video,Video VHS
Center,GM,Housewares,Bedding
Center,GM,Housewares,Candles
Center,GM,Housewares,Collectibles and Gifts
Center,GM,Housewares,Flashlights
Center,GM,Housewares,Frames
Center,GM,Insect and Rodent,Indoor Repellants or Traps
Center,GM,Insect and Rodent,Outdoor Repellants or Traps
Center,GM,Kitchen Accessories,Kitchen Accessories
Center,GM,Laundry,Bleach Liquid
Center,GM,Laundry,Bleach Powder
Center,GM,Laundry,Fabric Softener Liquid
Center,GM,Laundry,Fabric Softener Sheets
Center,Grocery,Baking Ingredients,Dry or Canned Milk
Center,Grocery,Baking Ingredients,Food Coloring
Center,Grocery,Spices,Salt Cooking or Edible or Seasoned
Center,Grocery,Spices,Salt Substitute
Center,Grocery,Spices,Seasoning Dry
Center,Grocery,Stuffing Products,Stuffing Products
Perimeter,Seafood,Frozen Shellfish,Frozen Shellfish
Perimeter,Seafood,Other Seafood,All Other Seafood
Perimeter,Seafood,Other Seafood,Prepared Seafood Entrees
Perimeter,Seafood,Other Seafood,Seafood Salads
Perimeter,Seafood,Other Seafood,Smoked Fish
Perimeter,Seafood,Other Seafood,Seafood Breading Sauces Dips
```

SKU DATA
```
SKU,NAME,LOCATION,DEPARTMENT,CATEGORY,SUBCATEGORY
1,SKUDESC1,Permiter,Bakery,Bakery Bread,Bagels
2,SKUDESC2,Permiter,Deli and Foodservice,Self Service Deli Cold,Beverages
3,SKUDESC3,Permiter,Floral,Bouquets and Cut Flowers,Bouquets and Cut Flowers
4,SKUDESC4,Permiter,Deli and Foodservice,Service Deli,All Other
5,SKUDESC5,Center,Frozen,Frozen Bake,Bread or Dough Products Frozen
6,SKUDESC6,Center,Grocery,Crackers,Rice Cakes
7,SKUDESC7,Center,GM,Audio Video,Audio
8,SKUDESC8,Center,GM,Audio Video,Video DVD
9,SKUDESC9,Permiter,GM,Housewares,Beeding
10,SKUDESC10,Permiter,Seafood,Frozen Shellfish,Frozen Shellfish
11,SKUDESC11,Permiter,Seafood,Other Seafood,All Other Seafood
12,SKUDESC12,Permiter,Seafood,Other Seafood,Prepared Seafood Entrees
13,SKUDESC13,Permiter,Seafood,Other Seafood,Salads
14,SKUDESC14,Permiter,Bakery,Bakery Bread,Bagels
15,SKUDESC15,Permiter,Deli and Foodservice,Self Service Deli Cold,Beverages
16,SKUDESC16,Permiter,Floral,Bouquets and Cut Flowers,Bouquets and Cut Flowers
17,SKUDESC17,Permiter,Deli and Foodservice,Service Deli,All Other
18, SKUDESC18, Center, Frozen, Frozen Bake, Bread or Dough Products Frozen
```


