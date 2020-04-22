mkdir -p ../dummy_segmentation_1/gtFine
mkdir ../dummy_segmentation_1/leftImg8bit
cd ../dummy_segmentation_1/leftImg8bit
mkdir train/ val/
cd ../gtFine
mkdir train/ val/
cd ../..
cp -r ../idd_segmentation_1/gtFine/train/0  ../dummy_segmentation_1/gtFine/train/
cp -r ../idd_segmentation_1/gtFine/train/1 ../dummy_segmentation_1/gtFine/train
cp -r ../idd_segmentation_1/gtFine/val/119 ../dummy_segmentation_1/gtFine/val
cp -r ../idd_segmentation_1/gtFine/val/132 ../dummy_segmentation_1/gtFine/val
cp -r ../idd_segmentation_1/leftImg8bit/train/0 ../dummy_segmentation_1/leftImg8bit/train
cp -r ../idd_segmentation_1/leftImg8bit/train/1 ../dummy_segmentation_1/leftImg8bit/train
cp -r ../idd_segmentation_1/leftImg8bit/val/119 ../dummy_segmentation_1/leftImg8bit/val
cp -r ../idd_segmentation_1/leftImg8bit/val/132 ../dummy_segmentation_1/leftImg8bit/val
