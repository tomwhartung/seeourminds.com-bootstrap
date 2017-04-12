""" adsense.py define Google AdSense ads for our content app

Purpose: define the advertisements we are displaying to support monetization
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

import os
RUNNING_LOCALLY = os.environ.get('RUNNING_LOCALLY')

adsense_ads = {}

if RUNNING_LOCALLY:
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
        # "top_aside_top_ad":
        #     '<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>' \
        #     '<!-- Top Aside Top Ad - Responsive -->' \
        #     '<ins class="adsbygoogle" ' \
        #          'style="display:block" ' \
        #          'data-ad-client="ca-pub-2594011034406643" ' \
        #          'data-ad-slot="4475764040" ' \
        #          'data-ad-format="auto"></ins>' \
        #     '<script>' \
        #         '(adsbygoogle = window.adsbygoogle || []).push({});' \
        #     '</script>',
        "top_aside_top_ad":
            '<script async ' \
                'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
            '</script>' \
            '<!-- Top Aside Top Ad - Large Rectangle -->' \
            '<ins class="adsbygoogle" ' \
                'style="display:inline-block;width:336px;height:280px" ' \
                'data-ad-client="ca-pub-2594011034406643" ' \
                'data-ad-slot="5812896448"></ins>' \
            '<script>' \
                '(adsbygoogle = window.adsbygoogle || []).push({});' \
            '</script>',
        "top_aside_bottom_ad":
            '<p>["top_aside_bottom_ad"].</p>',
        "above_middle_row_ad":
            '<p>["above_middle_row_ad"].</p>',
        "middle_left_ad":
            '<p>["middle_left_ad"].</p>',
        "middle_right_ad":
            '<p>["middle_right_ad"].</p>',
        "below_middle_row_ad":
            '<p>["below_middle_row_ad"].</p>',
    }

