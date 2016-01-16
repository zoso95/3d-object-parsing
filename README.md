# 3d-object-parsing

This is a few wrapper scripts around osm-bundler for making doing 3d reconstruction easier!

The main purpose of these projects are to go from a video of a scene, to point clouds of the individual objects in that scene.

To get this to work you will need to do a few things. Install osm-bundler, scipy, ffmeg, and change the directory headers in the two python scripts. Then you should be good to go.

An osm-bundler installation guide can be found [here](https://code.google.com/p/osm-bundler/wiki/InstallingRunningApplication),
a more windows centric installer guide I wrote a few years back can be found [here](https://docs.google.com/document/d/1nJNgV-KMxMjvZnSlLsdt8aoR6WnSmQjMxfqSZG0gsjw/edit?usp=sharing)
and finally a guide on making 3d models from point clouds I wrote a fews year ago can be found [here](https://docs.google.com/document/d/1kDlOnqkK1m8xxzZs5vqCHn5cUBJ-ftCyIm1bl2rFGQQ/edit?usp=sharing)

The example folder contains a video and the corresponding point cloud reconstruction. 

To see cool demos of what you can do with the technology, check out a [previous project](http://ctle.utah.edu/uset/students/bradway.php#pane4) I did. 
