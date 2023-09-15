
########################################################################################################################
#######################################  To find the corner ID of the building  ########################################

# Required packages are imported
# Please install the packages to run the code (Details at "Read_Me" file)
from OSMPythonTools.api import Api
import overpy
import osmapi as osm
from geopy.distance import geodesic
from itertools import combinations

# Prompt the user to input the "way ID" from OSM, details is in "Read_Me" file
way_id = input("Enter the way ID from OSM: ")

# An "api" object is created with Api function
api = Api()

# The created "api" object is used to do query with "query" function
way = api.query(f'way/{way_id}')

# The provided Tags at OSM is printed. These will show building address, building types, building levels
print("Building Address = ", way.tag('addr:street'), way.tag('addr:housenumber'), way.tag('addr:postcode'), way.tag('addr:city'))
print("Building Type = ", way.tag('building'))
if way.tag('building') == 'yes':
    print("Type =", 'Building')


# way.tag('building:levels') is regarded as an object named "way_levels"
way_levels = way.tag('building:levels')

# If tag('building:levels') is not provided in OSM, it is by default 1
if way_levels is None:
    BuildingLevel = 1
    print("Number of Building Levels = ", BuildingLevel)

# If tag('building:levels') is provided in OSM, it is by default that respective value
else:
    BuildingLevel = way.tag('building:levels')
    print("Number of Building Levels = ", BuildingLevel)


print("\n")
api_2 = overpy.Overpass()        # Creating an object of the Overpass API

# For the provided way_id and its geometry, Query is done
result = api_2.query(f"[out:json];way({way_id});out geom;")

CornerNodeID = []                # To store the corner node IDs, an empty list is created
CornerNodeID = result.ways       # Assigning the ways from the result(from Query) to the list named "CornerNodeID"
#CornerNodeID = [CornerNodeID]

for x in CornerNodeID:           # With for loop, iteration is done over the CornerNodeID list
    print(x)


################################ From Node ID to respective Latitude and Longitude #####################################

api_1 = osm.OsmApi()  # instantiate the OsmApi class

# Prompting the user to enter the node IDs
nodeID = []
num_nodes = int(input("Enter the number of Node IDs (Acknowledging from above nodes Array): "))

# Iterating for the specified number of nodes with for loop
for i in range(num_nodes):
    node = int(input(f"Enter Node ID {i+1} (From above nodes array): "))
    nodeID.append(node)                          # The node IDs are added to the nodeID list

print("Number of Node IDs =", len(nodeID))       # The number of node IDs is printed

# 5 Global variables are declared for the most common type buildings that has 5 nodes
FirstNode = (api_1.NodeGet(nodeID[0])["lat"], api_1.NodeGet(nodeID[0])["lon"])
SecondNode = (api_1.NodeGet(nodeID[1])["lat"], api_1.NodeGet(nodeID[1])["lon"])
ThirdNode = (api_1.NodeGet(nodeID[2])["lat"], api_1.NodeGet(nodeID[2])["lon"])
FourthNode = (api_1.NodeGet(nodeID[3])["lat"], api_1.NodeGet(nodeID[3])["lon"])
FifthNode = (api_1.NodeGet(nodeID[4])["lat"], api_1.NodeGet(nodeID[4])["lon"])

print("\n")

for x in nodeID:                                   # Iteration over the node ID list
    node = api_1.NodeGet(x)
    print("For Node ID ", x, "Latitude & Longitude is  : ", (node["lat"], node["lon"]))  # The latitude and logitude is getting Printed

################################  Calculating the edges by distances from Corner Nodes  ################################

EdgeSize = []

if num_nodes == 5:
    # Calculating and adding the edge sizes to the EdgeSize list
    # The distance is found using geodesic() function and then rounded upto 3 decimal places
    # Based on Combination formula, all possible edges are calculated

    five_nodes = [FirstNode, SecondNode, ThirdNode, FourthNode, FifthNode]
    EdgeSize = [round(geodesic(five_nodes[i], five_nodes[j]).meters, 3) for i, j in combinations(range(len(five_nodes)), 2)]

    # EdgeSize = [round(geodesic(FirstNode, SecondNode).meters, 3),
    #            round(geodesic(FirstNode, ThirdNode).meters, 3),
    #            .................................................
    #            round(geodesic(FourthNode, FifthNode).meters, 3)]


