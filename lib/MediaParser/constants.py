#!usr/bin/python
# -*- coding: utf-8 -*-
#
# file_name: constants
# description: 
# author: libo
# Histort:
# 	first created: 2015/11/16

__author__ = 'libo'

class EXIFKeys(object):

    ## info
    # 标题
    DESCRIPTION = "Image ImageDescription"

    ## source
    # 程序名称
    SOFTWARE_NAME = "Image Software"
    # 拍摄日期
    DATE_TIME = "Image DateTime"

    ## image
    # 宽度
    WIDTH = "EXIF ExifImageWidth"
    # 高度
    HEIGHT = "EXIF ExifImageLength"
    # 水平分辨率
    X_RESOLUTION = "Image XResolution"
    # 垂直分辨率
    Y_RESOLUTION = "Image YResolution"
    # 分辨率单位
    RESOLUTION_UNIT = "Image ResolutionUnit"

    ## camera
    # 制造商
    MAKE = "Image Make"
    # 型号
    MODEL = "Image Model"
    # 曝光时间
    EXPOSURE_TIME = "EXIF ExposureTime"
    # ISO速度
    ISO_SPEED = "EXIF ISOSpeedRatings"
    # 曝光补偿
    EXPOSURE_BIAS_VALUE = "EXIF ExposureBiasValue"
    # 焦距
    FOCAL_LENGTH = "EXIF FocalLength"
    # 最大光圈
    APERTURE_VALUE = "EXIF ApertureValue"
    # 光圈值
    F_NUMBER = "EXIF FNumber"
    # 35mm焦距
    FOCAL_LENGTH_IN_35MM_FILM = "EXIF FocalLengthIn35mmFilm"
    # 测光模式
    METERING_MODE = "EXIF MeteringMode"

    ## GPS
    # 经度
    GPS_LONGITUDE = "GPS GPSLongitude"
    # 纬度
    GPS_LATITUDE = "GPS GPSLatitude"

    ## 高级
    # 白平衡
    WHITE_BALANCE = "EXIF WhiteBalance"
    # 清晰度
    SHARPNESS = "EXIF Sharpness"
    # #
    # EXPOSURE_MODE = "EXIF ExposureMode"
    # 曝光程序
    EXPOSURE_PROGRAM = "EXIF ExposureProgram"
    # 饱和度
    SATURATION = "EXIF Saturation"
    # #
    SCENE_CAPTURE_TYPE = "EXIF SceneCaptureType"
    # 对比度
    CONTRAST = "EXIF Contrast"
    # 快门速度
    SHUTTER = "EXIF ShutterSpeedValue"

    # file

class EXIFValues(object):

    WHITE_BALANCE_AUTO = 0
    WHITE_BALANCE_MANUAL = 1

    SHARPNESS_NORMAL = 0
    SHARPNESS_SOFT = 1
    SHARPNESS_HARD = 2

    # EXPOSURE_MODE_AUTO = 0
    # EXPOSURE_MODE_MANUAL = 1
    # EXPOSURE_MODE_AUTO_BRAKEY = 2

    EXPOSURE_PROGRAM_UNIDENTIFIED = 0
    EXPOSURE_PROGRAM_MANUAL = 1
    EXPOSURE_PROGRAM_PROGRAM_NORMAL = 2
    EXPOSURE_PROGRAM_APERTURE_PRIORITY = 3
    EXPOSURE_PROGRAM_SHUTTER_PRIORITY = 4
    EXPOSURE_PROGRAM_PROGRAM_CREATIVE = 5
    EXPOSURE_PROGRAM_PROGRAM_ACTION = 6
    EXPOSURE_PROGRAM_PORTRAIT_MODE = 7
    EXPOSURE_PROGRAM_LANDSCAPE_MODE = 8

    SATURATION_NORMAL = 0
    SATURATION_SOFT = 1
    SATURATION_HARD = 2

    SCENE_CAPTURE_TYPE_STANDARD = 0
    SCENE_CAPTURE_TYPE_LANDSCAPE = 1
    SCENE_CAPTURE_TYPE_PROTRAIT = 2
    SCENE_CAPTURE_TYPE_NIGHT = 3

    METERING_MODE_UNIDENTIFIED = 0
    METERING_MODE_AVERAGE = 1
    METERING_MODE_CENTER_WEIGHTED_AVERAGE = 2
    METERING_MODE_SPOT = 3
    METERING_MODE_MULTI_SPOT = 4
    METERING_MODE_PATTERN = 5
    METERING_MODE_PARTIAL = 6
    METERING_MODE_OTHER = 255

    CONTRAST_NORMAL = 0
    CONTRAST_SOFT = 1
    CONTRAST_HARD = 2

