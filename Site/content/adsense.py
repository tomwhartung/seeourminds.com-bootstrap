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
# #############################################################################
#
# We define global constants to contain the code we get from google.
# This makes it easier to format the code itself for PEP8 compliance, and
# makes it easier to turn ad types off and on as we zero in on how
# we want them to look.
#
# RTFMIW - Read The Freakin Manual I Wrote:
#   https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/google/adsense.md
#
# #############################################################################
# #############################################################################
#
# TOP_ROW_LARGE_*BOARD_ADs: for the very tops of pages
# ----------------------------------------------------
#
TOP_ROW_LARGE_BILLBOARD_IFRAME = \
    '<iframe width="970" height="250" allowtransparency="true" ' \
        'id="top-row-large-billboard-ad" style="background: #CCCCCC"></iframe>'
TOP_ROW_LARGE_BILLBOARD_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Top Row Ad - Billboard -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:inline-block;width:970px;height:250px" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="9898235241"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

TOP_ROW_LARGE_LEADERBOARD_IFRAME = \
    '<iframe width="970" height="90" allowtransparency="true" ' \
        'id="top-row-large-leaderboard-ad" style="background: #CCCCCC"></iframe>'
TOP_ROW_LARGE_LEADERBOARD_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Top Row Ad - Large Leaderboard -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:inline-block;width:970px;height:90px" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="6194562442"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

# #############################################################################
#
# TOP_LEFT_RESPONSIVE_AD for the upper left corner on the galleries pages
# -----------------------------------------------------------------------
#
TOP_LEFT_RESPONSIVE_IFRAME = \
    '<iframe width="320" height="320" allowtransparency="true" ' \
        'id="top-left-responsive-ad" style="background: #CCCCCC"></iframe>'
TOP_LEFT_RESPONSIVE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Top Left Ad - Responsive -->' \
    '<ins class="adsbygoogle" ' \
         'style="display:block" ' \
         'data-ad-client="ca-pub-2594011034406643" ' \
         'data-ad-slot="7003644444" ' \
         'data-ad-format="auto"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

# #############################################################################
#
# TOP_ASIDE_TOP_*_ADs: for above the email form
# ---------------------------------------------
#
TOP_ASIDE_TOP_LARGE_MOBILE_BANNER_IFRAME = \
    '<iframe width="320" height="100" allowtransparency="true" ' \
        'id="top-aside-top-large-mobile-banner-ad" style="background: #CCCCCC"></iframe>'
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

TOP_ASIDE_TOP_RESPONSIVE_IFRAME = \
    '<iframe width="320" height="320" allowtransparency="true" ' \
        'id="top-aside-top-responsive-ad" style="background: #CCCCCC"></iframe>'
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

# #############################################################################
#
# TOP_ASIDE_BOTTOM_*_ADs: for below the email form
# ------------------------------------------------
# Responsive ads may vary in size (I think?)
# At least, responsive ads may be a different size than responsive links
# At first I thought this one was 190x130, now it's 322x90, and
#   I suppose it may change again
#
TOP_ASIDE_BOTTOM_RESPONSIVE_LINKS_IFRAME = \
    '<iframe width="322" height="90" allowtransparency="true" ' \
        'id="top-aside-bottom-responsive-links-ad" style="background: #CCCCCC"></iframe>'
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

TOP_ASIDE_BOTTOM_RESPONSIVE_IFRAME = \
    '<iframe width="320" height="320" allowtransparency="true" ' \
        'id="top-aside-bottom-responsive-ad" style="background: #CCCCCC"></iframe>'
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
# *_ROW_LARGE_LEADERBOARD_ADs: for the single image page, etc.
# ------------------------------------------------------------
#
ABOVE_MIDDLE_ROW_LARGE_LEADERBOARD_IFRAME = \
    '<iframe width="970" height="90" allowtransparency="true" ' \
        'id="above-middle-row-large-leaderboard-ad" style="background: #CCCCCC"></iframe>'
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
        'id="above-middle-row-leaderboard-ad" style="background: #CCCCCC"></iframe>'
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
        'id="below-middle-row-large-leaderboard-ad" style="background: #CCCCCC"></iframe>'
BELOW_MIDDLE_ROW_LARGE_LEADERBOARD_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Below Middle Row Ad - Large Leaderboard -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:inline-block;width:970px;height:90px" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="7220420844"></ins> ' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

BOTTOM_ROW_LARGE_LEADERBOARD_IFRAME = \
    '<iframe width="970" height="90" allowtransparency="true" ' \
        'id="bottom-row-large-leaderboard-ad" style="background: #CCCCCC"></iframe>'
BOTTOM_ROW_LARGE_LEADERBOARD_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Bottom Row Ad - Large Leaderboard -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:inline-block;width:970px;height:90px" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="9879509240"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