elif num_nodes == 6:
    # Needed "Local Variables" are added
    SixthNode = (api_1.NodeGet(nodeID[5])["lat"], api_1.NodeGet(nodeID[5])["lon"])

    # Calculating and adding the edge sizes to the EdgeSize list
    # The distance is found using geodesic() function and then rounded upto 3 decimal places
    # Based on Combination formula, all possible edges are calculated

    six_nodes = [FirstNode, SecondNode, ThirdNode, FourthNode, FifthNode, SixthNode]
    EdgeSize = [round(geodesic(six_nodes[i], six_nodes[j]).meters, 3) for i, j in
                combinations(range(len(six_nodes)), 2)]

elif num_nodes == 7:
    # Needed "Local Variables" are added
    SixthNode = (api_1.NodeGet(nodeID[5])["lat"], api_1.NodeGet(nodeID[5])["lon"])
    SeventhNode = (api_1.NodeGet(nodeID[6])["lat"], api_1.NodeGet(nodeID[6])["lon"])

    # Calculating and adding the edge sizes to the EdgeSize list
    # The distance is found using geodesic() function and then rounded upto 3 decimal places
    # Based on Combination formula, all possible edges are calculated

    seven_nodes = [FirstNode, SecondNode, ThirdNode, FourthNode, FifthNode, SixthNode, SeventhNode]
    EdgeSize = [round(geodesic(seven_nodes[i], seven_nodes[j]).meters, 3) for i, j in
                combinations(range(len(seven_nodes)), 2)]

elif num_nodes == 8:
    # Needed "Local Variables" are added
    SixthNode = (api_1.NodeGet(nodeID[5])["lat"], api_1.NodeGet(nodeID[5])["lon"])
    SeventhNode = (api_1.NodeGet(nodeID[6])["lat"], api_1.NodeGet(nodeID[6])["lon"])
    EighthNode = (api_1.NodeGet(nodeID[7])["lat"], api_1.NodeGet(nodeID[7])["lon"])

    # Calculating and adding the edge sizes to the EdgeSize list
    # The distance is found using geodesic() function and then rounded upto 3 decimal places
    # Based on Combination formula, all possible edges are calculated

    eight_nodes = [FirstNode, SecondNode, ThirdNode, FourthNode, FifthNode, SixthNode, SeventhNode, EighthNode]
    EdgeSize = [round(geodesic(eight_nodes[i], eight_nodes[j]).meters, 3) for i, j in combinations(range(len(eight_nodes)), 2)]


elif num_nodes == 9:
    # Needed "Local Variables" are added
    SixthNode = (api_1.NodeGet(nodeID[5])["lat"], api_1.NodeGet(nodeID[5])["lon"])
    SeventhNode = (api_1.NodeGet(nodeID[6])["lat"], api_1.NodeGet(nodeID[6])["lon"])
    EighthNode = (api_1.NodeGet(nodeID[7])["lat"], api_1.NodeGet(nodeID[7])["lon"])
    NinthNode = (api_1.NodeGet(nodeID[8])["lat"], api_1.NodeGet(nodeID[8])["lon"])

    # Calculating and adding the edge sizes to the EdgeSize list
    # The distance is found using geodesic() function and then rounded upto 3 decimal places
    # Based on Combination formula, all possible edges are calculated

    nine_nodes = [FirstNode, SecondNode, ThirdNode, FourthNode, FifthNode, SixthNode, SeventhNode, EighthNode, NinthNode]
    EdgeSize = [round(geodesic(nine_nodes[i], nine_nodes[j]).meters, 3) for i, j in
                combinations(range(len(nine_nodes)), 2)]

