# chainpoly
a simple linear chain polymer model 

Atom type description:  

Type-1 and 2 : Polymer chain. Type 1 atoms are reactive sites in the polymer.  
Type-5 : Linker species  
Type-3,4,6,7 : Graphene (if any)  

**Process:**
Step  0 : start with a sparsely generated random set of chains. Relax them at finite temperature.  
Step  1 : use hydrocompression to aquire desired density.  
Step  2 : heat up the sample. activate the polymer and linkers. we reduce 'bump' in the bump-LJ to accelerate reaction (=activation)  
step  3 : Anneal  
step  4 : NPT to relax internal stresses  
step  3 : Tensile testing 
