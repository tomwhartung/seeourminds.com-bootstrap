
# README.md

This file contains very important information!

# Template

There is a template for new gallery json files "next door" in:

- ../templates/9999-gallery_template.json

# External References

Following is a list of external references to gallery pages.

Note that **IF WE CHANGE THE NAME OF A JSON FILE OR THE ID OF AN IMAGE OF ONE OF THESE FILES**
then we will **NEED TO UPDATE THE LINK IN ANY POSTS THAT REFER TO THE IMAGE!!**

## Medium.com/@seeourminds

Article "The Good..." contains a link to the image:
- Dana Scully: /image/2700-fictional-tv-x_files/2720/

Article "...The Bad..." contains a link to the image:
- Woody Allen: /image/0500-real-famous/0500/

Article "...And The Ugly" contains a link to the image:
- Padme Amidala: /image/1200-fictional-movies-star_wars-prequel/1200/

## Medium.com/@tomwhartung

Article "The New Art - The New Life: 100 Years Later" contains a link to the gallery:
- Mondrianesque Compositions: https://www.seeourminds.com/gallery/9600-generic_images-experiments-mondrian/

# Bad Characters!

The characters listed below cause this ascii decode error:

- 'ascii' codec can't decode byte 0xe2 in position 16501: ordinal not in range(128)

**Note: this error occurs only when serving page in apache** - not when using local server!

## Cause

I believe these come from copy-and-pasting quotes found online.

## The Double-Fix

I am fixing **both** the characters and the source of the error, and advise you to do the same.

- Use grep to find and vi to remove the characters see the (partial) list below
- Programmatic fix - found at this url and verified to work with the bad characters:
- - https://stackoverflow.com/questions/42762556/how-to-interpret-this-error-unicodedecodeerror-ascii-codec-cant-decode-byte

## List of Bad Characters:

- –
- ’
- …
- —

## List of Commands to Find the Bad Characters:

```
grep '…' *
grep '–' *
grep '’' *
grep '—' *
```

Only this `README.md` file should show up as output from any of these commands.