elif num_nodes == 10:
    # Needed "Local Variables" are added
    SixthNode = (api_1.NodeGet(nodeID[5])["lat"], api_1.NodeGet(nodeID[5])["lon"])
    SeventhNode = (api_1.NodeGet(nodeID[6])["lat"], api_1.NodeGet(nodeID[6])["lon"])
    EighthNode = (api_1.NodeGet(nodeID[7])["lat"], api_1.NodeGet(nodeID[7])["lon"])
    NinthNode = (api_1.NodeGet(nodeID[8])["lat"], api_1.NodeGet(nodeID[8])["lon"])
    TenthNode = (api_1.NodeGet(nodeID[9])["lat"], api_1.NodeGet(nodeID[9])["lon"])

    # Calculating and adding the edge sizes to the EdgeSize list
    # The distance is found using geodesic() function and then rounded upto 3 decimal places
    # Based on Combination formula, all possible edges are calculated
    ten_nodes = [FirstNode, SecondNode, ThirdNode, FourthNode, FifthNode, SixthNode, SeventhNode, EighthNode,
                  NinthNode, TenthNode]
    EdgeSize = [round(geodesic(ten_nodes[i], ten_nodes[j]).meters, 3) for i, j in
                combinations(range(len(ten_nodes)), 2)]

elif num_nodes == 11:
    # Needed "Local Variables" are added
    SixthNode = (api_1.NodeGet(nodeID[5])["lat"], api_1.NodeGet(nodeID[5])["lon"])
    SeventhNode = (api_1.NodeGet(nodeID[6])["lat"], api_1.NodeGet(nodeID[6])["lon"])
    EighthNode = (api_1.NodeGet(nodeID[7])["lat"], api_1.NodeGet(nodeID[7])["lon"])
    NinthNode = (api_1.NodeGet(nodeID[8])["lat"], api_1.NodeGet(nodeID[8])["lon"])
    TenthNode = (api_1.NodeGet(nodeID[9])["lat"], api_1.NodeGet(nodeID[9])["lon"])
    EleventhNode = (api_1.NodeGet(nodeID[10])["lat"], api_1.NodeGet(nodeID[10])["lon"])

    # Calculating and adding the edge sizes to the EdgeSize list
    # The distance is found using geodesic() function and then rounded upto 3 decimal places
    # Based on Combination formula, all possible edges are calculated

    eleven_nodes = [FirstNode, SecondNode, ThirdNode, FourthNode, FifthNode, SixthNode, SeventhNode, EighthNode,
                 NinthNode, TenthNode, EleventhNode]
    EdgeSize = [round(geodesic(eleven_nodes[i], eleven_nodes[j]).meters, 3) for i, j in
                combinations(range(len(eleven_nodes)), 2)]

elif num_nodes == 12:
    # Needed "Local Variables" are added
    SixthNode = (api_1.NodeGet(nodeID[5])["lat"], api_1.NodeGet(nodeID[5])["lon"])
    SeventhNode = (api_1.NodeGet(nodeID[6])["lat"], api_1.NodeGet(nodeID[6])["lon"])
    EighthNode = (api_1.NodeGet(nodeID[7])["lat"], api_1.NodeGet(nodeID[7])["lon"])
    NinthNode = (api_1.NodeGet(nodeID[8])["lat"], api_1.NodeGet(nodeID[8])["lon"])
    TenthNode = (api_1.NodeGet(nodeID[9])["lat"], api_1.NodeGet(nodeID[9])["lon"])
    EleventhNode = (api_1.NodeGet(nodeID[10])["lat"], api_1.NodeGet(nodeID[10])["lon"])
    TwelfthNode = (api_1.NodeGet(nodeID[11])["lat"], api_1.NodeGet(nodeID[11])["lon"])

    # Calculating and adding the edge sizes to the EdgeSize list
    # The distance is found using geodesic() function and then rounded upto 3 decimal places
    # Based on Combination formula, all possible edges are calculated

    twelve_nodes = [FirstNode, SecondNode, ThirdNode, FourthNode, FifthNode, SixthNode, SeventhNode, EighthNode,
                    NinthNode, TenthNode, EleventhNode, TwelfthNode]
    EdgeSize = [round(geodesic(twelve_nodes[i], twelve_nodes[j]).meters, 3) for i, j in
                combinations(range(len(twelve_nodes)), 2)]

