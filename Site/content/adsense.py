""" adsense.py define Google AdSense ads for our content app

Purpose: define the advertisements we are displaying to support monetization
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

import os
USE_AD_PLACEHOLDERS = os.environ.get('USE_AD_PLACEHOLDERS')

adsense_ads = {}

if USE_AD_PLACEHOLDERS:
    adsense_ads = {
        "top_aside_top_ad":
            '<h4>Google AdSense "top_aside_top_ad" placeholder.</h4>',
        "top_aside_bottom_ad":
            '<h4>Google AdSense "top_aside_bottom_ad" placeholder.</h4>',
        "above_middle_row_ad":
            '<h4>Google AdSense "above_middle_row_ad" placeholder.</h4>',
        "middle_left_ad":
            '<h4>Google AdSense "middle_left_ad" placeholder.</h4>',
        "middle_right_ad":
            '<h4>Google AdSense "middle_right_ad" placeholder.</h4>',
        "below_middle_row_ad":
            '<h4>Google AdSense "below_middle_row_ad" placeholder.</h4>',
    }
else:
    adsense_ads = {
        "top_aside_top_ad":
            '<h4>Future Google AdSense "top_aside_top_ad" code.</h4>',
        "top_aside_bottom_ad":
            '<h4>Future Google AdSense "top_aside_bottom_ad" code.</h4>',
        "above_middle_row_ad":
            '<h4>Future Google AdSense "above_middle_row_ad" code.</h4>',
        "middle_left_ad":
            '<h4>Future Google AdSense "middle_left_ad" code.</h4>',
        "middle_right_ad":
            '<h4>Future Google AdSense "middle_right_ad" code.</h4>',
        "below_middle_row_ad":
            '<h4>Future Google AdSense "below_middle_row_ad" code.</h4>',
    }

