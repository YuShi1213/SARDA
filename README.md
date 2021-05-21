# SARDA
This is the core code for the paper"Unsupervised Domain Adaptation for SAR Target Detection".The complete code will be open source in the future

The CycleGAN code can be find in  https://github.com/junyanz/CycleGAN

# faster_rcnn_SARDA.py 
    the overall network architecture of our method. This is same with Figure 1 in our manuscript.
# vgg16_SARDA.py
    the classifier and feature extractor(VGG16) architecture of our method
# test_net_SARDA _pseudo.py
    the code of generating pseudo labels， instance-level and image-level score
# IPL_sort.py
    the code of sorting according to image-level score