elif num_nodes == 13:
    # Needed "Local Variables" are added
    SixthNode = (api_1.NodeGet(nodeID[5])["lat"], api_1.NodeGet(nodeID[5])["lon"])
    SeventhNode = (api_1.NodeGet(nodeID[6])["lat"], api_1.NodeGet(nodeID[6])["lon"])
    EighthNode = (api_1.NodeGet(nodeID[7])["lat"], api_1.NodeGet(nodeID[7])["lon"])
    NinthNode = (api_1.NodeGet(nodeID[8])["lat"], api_1.NodeGet(nodeID[8])["lon"])
    TenthNode = (api_1.NodeGet(nodeID[9])["lat"], api_1.NodeGet(nodeID[9])["lon"])
    EleventhNode = (api_1.NodeGet(nodeID[10])["lat"], api_1.NodeGet(nodeID[10])["lon"])
    TwelfthNode = (api_1.NodeGet(nodeID[11])["lat"], api_1.NodeGet(nodeID[11])["lon"])
    ThirteenthNode = (api_1.NodeGet(nodeID[12])["lat"], api_1.NodeGet(nodeID[12])["lon"])

    # Calculating and adding the edge sizes to the EdgeSize list
    # The distance is found using geodesic() function and then rounded upto 3 decimal places
    # Based on Combination formula, all possible edges are calculated

    thirteen_nodes = [FirstNode, SecondNode, ThirdNode, FourthNode, FifthNode, SixthNode, SeventhNode, EighthNode,
                    NinthNode, TenthNode, EleventhNode, TwelfthNode, ThirteenthNode]
    EdgeSize = [round(geodesic(thirteen_nodes[i], thirteen_nodes[j]).meters, 3) for i, j in
                combinations(range(len(thirteen_nodes)), 2)]

########################################################################################################################
################################  CALCULATING THE AREA OF AN UNIFORM SIZED BUILDING  ###################################
########################################################################################################################
print("\n")

# Define the categories
categories = {
    1: "Rectangular Building",
    2: "Front Door Ahead Building",
    3: "Ahead Door Cutting Edge Building",
    4: "L-Shaped Building"
}

# Display the categories
print("Building Categories:")
for category_number, category_name in categories.items():
    print(f"Category {category_number}: {category_name}")

print("\n")
# Asking the user to select a category
selected_category = int(input("Please enter the category number that best represents your building: "))

# Validate the selected category
if selected_category in categories:
    chosen_category = categories[selected_category]
    print(f"You have selected Category {selected_category}: {chosen_category}")
else:
    print("Invalid category number. Please try again.")


if selected_category == 1:
    print("\n")
    print("                                    Edge Size    : ", EdgeSize)

    # Sorting the EdgeSize list in reverse order (from max to min)
    EdgeSize.sort(reverse=True)
    print("                Sorted Edge Size from max to min : ", EdgeSize)
    print("\n")

    import collections
    RevisedEdgeSize = []
    RevisedEdgeSize = [item for item, count in collections.Counter(EdgeSize).items() if count > 1]
    print("             Revised EdgeSize Array (Max to min) : ", RevisedEdgeSize)

    # Ground-floor area is calculated
    # Calculating the house area with corner edges representing wide and length
    print("Building-area of the ground level  (in meter sqr): ", round(RevisedEdgeSize[1] * RevisedEdgeSize[2]), 3)

    # Total area including all levels is calculated when way.tag('building:levels') is not provided
    if way.tag('building:levels') == ['None']:
        print("      Building-area of all levels  (in meter sqr): ", round(RevisedEdgeSize[1] * RevisedEdgeSize[2]), 3)
    else:
        # BuildingLevel is predefined variable representing the number of levels
        # Total area including all levels is calculated when way.tag('building:levels') is provided
        print("      Building-area of all levels  (in meter sqr): ",
              round(RevisedEdgeSize[1] * RevisedEdgeSize[2] * BuildingLevel, 3))