# #############################################################################
#
# MIDDLE_*_RESPONSIVE_ADs: for the image page
# -------------------------------------------
#
MIDDLE_LEFT_RESPONSIVE_IFRAME = \
    '<iframe width="147" height="548" allowtransparency="true" ' \
        'id="middle-left-responsive-ad" style="background: #CCCCCC"></iframe>'
MIDDLE_LEFT_RESPONSIVE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Middle Left Ad - Responsive -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:block" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="5324885242" ' \
        'data-ad-format="auto"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

MIDDLE_RIGHT_RESPONSIVE_IFRAME = \
    '<iframe width="147" height="548" allowtransparency="true" ' \
        'id="middle-right-responsive-ad" style="background: #CCCCCC"></iframe>'
MIDDLE_RIGHT_RESPONSIVE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Middle Right Ad - Responsive -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:block" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="2092217240" ' \
        'data-ad-format="auto"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

# #############################################################################
#
# MIDDLE_CONTENT_*_ADs: for the galleries -> gallery page, and ???
# ----------------------------------------------------------------
# Because that page is built using a for loop to create multiple columns,
#    we couldn't get the ads to work on the sides the way we wanted to.
# (NOT saying that is impossible, just that we decided to try something new.)
# So we are going to try mixing rectangular ads in with the grojas!
# Notes:
#   We are setting up a few different sizes, to see how they look
#   We may not actually get code for and use all these sizes right away...
#
MIDDLE_CONTENT_RESPONSIVE_IFRAME = \
    '<iframe width="320" height="320" allowtransparency="true" ' \
        'id="gallery-page-responsive-ad" style="background: #CCCCCC">' \
    '</iframe>'
MIDDLE_CONTENT_RESPONSIVE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Middle Content Ad - Responsive -->' \
    '<ins class="adsbygoogle" ' \
         'style="display:block" ' \
         'data-ad-client="ca-pub-2594011034406643" ' \
         'data-ad-slot="4092047248" ' \
         'data-ad-format="auto"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

MIDDLE_CONTENT_LARGE_RECTANGLE_IFRAME = \
    '<iframe width="320" height="320" allowtransparency="true" ' \
        'id="gallery-page-large-rectangle-ad" style="background: #CCCCCC">' \
    '</iframe>'
MIDDLE_CONTENT_LARGE_RECTANGLE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Middle Content Ad - Large Rectangle -->' \
    '<ins class="adsbygoogle" ' \
         'style="display:inline-block;width:336px;height:280px" ' \
         'data-ad-client="ca-pub-2594011034406643" ' \
         'data-ad-slot="9998980048"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

MIDDLE_CONTENT_MEDIUM_RECTANGLE_IFRAME = \
    '<iframe width="300" height="250" allowtransparency="true" ' \
        'id="gallery-page-medium-rectangle-ad" style="background: #CCCCCC">' \
    '</iframe>'
MIDDLE_CONTENT_MEDIUM_RECTANGLE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Middle Content Ad - Medium Rectangle -->' \
    '<ins class="adsbygoogle" ' \
         'style="display:inline-block;width:300px;height:250px" ' \
         'data-ad-client="ca-pub-2594011034406643" ' \
         'data-ad-slot="6626711244"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

MIDDLE_CONTENT_SQUARE_IFRAME = \
    '<iframe width="250" height="250" allowtransparency="true" ' \
        'id="gallery-page-square-ad" style="background: #CCCCCC">' \
    '</iframe>'
MIDDLE_CONTENT_SQUARE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Middle Content Ad - Square -->' \
    '<ins class="adsbygoogle" ' \
         'style="display:inline-block;width:250px;height:250px" ' \
         'data-ad-client="ca-pub-2594011034406643" ' \
         'data-ad-slot="9580177644"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

MIDDLE_CONTENT_SMALL_SQUARE_IFRAME = \
    '<iframe width="200" height="200" allowtransparency="true" ' \
        'id="gallery-page-small-square-ad" style="background: #CCCCCC">' \
    '</iframe>'
MIDDLE_CONTENT_SMALL_SQUARE_AD = \
    '<script async ' \
    'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Middle Content Ad - Small Square -->' \
    '<ins class="adsbygoogle" ' \
         'style="display:inline-block;width:200px;height:200px" ' \
         'data-ad-client="ca-pub-2594011034406643" ' \
         'data-ad-slot="3533644042"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

# #############################################################################
#
# BOTTOM_*_RESPONSIVE_ADs: for the quiz pages, on either side of the disclaimer
# When I see these ads, they appear to be tall and narrow, hence the given
#   width and height, even though they are the same "size" (responsive)
#   as ads we use above these, in the aside.  Interesting.
#
BOTTOM_LEFT_RESPONSIVE_IFRAME = \
    '<iframe width="147" height="548" allowtransparency="true" ' \
        'id="bottom-left-responsive-ad" style="background: #CCCCCC"></iframe>'