class Constants(EXIFKeys, EXIFValues):
    pass

class EXIFKeysTrans(object):

    ## info
    # 标题
    DESCRIPTION = u"标题"

    ## source
    # 程序名称
    SOFTWARE_NAME = u"程序名称"
    # 拍摄日期
    DATE_TIME = u"拍摄日期"

    ## image
    # 宽度
    WIDTH = u"宽度"
    # 高度
    HEIGHT = u"高度"
    # 水平分辨率
    X_RESOLUTION = u"水平分辨率"
    # 垂直分辨率
    Y_RESOLUTION = u"垂直分辨率"
    # 分辨率单位
    RESOLUTION_UNIT = u"分辨率单位"

    ## camera
    # 制造商
    MAKE = u"制造商"
    # 型号
    MODEL = u"型号"
    # 曝光时间
    EXPOSURE_TIME = u"曝光时间"
    # ISO速度
    ISO_SPEED = u"ISO速度"
    # 曝光补偿
    EXPOSURE_BIAS_VALUE = u"曝光补偿"
    # 焦距
    FOCAL_LENGTH = u"焦距"
    # 最大光圈
    APERTURE_VALUE = u"最大光圈"
    # 光圈值
    F_NUMBER = u"光圈值"
    # 35mm焦距
    FOCAL_LENGTH_IN_35MM_FILM = u"35mm焦距"
    # 测光模式
    METERING_MODE = u"测光模式"

    ## GPS
    # 经度
    GPS_LONGITUDE = u"经度"
    # 纬度
    GPS_LATITUDE = u"纬度"

    ## 高级
    # 白平衡
    WHITE_BALANCE = u"白平衡"
    # 清晰度
    SHARPNESS = u"清晰度"
    # #
    # EXPOSURE_MODE = "EXIF ExposureMode"
    # 曝光程序
    EXPOSURE_PROGRAM = u"曝光程序"
    # 饱和度
    SATURATION = u"饱和度"
    # #
    SCENE_CAPTURE_TYPE = "EXIF SceneCaptureType"
    # 对比度
    CONTRAST = u"对比度"
    # 快门速度
    SHUTTER = u"快门速度"

    # file

class EXIFValuesTrans(object):

    WHITE_BALANCE_AUTO = u"自动"
    WHITE_BALANCE_MANUAL = u"手动"

    SHARPNESS_NORMAL = u"正常"
    SHARPNESS_SOFT = u"柔和"
    SHARPNESS_HARD = u"强硬"

    # EXPOSURE_MODE_AUTO = "自动"
    # EXPOSURE_MODE_MANUAL = "手动"
    # EXPOSURE_MODE_AUTO_BRAKEY = "Brakey"

    EXPOSURE_PROGRAM_UNIDENTIFIED = u"未知"
    EXPOSURE_PROGRAM_MANUAL = u"手动"
    EXPOSURE_PROGRAM_PROGRAM_NORMAL = u"正常"
    EXPOSURE_PROGRAM_APERTURE_PRIORITY = u"光圈优先"
    EXPOSURE_PROGRAM_SHUTTER_PRIORITY = u"快门优先"
    EXPOSURE_PROGRAM_PROGRAM_CREATIVE = u"生成"
    EXPOSURE_PROGRAM_PROGRAM_ACTION = u"动作"
    EXPOSURE_PROGRAM_PORTRAIT_MODE = u"肖像"
    EXPOSURE_PROGRAM_LANDSCAPE_MODE = u"风景"

    SATURATION_NORMAL = u"正常"
    SATURATION_SOFT = u"柔和"
    SATURATION_HARD = u"强硬"

    SCENE_CAPTURE_TYPE_STANDARD = "标准"
    SCENE_CAPTURE_TYPE_LANDSCAPE = "风景"
    SCENE_CAPTURE_TYPE_PROTRAIT = "肖像"
    SCENE_CAPTURE_TYPE_NIGHT = "夜晚"

    METERING_MODE_UNIDENTIFIED = u"未知"
    METERING_MODE_AVERAGE = u"平均"
    METERING_MODE_CENTER_WEIGHTED_AVERAGE = u"中心加权平均"
    METERING_MODE_SPOT = u"点"
    METERING_MODE_MULTI_SPOT = u"多点"
    METERING_MODE_PATTERN = u"图案"
    METERING_MODE_PARTIAL = u"局部"
    METERING_MODE_OTHER = u"其他"

    CONTRAST_NORMAL = u"正常"
    CONTRAST_SOFT = u"柔和"
    CONTRAST_HARD = u"强硬"

class ConstantsTrans(EXIFKeysTrans, EXIFValuesTrans):
    pass

