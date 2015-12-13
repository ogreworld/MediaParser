#!usr/bin/python
# -*- coding: utf-8 -*-
#
# file_name: media_parser
# description: 
# author: libo
# Histort:
# 	first created: 2015/11/16

__author__ = 'libo'

import exifread
import PyLogger

from constants import *

class MediaParser(Constants):
    '''
    This class is made for parsing exif string
    '''

    def __init__(self, file_obj=None):
        '''
        init function
        :param file_obj: could be a string or file object
        :return: None
        '''
        self.logger = PyLogger.getLogger(self.__class__.__name__)
        self.exif_obj = {}
        if file_obj is not None:
            self.parse_file(file_obj)

    def parse_file(self, file_obj):
        '''
        parse the file_obj to exif strings
        :param file_obj: could be a string or file object
        :return: exif object
        '''
        self.logger.debug("Parse for %s"%file_obj)
        if isinstance(file_obj, str):
            file_obj = open(file_obj, "rb")

        self.exif_obj = exifread.process_file(file_obj)
        file_obj.close()
        return self.exif_obj


    def get_item_value(self, item_key, is_trans=False):
        '''
        get the item value of exif strings
        :param item_key: attribute of EXIFKeys
        :param is_trans: tranlation or not
        :return: value for the key
        '''
        self.logger.debug("Get value of %s"%item_key)
        if self.exif_obj.has_key(item_key):
            value = self.exif_obj[item_key]
            if isinstance(value, str):
                return value
            elif len(value.values) == 1:
                tmp = value.values[0]
                if isinstance(tmp, exifread.utils.Ratio):
                    if tmp.den != 0:
                        return float(tmp.num)/float(tmp.den)
                    else:
                        return [tmp.num, tmp.den]
                else:
                    return tmp
            else:
                return value.values
        else:
            self.logger.warn("Item %s is not found"%item_key)

    def get_all_settings(self, is_trans=False):
        '''
        get all exif strings
        :param is_trans: translation or not
        :return: dict of exif keys and values
        '''
        curr_settings = {}
        if not is_trans:

            for key in dir(EXIFKeys):
                if not "__" in key:
                    item_key = getattr(EXIFKeys, key)
                    curr_settings.update({item_key:self.get_item_value(item_key)})
        else:

            for key in dir(EXIFKeys):
                if not "__" in key:
                    item_key = getattr(EXIFKeys, key)
                    item_key_trans = getattr(EXIFKeysTrans, key)
                    item_value = self.get_item_value(item_key)
                    item_value_trans = item_value
                    for value in dir(EXIFValues):
                        if key in value and getattr(EXIFValues, value) == item_value:
                            item_value_trans = getattr(EXIFValuesTrans, value)
                            break

                    curr_settings.update({item_key_trans:item_value_trans})
        return curr_settings



