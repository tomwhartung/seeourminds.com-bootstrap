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

# #############################################################################
#
# We define global constants to contain the code we get from google.
# This makes it easier to format the code itself for PEP8 compliance, and
# makes it easier to turn ad types off and on as we zero in on how
# we want them to look.
#
# #############################################################################
#
# Ads for the aside(s) on the home page, etc.
# -------------------------------------------
#
TOP_ASIDE_TOP_LARGE_MOBILE_BANNER_IFRAME = \
    '<iframe width="320" height="100" allowtransparency="true" ' \
        'style="background: #CCCCCC"></iframe>'
TOP_ASIDE_TOP_LARGE_MOBILE_BANNER_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Top Aside Top Ad -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:inline-block;width:320px;height:100px" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="1511964445"></ins>' \
    '<script> (adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

TOP_ASIDE_TOP_LARGE_RECTANGLE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Top Aside Top Ad - Large Rectangle -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:inline-block;width:336px;height:280px" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="5812896448"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

TOP_ASIDE_TOP_RESPONSIVE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Top Aside Top Ad - Responsive -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:block" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="4475764040" ' \
        'data-ad-format="auto"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

#
# Responsive ads may vary in size.
# At first I thought this one was 190x130, now it's 322x90, and
#   I suppose it may change again
#
TOP_ASIDE_BOTTOM_RESPONSIVE_LINKS_IFRAME = \
    '<iframe width="322" height="90" allowtransparency="true" ' \
        'style="background: #CCCCCC"></iframe>'
TOP_ASIDE_BOTTOM_RESPONSIVE_LINKS_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Top Aside Bottom Ad - Responsive Links -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:block" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="5662962444" ' \
        'data-ad-format="link"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

TOP_ASIDE_BOTTOM_LARGE_MOBILE_BANNER_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Top Aside Bottom Ad - Large Mobile Banner -->' \
    '<ins class="adsbygoogle"' \
        'style="display:inline-block;width:320px;height:100px" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="1243096048"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

TOP_ASIDE_BOTTOM_RESPONSIVE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Top Aside Bottom Ad - Responsive -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:block" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="4416888448" ' \
        'data-ad-format="auto"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

# #############################################################################
#
# Leaderboard ads for the single image page, etc.
# -----------------------------------------------
#
ABOVE_MIDDLE_ROW_LARGE_LEADERBOARD_IFRAME = \
    '<iframe width="970" height="90" allowtransparency="true" ' \
        'style="background: #CCCCCC"></iframe>'
ABOVE_MIDDLE_ROW_LARGE_LEADERBOARD_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Above Middle Row Ad - Large Leaderboard -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:inline-block;width:970px;height:90px" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="7360021648"></ins> ' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

ABOVE_MIDDLE_ROW_LEADERBOARD_IFRAME = \
    '<iframe width="728" height="90" allowtransparency="true" ' \
        'style="background: #CCCCCC"></iframe>'
ABOVE_MIDDLE_ROW_LEADERBOARD_AD = \
    '<script async ' \
       'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Above Middle Row Ad - Leaderboard -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:inline-block;width:728px;height:90px" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="2929822048"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

BELOW_MIDDLE_ROW_LARGE_LEADERBOARD_IFRAME = \
    '<iframe width="970" height="90" allowtransparency="true" ' \
        'style="background: #CCCCCC"></iframe>'
BELOW_MIDDLE_ROW_LARGE_LEADERBOARD_AD = \
    ''

# #############################################################################
#
# Define the dictionary that contains the ad code, and
# populate it appropriately, based on whether we are running locally
#
adsense_ads = {}

if RUNNING_LOCALLY:
    adsense_ads = {
        "top_aside_top_ad":
            TOP_ASIDE_TOP_LARGE_MOBILE_BANNER_IFRAME,
        "top_aside_top_responsive_ad":
            '<h4>Google AdSense "top_aside_top_responsive_ad" placeholder.</h4>',
        "top_aside_bottom_ad":
            TOP_ASIDE_BOTTOM_RESPONSIVE_LINKS_IFRAME,
        "top_aside_bottom_responsive_ad":
            '<h4>Google AdSense "top_aside_bottom_responsive_ad" placeholder.</h4>',
        "above_middle_row_ad":
            ABOVE_MIDDLE_ROW_LARGE_LEADERBOARD_IFRAME,
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
            # TOP_ASIDE_TOP_LARGE_RECTANGLE_AD,
            TOP_ASIDE_TOP_LARGE_MOBILE_BANNER_AD,
        "top_aside_top_responsive_ad":
            TOP_ASIDE_TOP_RESPONSIVE_AD,
        "top_aside_bottom_ad":
            # TOP_ASIDE_BOTTOM_LARGE_MOBILE_BANNER_AD,
            TOP_ASIDE_BOTTOM_RESPONSIVE_LINKS_AD,
        "top_aside_bottom_responsive_ad":
            TOP_ASIDE_BOTTOM_RESPONSIVE_AD,
        "above_middle_row_ad":
            ABOVE_MIDDLE_ROW_LARGE_LEADERBOARD_AD,
        "middle_left_ad":
            '<p>["middle_left_ad"].</p>',
        "middle_right_ad":
            '<p>["middle_right_ad"].</p>',
        "below_middle_row_ad":
            '<p>["below_middle_row_ad"].</p>',
    }