BOTTOM_LEFT_RESPONSIVE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Bottom Left Ad - Responsive -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:block" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="2216641649" ' \
        'data-ad-format="auto"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

BOTTOM_RIGHT_RESPONSIVE_IFRAME = \
    '<iframe width="147" height="548" allowtransparency="true" ' \
        'id="bottom-right-responsive-ad" style="background: #CCCCCC"></iframe>'
BOTTOM_RIGHT_RESPONSIVE_AD = \
    '<script async ' \
        'src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">' \
    '</script>' \
    '<!-- Bottom Right Ad - Responsive -->' \
    '<ins class="adsbygoogle" ' \
        'style="display:block" ' \
        'data-ad-client="ca-pub-2594011034406643" ' \
        'data-ad-slot="5030507249" ' \
        'data-ad-format="auto"></ins>' \
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});' \
    '</script>'

# #############################################################################
# #############################################################################
#
# Define the adsense_ads dictionary
# ---------------------------------
# Define the dictionary that contains the ad code, and
# populate it appropriately, based on whether we are running locally
#
adsense_ads = {}

if RUNNING_LOCALLY:
    adsense_ads = {
        "top_row_large_billboard_ad":
            TOP_ROW_LARGE_BILLBOARD_IFRAME,
        "top_row_large_leaderboard_ad":
            TOP_ROW_LARGE_LEADERBOARD_IFRAME,
        "top_left_ad":
            TOP_LEFT_RESPONSIVE_IFRAME,
        "top_aside_top_ad":
            TOP_ASIDE_TOP_LARGE_MOBILE_BANNER_IFRAME,
        "top_aside_top_responsive_ad":
            TOP_ASIDE_TOP_RESPONSIVE_IFRAME,
        "top_aside_bottom_ad":
            TOP_ASIDE_BOTTOM_RESPONSIVE_LINKS_IFRAME,
        "top_aside_bottom_responsive_ad":
            TOP_ASIDE_BOTTOM_RESPONSIVE_IFRAME,
        "above_middle_row_ad":
            ABOVE_MIDDLE_ROW_LARGE_LEADERBOARD_IFRAME,
        "middle_left_ad":
            MIDDLE_LEFT_RESPONSIVE_IFRAME,
        "middle_content_responsive_ad":
            MIDDLE_CONTENT_RESPONSIVE_IFRAME,
        "middle_content_large_rectangle_ad":
            MIDDLE_CONTENT_LARGE_RECTANGLE_IFRAME,
        "middle_content_medium_rectangle_ad":
            MIDDLE_CONTENT_MEDIUM_RECTANGLE_IFRAME,
        "middle_content_square_ad":
            MIDDLE_CONTENT_SQUARE_IFRAME,
        "middle_content_small_square_ad":
            MIDDLE_CONTENT_SMALL_SQUARE_IFRAME,
        "middle_right_ad":
            MIDDLE_RIGHT_RESPONSIVE_IFRAME,
        "below_middle_row_ad":
            BELOW_MIDDLE_ROW_LARGE_LEADERBOARD_IFRAME,
        "bottom_left_ad":
            BOTTOM_LEFT_RESPONSIVE_IFRAME,
        "bottom_right_ad":
            BOTTOM_RIGHT_RESPONSIVE_IFRAME,
        "bottom_row_ad":
            BOTTOM_ROW_LARGE_LEADERBOARD_IFRAME,
    }
else:
    adsense_ads = {
        "top_row_large_billboard_ad":
            TOP_ROW_LARGE_BILLBOARD_AD,
        "top_row_large_leaderboard_ad":
            TOP_ROW_LARGE_LEADERBOARD_AD,
        "top_left_ad":
            TOP_LEFT_RESPONSIVE_AD,
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
            MIDDLE_LEFT_RESPONSIVE_AD,
        "middle_content_responsive_ad":
            MIDDLE_CONTENT_RESPONSIVE_AD,
        "middle_content_large_rectangle_ad":
            MIDDLE_CONTENT_LARGE_RECTANGLE_AD,
        "middle_content_medium_rectangle_ad":
            MIDDLE_CONTENT_MEDIUM_RECTANGLE_AD,
        "middle_content_square_ad":
            MIDDLE_CONTENT_SQUARE_AD,
        "middle_content_small_square_ad":
            MIDDLE_CONTENT_SMALL_SQUARE_AD,
        "middle_right_ad":
            MIDDLE_RIGHT_RESPONSIVE_AD,
        "below_middle_row_ad":
            BELOW_MIDDLE_ROW_LARGE_LEADERBOARD_AD,
        "bottom_left_ad":
            BOTTOM_LEFT_RESPONSIVE_AD,
        "bottom_right_ad":
            BOTTOM_RIGHT_RESPONSIVE_AD,
        "bottom_row_ad":
            BOTTOM_ROW_LARGE_LEADERBOARD_AD,
    }

