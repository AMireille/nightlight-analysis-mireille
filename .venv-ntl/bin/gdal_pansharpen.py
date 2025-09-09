#!/home/kir2351763/RRA/other trainings/DSCBI/nightlight-analysis-mireille/.venv-ntl/bin/python

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.gdal_pansharpen as a convenience to use as a script
from osgeo_utils.gdal_pansharpen import *  # noqa
from osgeo_utils.gdal_pansharpen import main

deprecation_warn("gdal_pansharpen")
sys.exit(main(sys.argv))
