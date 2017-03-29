# -*- coding: utf-8 -*-

import cv2
import alpr
from modules import util
from modules import config as cfg


def apply(img):
    """
    Rescale image
    :param img: input image  
    """

    # build structuring element
    se = cv2.getStructuringElement(cv2.MORPH_RECT, cfg.MORPH_RECT_SIZE)

    # apply morphological closing -- https://goo.gl/btlvQk
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, se)

    return closing
# end function


def run(stage):
    """
    Run stage task
    :param stage: Stage number 
    :return: 
    """
    util.log("Stage", stage, "Morphological closing")
    for read in util.get_images(stage):
        # open image
        file = util.stage_image(read, stage)
        img = cv2.imread(file, cv2.CV_8UC1)

        # apply
        out = apply(img)

        # save to file
        write = util.stage_image(read, stage + 1)
        cv2.imwrite(write, out)

        # glass view
        file = util.stage_image(read, alpr.SCALED_PLATE)
        img = cv2.imread(file, cv2.CV_8UC1)
        img[out < 250] = 0
        write = util.stage_image("." + read, stage + 1)
        cv2.imwrite(write, img)

        # log
        util.log("Converted", read, stage=stage)
    # end for
# end function
