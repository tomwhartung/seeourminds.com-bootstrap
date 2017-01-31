/**
 * ****************************************
 *  Data and functions used by the gallery
 * ****************************************
 *
 * We could keep this in the global js directory, but
 *   I think it's fine keeping it here, at least for now.
 *
 * That is, I do not forsee other pages using any of this, but
 *   if it turns out to be useful to one or more of them,
 *     by all means move it to the global js dir.
 *
 */

gallery = {};

/**
 ************************************
 * Gallery data
 ************************************
 */
gallery.name = {
   'sixteen_types':
      "Sixteen Types",
   'friends':
      "Friends and Family",
   'tv_shows':
      "TV Shows",
   'politicians':
      "Politicians"
}

gallery.description = {
   'sixteen_types':
      "This gallery contains images of ... Sixteen Types ... and so on.",
   'friends':
      "This gallery contains images of ... Friends and Family ... and so on.",
   'tv_shows':
      "This gallery contains images of ... TV Shows ... and so on.",
   'politicians':
      "This gallery contains images of ... Politicians ... and so on."
}

/**
 ************************************
 * Gallery functions
 ************************************
 */

/**
 * All we want is a simple way to get the
 * value of the "gallery" query variable so we know which gallery to display.
 *
 * This method, which is just one of many found (there are several on stack overflow),
 * is quite simple (many use regexes).  Yay for that!
 * Yet it is also quite  possibly fairly inefficient - especially if we are looking for
 * the values of multiple query variables.
 *
 * If we need to do this in more than one place or for more than one query variable,
 * we should definitely move/merge this with a global JS file and probably look at
 * using a different method (e.g., one that processes all query variables, putting
 * them in an associative array, so we only have to do all that once).
 *
 * Reference:
 *    https://css-tricks.com/snippets/javascript/get-url-variables/
 */
gallery.getQueryVariable = function (variable) {
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
}

/**
 * Callback from getJSON call that processes the JSON we get
 */
gallery.populateGallery = function( image_json ) {
   //
   // (1) Compile the handlebars template
   // (2) Add the full path to the image to the image data
   // (3) After every "columns" images, set "add_row_separator" to a truesy value and add it to the image data
   // (4) Give the handlebars template the resultant image data to get the html
   // (5) Add the html to the document in the appropriate place
   //
   var full_path_to_image;
   var num_columns = 4;
   var handlebars_html = $("#gallery-image-template").html();
   var handlebars_template = Handlebars.compile( handlebars_html );                   // (1)
   for( var data_sub = 0; data_sub < image_json.image_list.length; data_sub++ ) {
      image_json.image_list[data_sub].full_path_to_image = gallery.path_to_images +   // (2)
         image_json.image_list[data_sub].image_file_name;
      if( (data_sub % num_columns) == 0 && data_sub != 0 ) {
         image_json.image_list[data_sub].add_row_separator = true;                    // (3)
      } else {
         image_json.image_list[data_sub].add_row_separator = false;
      }
   }
   var gallery_html = handlebars_template( image_json );    // (4)
   $('#all-gallery-images').html( gallery_html );           // (5)
}

/**
 ********************************************
 * Code to assemble the data needed and
 * call the functions in the proper sequence
 ********************************************
 *
 * (1) Get the name of the gallery to show from the query variable (in the url)
 * (2) Get the corresponding json file containing the data for the gallery to show,
 *     setting a callback function to populate the gallery with each image and its data.
 */
gallery.gallery_to_show = gallery.getQueryVariable( 'gallery' );      // (1)

gallery.json_file_name = 'json/' + gallery.gallery_to_show + '.json';
gallery.path_to_images = '../../images/galleries/' + gallery.gallery_to_show + '/';

$.getJSON( gallery.json_file_name, gallery.populateGallery );         // (2)