if selected_category == 2:
    print("\n")
    print("                                    Edge Size    : ", EdgeSize)

    # Sorting the EdgeSize list in reverse order (from max to min)
    EdgeSize.sort(reverse=True)
    print("                Sorted Edge Size from max to min : ", EdgeSize)
    print("\n")

    # Ground-floor area is calculated
    print("Building-area of the ground level  (in meter sqr): ",
          round((EdgeSize[4] * EdgeSize[6]) + (EdgeSize[-5] * EdgeSize[-9]), 3))

    # Total area including all levels is calculated when way.tag('building:levels') is not provided
    if way.tag('building:levels') == ['None']:
        print("      Building-area of all levels  (in meter sqr): ",
              round((EdgeSize[4] * EdgeSize[6]) + (EdgeSize[-5] * EdgeSize[-9]), 3))
    else:
        # BuildingLevel is predefined variable representing the number of levels
        # Total area including all levels is calculated when way.tag('building:levels') is provided
        print("      Building-area of all levels  (in meter sqr): ",
              round(((EdgeSize[4] * EdgeSize[6]) + (EdgeSize[-5] * EdgeSize[-9])) * BuildingLevel, 3))



if selected_category == 3:
    print("\n")
    print("                                    Edge Size    : ", EdgeSize)

    # Sorting the EdgeSize list in reverse order (from max to min)
    EdgeSize.sort(reverse=True)
    print("                Sorted Edge Size from max to min : ", EdgeSize)
    print("\n")

    # Ground-floor area is calculated
    print("Building-area of the ground level  (in meter sqr): ",
          round((EdgeSize[4] * EdgeSize[6]) + (EdgeSize[-5] * EdgeSize[-9]) - 0.5 * (EdgeSize[-2] * EdgeSize[-3]), 3))

    # Total area including all levels is calculated when way.tag('building:levels') is not provided
    if way.tag('building:levels') == ['None']:
        print("      Building-area of all levels  (in meter sqr): ",
              round((EdgeSize[4] * EdgeSize[6]) + (EdgeSize[-5] * EdgeSize[-9]) - 0.5 * (EdgeSize[-2] * EdgeSize[-3]), 3))
    else:
        # BuildingLevel is predefined variable representing the number of levels
        # Total area including all levels is calculated when way.tag('building:levels') is provided
        print("      Building-area of all levels  (in meter sqr): ",
              round(((EdgeSize[4] * EdgeSize[6]) + (EdgeSize[-5] * EdgeSize[-9]) - 0.5 * (EdgeSize[-2] * EdgeSize[-3])) * BuildingLevel, 3))


if selected_category == 4:
    print("\n")
    print("                                    Edge Size    : ", EdgeSize)

    # Sorting the EdgeSize list in reverse order (from max to min)
    EdgeSize.sort(reverse=True)
    print("                Sorted Edge Size from max to min : ", EdgeSize)
    print("\n")

    # Ground-floor area is calculated
    print("Building-area of the ground level  (in meter sqr): ",
          round((EdgeSize[3] * EdgeSize[5]) + (EdgeSize[-4] * EdgeSize[11]), 3))

    # Total area including all levels is calculated when way.tag('building:levels') is not provided
    if way.tag('building:levels') == ['None']:
        print("      Building-area of all levels  (in meter sqr): ",
              round((EdgeSize[3] * EdgeSize[5]) + (EdgeSize[-4] * EdgeSize[11]), 3))
    else:
        # BuildingLevel is predefined variable representing the number of levels
        # Total area including all levels is calculated when way.tag('building:levels') is provided
        print("      Building-area of all levels  (in meter sqr): ",
              round((EdgeSize[3] * EdgeSize[5]) + (EdgeSize[-4] * EdgeSize[11]), 3))

else:
    # Invalid category
    print("Invalid category number. Please select a valid category.")

