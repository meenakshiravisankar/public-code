# set environment variables
export PYTHONPATH=$PYTHONPATH:/home/meenu/Desktop/ddp/code/autonue/public-code/helpers
export ANUE=/home/meenu/Desktop/ddp/code/autonue/idd_segmentation_2
export C=8

python3 preperation/createLabels.py --datadir $ANUE --id-type level3Id --num-workers $C

