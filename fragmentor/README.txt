Command line and example files downloaded from Webina (https://durrantlab.pitt.edu/webina/), Apache license 2.0


Hints for the web team
======================

Further pointers to create Seamless web interfaces (inside Docker image):
    cd ~/seamless-tests/highlevel =>
        Look at share-pdb.py
        Run ipython3 -i ~/seamless-scripts/serve-graph.py -- share-pdb.seamless share-pdb.zip --mounts 1 --interactive
    cd ~/seamless-examples/datatables =>
        Look at gen-context.py
        Run ipython3 -i ~/seamless-scripts/serve-graph.py -- datatables.seamless datatables.zip --mounts 1 --interactive
