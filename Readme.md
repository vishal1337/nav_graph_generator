# nav_graph_generator
    A simple script to generate nav_graph boilerplate

# Description
    - This script generates Navigation graph with all the possible fragment destinations and navigation actions.
    - This script also adds boilerplate code in Fragment files to make use of nav grah from fragments. It's intially commented, you need to uncomment the code to run.

#### Requirement : Python

##### PS: THIS IS NOT A COMPLETE SOLUTION TO INTEGRATE NAVGRAPH, BUT SERVES YOU WITH A GOOD STARTING POINT, SVAING YOU A LOT OF TIME.

##### PPS: Feel free to modify the script as per your requirements.

# How to use:

    step 1:  Goto nav_graph_generator.py and replace global variable as per your module.
    step 2:  Run 'python3 nav_graph_generator.py'. This should generate the navgraph and boilerplate code.
    step 3:  Goto generated nav_graph file and insert id and destination where indicated and reformat the file by pressing 'command + option + l' together.
    step 4:  Now Introduce FragmentContainerView in your respective Activity, and continue your development as you would.

# What it does not generate (for now):
    - Navigation Arguments
    - Back Navigation Support

### POC: Vishal Choudhary | Android