# Matches a Method to Required Tools
methodToTools = {
	"cut": "knife",
	"chop": "knife",
	"mince": "knife",
	"slice": "knife",
	"dice": "knife",
	"cube": "knife",
	"bake": "oven",
	"microwave":"microwave",
	"baste":"basting spoon",
	"grate":"grater",
	"shred":"grater",
	"measure":"measuring cups",
	"peel":"peeler",
	"core":"paring knife",
	"pare":"paring knife",
	"blend":"electric mixer",
	"skewer": "barbecue fork",
	"strain": "strainer",
	"baste": "pastry brush",
	"glaze": "pastry brush",
	"juice": "juicer",
	"stir":"wooden spoon",
	"beat": "whisk"

}


def method2tool(method):
	if method in methodToTools:
		return methodToTools[method]
	else:
   		return None


##General list of tools that a step might include
toolslist = [
"spatula",
"knife",
"cooker",
"pan",
"yogurt maker",
"peeler",
"cube tray",
"strainer",
"fruit muddler",
"freezer tray",
"plate",
"fry pan",
"cake pan",
"foil",
"cuisinart",
"grinder",
"mincer",
"hullster",
"shaker",
"grate and slice set",
"scale",
"measuring cups",
"spoon",
"fork",
"press",
"whisk",
"skimmer",
"tongs",
"potato masher",
"soup ladle",
"brush",
"an opener",
"juicer press",
"floor sifter",
"pizza wheel",
"tea ball",
"pepper grinder",
"salt shaker",
"grater",
"corkscrew",
"lid",
"bowl",
"measuring cup",
"utensil",
"egg topper",
"cheese slicer",
"scoop",
"skimmer",
"strainer",
"serve ladle",
"saute spoon",
"cutting board",
"spill stopper",
"splatter screen",
"burner",
"egg beater",
"potato ricer",
"food mill",
"grater",
"peeler",
"slicer",
"stripper",
"corn zipper",
"shear",
"snips",
"chopper",
"mandoline",
"mortar",
"pestle",
"can",
"mister",
"seal",
"stopper",
"pourer",
"scale",
"timer",
"thermometer",
"board",
"cloth",
"parchment roll",
"aluminium foil",
"cupcake liners",
"decorating pen",
"muffin papers",
"baking cups",
"baking pan",
"bags",
"smoother",
"sieve",
"wheel",
"shield",
"blender",
"scraper",
"lifter",
"gloves",
"rack",
"rolling pin",
"skewer",
"wrangler",
"oven",
"microwave",
"lighter",
"probe",
"rack",
"saucepan",
"baking dish",
"plastic bag",
"paper warp",
"pan",
"dish",
"skillet",
"casserole",
"mixing bowl",
"frying pan",
"baking sheet",
"Absinthe spoon",
"Adjustable V-rack",
"Aluminum foil",
"Aluminum stock pan",
"Anodized aluminum nonstick pan",
"Apple corer",
"Apple cutter",
"Auto reignition",
"Bachelor griller",
"Bamboo stove",
"Bar spoon",
"Barbecue",
"Barbecue grill",
"Basket rack",
"Baster",
"Beehive oven",
"Berry spoon",
"Big green egg",
"Biscuit cutter",
"Biscuit press",
"Blow torch",
"Boil over preventer",
"baking pan",
"baking sheets",
"Baking stone",
"Beanpot",
"Bedrock mortar",
"Bottle opener",
"Bottle scraper",
"Bowl",
"Braiser pan",
"Brasero",
"Brazier pot",
"Bread knife",
"Bread pan",
"Bread machine",
"Broiler pan",
"Browning tray",
"Burjiko",
"Butane torch",
"Butcher block",
"Butcher paper",
"Butter churn",
"Butter curler",
"Caddy spoon",
"Cake and pie server",
"Cake pan",
"Can opener",
"Candy thermometer",
"Carbon steel pan",
"Casserole",
"Casserole pan",
"Cassole",
"Cast iron skillet",
"Cast iron dutch oven",
"Chakla",
"Chambers stove",
"Cheesecloth",
"Cheesemelter",
"Cheese knife",
"Cheese scoop",
"Cherry pitter",
"Chestnut pan",
"Chinoise",
"Chip pan",
"Chocolatera",
"Churchkey",
"Cocktail stick",
"Coffee filter",
"coffeemaker",
"Colander",
"Convection microwave",
"Cookie cutter",
"Cookie press",
"Cookie sheet",
"Cooking pot",
"Cooking sheet",
"cooling racks",
"copper hand hammered brazing pot",
"Copper sauce pan",
"Corkscrew",
"Crab cracker",
"Crepe pan",
"Cutting board",
"Chorkor oven",
"Clean-burning stove",
"Clome oven",
"Coffee percolator",
"Coffeemaker",
"Comal (cookware)",
"Combi steamer",
"Communal oven",
"Community Cooker",
"Convection microwave",
"Convection oven",
"Cook stove",
"Corn roaster",
"Crepe maker",
"Diffuser (heat)",
"Double boiler",
"Doufeu",
"Dough blender",
"Dough scraper",
"Dutch oven",
"Deep fryer",
"Eggbeater",
"Egg piercer",
"Egg poacher",
"Egg separator",
"Egg slicer",
"Egg timer",
"Electric kettle",
"Electric water boiler",
"Embossing mat",
"Earth oven",
"EcoZoom",
"Electric cooker",
"Electric stove",
"Energy regulator",
"Fillet knife",
"Fish scalar",
"Fish slice (kitchen utensil)",
"Flat iron grill pan",
"Flat rack",
"Flesh-hook",
"Flour sifter",
"Fondue pot",
"Food mill",
"Food processor",
"Frosting spatula",
"Frying pan",
"Frying skillet",
"Funnel",
"Field kitchen",
"Fire pot",
"Flattop grill",
"Food steamer",
"Foukou",
"Fufu Machine",
"Gas stove",
"Garlic press",
"Glass baking pan",
"Gratine pan",
"Grapefruit knife",
"Grater",
"Gravy strainer",
"Greaseproof paper",
"Griddle",
"Grill pan",
"Square griddle pan",
"Hand held electric mixer",
"Herb chopper",
"Halogen oven",
"Haybox",
"Hibachi",
"Hoang Cam stove",
"Hobo stove",
"Horno",
"Hot Box (appliance)",
"Hot plate",
"Induction cooking",
"Juicer",
"Karahi",
"Kettle",
"Kitchen utensil",
"kitchen knife",
"Kamado",
"Kettle",
"Kitchen oven",
"Kitchen stove",
"Kitchener range",
"Krampouz",
"Kujiejun",
"Kyoto box",
"Ladle",
"Lame",
"Lemon reamer",
"Lemon squeezer",
"Loaf pan",
"Lobster pick",
"Lo trau",
"Mandoline",
"Mated colander pot",
"Measuring cup",
"Measuring jug",
"Measuring spoon",
"Meat grinder",
"Meat tenderizer",
"Meat thermometer",
"Meatloaf pan",
"Melon baller",
"Mezzaluna",
"Mortar and pestle",
"Microplane",
"Microwave",
"Microwave oven",
"Milk watcher",
"Mouli grater",
"Mushroom cloth",
"Masonry oven",
"Mess kit",
"Microwave oven",
"Multi-fuel stove",
"Nonadjustable V-rack",
"Nonstick skillet",
"Nutcracker",
"Nutmeg grater",
"Nomiku",
"Omelette pan",
"Oven",
"Oven bag",
"Oven glove",
"OXO (brand)",
"P-38 can opener",
"Paella pan",
"Palayok",
"Parchment paper",
"Pasta spoon",
"Pastry bag",
"Pastry blender",
"Pastry brush",
"Pastry wheel",
"Peel (tool)",
"Peeler",
"Pepper mill",
"Pie bird",
"Pie pan",
"Pizza cutter",
"Plastic wrap",
"Potato masher",
"Potato ricer",
"pot boiler",
"Pot holder",
"Pothook",
"Poultry shears",
"Pressure cooker",
"Pudding basin",
"Pudding cloth",
"Pyrex baking dish",
"Popcorn maker",
"Primus stove",
"Ramekin",
"Rice spoon",
"Ricer",
"rice cooker",
"Roasting jack",
"Roasting pan",
"Roasting pan with high cover",
"Roasting rack",
"Roller docker",
"Rolling pin",
"Rondeau",
"Round cake pan",
"Red Cross stove",
"Reflector oven",
"Remoska",
"Rice cooker",
"Rice polisher",
"Roasting jack",
"Rocket mass heater",
"Rocket stove",
"Russian oven",
"salad spoon",
"Salt and pepper shakers",
"Saran (plastic)",
"Saucier",
"saute pan",
"Saucepan",
"Sauteuse pan",
"Scales",
"Scissors",
"Scoop",
"Scotch hands",
"Scraper (kitchen)",
"Serving spoon",
"Serving tongs",
"Shellfish scraper",
"Sieve",
"Silpat",
"Skewer",
"Skillet",
"Skimmer",
"Slotted spoon",
"soup ladle",
"Spatula",
"Spider",
"splatter screen",
"Springform pan",
"Spurtle",
"Stainless steel pan",
"Stir-fry pan",
"stockpot",
"Sugar nips",
"Sugar spoon",
"Sugar thermometer",
"Sugar tong",
"Sujeo",
"Sabbath mode",
"Salamander broiler",
"Samovar",
"Sandwich toaster",
"Self-cleaning oven",
"Shichirin",
"Sigri (stove)",
"Slow cooker",
"Solar cooker",
"Soy milk maker",
"Stove",
"Susceptor",
"Tablespoon",
"Tajine",
"Tamis",
"Tava",
"Tea infuser",
"Teflon coated frying pan",
"Timbale (food)",
"Tin foil",
"Tin opener",
"Toaster oven",
"Tomato knife",
"Tongs",
"Trivection oven",
"Trivet",
"Trussing needle",
"Two burner griddle pan",
"Tabun oven",
"Tandoor",
"Tangia",
"Tea stove",
"Thermal immersion circulator",
"Toaster",
"Tommy cooker",
"Trojan Room coffee pot",
"Turkey fryer",
"Vegetable peeler",
"Vertical rack",
"Vacuum fryer",
"Wax paper",
"Whisk",
"Wok",
"Wonder pot",
"Wooden spoon",
"Waffle iron",
"Wet grinder",
"Wood-burning stove",
"Wood-fired oven",
"Zester"


]


	