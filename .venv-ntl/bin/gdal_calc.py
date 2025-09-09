#!/home/kir2351763/RRA/other trainings/DSCBI/nightlight-analysis-mireille/.venv-ntl/bin/python

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.gdal_calc as a convenience to use as a script
from osgeo_utils.gdal_calc import *  # noqa
from osgeo_utils.gdal_calc import main

deprecation_warn("gdal_calc")
sys.exit(main(sys.argv))
