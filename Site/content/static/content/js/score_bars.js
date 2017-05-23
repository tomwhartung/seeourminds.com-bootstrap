/**
 * score_bars.js: using score json to create horizontal d3 bars
 * ------------------------------------------------------------
 * Derived with much effort (this is my first experience with svg and d3)
 *   from bullet.js , found in the d3 gallery.
 * For a bunch more information, see the 25-d3_tutorials_to_score_bars
 *   project in my always_learning_python repo (first link in References).
 * References:
 *   https://github.com/tomwhartung/always_learning_python
 *   https://github.com/d3/d3/wiki/Gallery
 *   https://bl.ocks.org/mbostock/4061961
 */
(function() {
  d3.score_bars = function() {
    var reverse = false;
    var get_score_pct_fcn = get_score_pct;
    var get_function_letter_fcn = get_function_letter;
    var css_class = "x-score";  // default value; to override, call css_class()
    var width = 300;            // default value; to override, call width()
    var height = 40;            // default value; to override, call height()
    var tick_format = null;
    /**
     * Function to process each of the SVGGElements in the list
     */
    function score_bars(svgg_elt_list) {
      svgg_elt_list.each(function(data, index) {
        var score_value = get_score_pct_fcn.call(this, data, index);
        var function_letter = get_function_letter_fcn.call(this, data, index);
        var this_svgg_elt = d3.select(this);
        var score_value_arr = []
        score_value_arr = []              // data() fcn expects an array
        score_value_arr.push(score_value);

        // console.log('d3.score - score_bars - check check 123 123');
        // console.log('d3.score - score_bars - width x height: ' + width + ' x ' + height)

        var x_scale = d3.scaleLinear()
          .domain([0, 100])
          .range(reverse ? [width, 0] : [0, width]);

        var score_pct_lines = this_svgg_elt.selectAll("line.score-pct")
          .data(score_value_arr);
        //
        // Add the narrow base line for each bar
        //
        score_pct_lines.enter().append("line")
          .attr("class", "score-pct")
          .attr("x1", 0)
          .attr("x2", width)
          .attr("y1", height)
          .attr("y2", height);
        //
        // Add the rectangle representing the score for this personality function
        //
        score_pct_lines.enter().append("rect")
          .attr("class", set_css_class(function_letter))
          .attr("x", 0)
          .attr("y", height / 3)
          .attr("width", x_scale)
          .attr("height", height * 2 / 3);
        //
        // Use the desired tick format or the default.  I am not sure what the
        //   "8" is for! It was in the original code so I am respecting that.
        // Changing the value doesn't do much unless it gets over like 1000.
        // Reference - about 2/3 the way down on this page:
        //   https://github.com/d3/d3-3.x-api-reference/blob/master/SVG-Axes.md
        //
        var format = tick_format || x_scale.tickFormat(8);
        //
        // Update the tick groups.
        //
        var tick = this_svgg_elt.selectAll("g.tick")
          .data(x_scale.ticks(8), function(data) {
            return this.textContent || format(data);
          });

        //
        // Add the tick marks and the text that appears beneath them
        //
        var tick_enter = tick.enter().append("g")
          .attr("class", "tick")
          .attr("transform", score_bar_translate(x_scale))
          .style("opacity", 1);
        //
        // Add the actual tick marks
        //
        tick_enter.append("line")
          .attr("y1", height * 1 / 3)
          .attr("y2", height * 4 / 3);
        //
        // Add the label that appears under each tick mark
        //
        tick_enter.append("text")
          .attr("text-anchor", "right")  // anchor it on the right, then
          .attr("dx", "-.5em")           // move it a little to the left
          .attr("dy", "1em")
          .attr("y", height * 7 / 6)
          .text(format);

      });
      // d3.timer.flush();
    }

    /**
     * Set (override default) or get current css_class
     */
    score_bars.css_class = function(new_class) {
      if (!arguments.length) {
        return css_class;
      }
      css_class = new_class;
      return score_bars;
    };

    /**
     * Set (override default) or get current width
     */
    score_bars.width = function(new_width) {
      if (!arguments.length) {
        return width;
      }
      width = new_width;
      return score_bars;
    };

    /**
     * Set (override default) or get current height
     */
    score_bars.height = function(new_height) {
      if (!arguments.length) {
        return height;
      }
      height = new_height;
      return score_bars;
    };

    /**
     * Set (override default) or get current tick format
     */
    score_bars.tick_format = function(new_tick_format) {
      if (!arguments.length) {
        return tick_format;
      }
      tick_format = new_tick_format;
      return score_bars;
    };

    return score_bars;
  };
  /*
   * Returns the value for score_pct from the data
   */
  function get_score_pct(data, index) {
    return data.score_pct;
  }
  /*
   * Returns the value for the function_letter from the data
   */
  function get_function_letter(data, index) {
    return data.function_letter;
  }
  /*
   * Return a function that returns a translate string so that the
   * numbers on the axis are not all squished together on the left.
   */
  function score_bar_translate(x_scale) {
    return function(data) {
      return "translate(" + x_scale(data) + ",0)";
    };
  }
  /**
   * Use the function_letter to set the css class (blue for "N" , etc.)
   */
  function set_css_class (function_letter) {
    /*
     * I am undecided about whether the J & P bars should be grey or should
     * reflect the color of the dominant function (e.g., red for Judging-Feeling)
     * I think the grey bars look better but having the colored bars conveys more information.
     * -> Use this variable to easily toggle whether the bar on the bottom is
     * grey or the same color as the dominant function.
     */
    // var grey_j_p_bars = false;
    var grey_j_p_bars = true;

    if (function_letter == 'N') {
      this.__perceiving_css_class__ = 'n-score'
      css_class = "n-score";
    }
    else if (function_letter == 'S') {
      this.__perceiving_css_class__ = 's-score'
      css_class = "s-score";
    }
    else if (function_letter == 'F') {
      this.__judging_css_class__ = 'f-score'
      css_class = "f-score";
    }
    else if (function_letter == 'T') {
      this.__judging_css_class__ = 't-score'
      css_class = "t-score";
    }
    else if (function_letter == 'P') {
      if (grey_j_p_bars) {
        css_class = "x-score";
      }
      else {
        css_class = this.__perceiving_css_class__;
      }
    }
    else if (function_letter == 'J') {
      if (grey_j_p_bars) {
        css_class = "x-score";
      }
      else {
        css_class = this.__judging_css_class__;
      }
    }
    else {
      css_class = "x-score";
    }
    return css_class;
  }
})();
/**
 * score_bars namespace:
 * ---------------------
 * Keep our utility functions from interfering with other js code
 */
var score_bars = {
  /**
   * Use the data in "score" to create the SVG score bars chart in the
   * location specified by the parameters in "positioning" .
   */
  create_chart_svg: function(positioning, score) {
    var selector = positioning.selector;
    var total_width = positioning.total_width;
    var total_height = positioning.total_height;
    var margin_top = positioning.margin_top;
    var margin_right = positioning.margin_right;
    var margin_bottom = positioning.margin_bottom;
    var margin_left = positioning.margin_left;

    var bar_width = total_width - margin_left - margin_right;
    var bar_height = total_height - margin_top - margin_bottom;
    var tick_format_fcn = null;

    if (bar_width < 0) {
      console.log('score_bars.create_chart_svg: invalid bar_width (' +
        bar_width +'), setting it to 0 to prevent an error');
      bar_width = 0;
    }
    if (bar_height < 0) {
      console.log('score_bars.create_chart_svg: invalid bar_height (' +
        bar_height +'), setting it to 0 to prevent an error');
      bar_height = 0;
    }

    if (total_width < 275) {
      tick_format_fcn = function(tick_data) {return "";}
    }
    else if (total_width < 360) {
      tick_format_fcn = function(tick_data) {return tick_data;}
    }
    else {
      tick_format_fcn = function(tick_data) {return tick_data + "%";}
    }

    // console.log('create_chart_svg - selector: ' + selector);
    // console.log('create_chart_svg - total_width x total_height: ' + total_width + ' x ' + total_height);
    // console.log('create_chart_svg - bar_width x bar_height: ' + bar_width + ' x ' + bar_height);
    //
    // Convert the score to the data we need for the chart
    // Create the chart
    //
    var score_bars_data = score_bars.score_to_bars_data(score);
    var score_bars_chart = d3.score_bars()
      .tick_format(tick_format_fcn)
      .width(bar_width)
      .height(bar_height);
    //
    // Create the svg chart elements, setting attributes as appropriate
    //
    var score_bars_svg = d3.select(selector).selectAll("svg")
      .data(score_bars_data)
      .enter().append("svg")
      .attr("class", "score-bar")
      .attr("width", bar_width + margin_left + margin_right)
      .attr("height", bar_height + margin_top + margin_bottom)
      .append("g")
      .attr("transform", "translate(" + margin_left + "," + margin_top + ")")
      .call(score_bars_chart);
    //
    // Add the "g" elements for the score bar labels
    // Add the personality function letter and name to the chart
    //
    var function_letter_elt = score_bars_svg.append("g")
      .style("text-anchor", "end")
      .attr("transform", "translate(-6," + bar_height / 2 + ")");

    function_letter_elt.append("text")
      .attr("class", "function-letter")
      .text(function(data) { return data.function_letter; });
    //
    // Add the text "Extraversion," "Thinking," etc. only if there's enough room
    //
    if (margin_left > 50) {
      function_letter_elt.append("text")
        .attr("class", "function-name")
        .attr("dy", "1em")
        .text(function(data) { return data.function_name; });
    }

  },
  /**
   * Translate the "score" object found in the json file to the
   * format we need to draw the score_bars chart.
   * This function uses a fairly brute-force approach, so the code should be
   * easy to understand.
   */
  score_to_bars_data: function (score) {
    //
    // Values stored in the passed-in score object:
    //
    var score_value;
    var e_score_value;
    var i_score_value;
    var n_score_value;
    var s_score_value;
    var f_score_value;
    var t_score_value;
    var j_score_value;
    var p_score_value;
    //
    // Intermediate values derived from values in the passed-in score object:
    //
    var e_or_i_letter;
    var n_or_s_letter;
    var f_or_t_letter;
    var j_or_p_letter;
    var e_or_i_name;
    var n_or_s_name;
    var f_or_t_name;
    var e_i_total;
    var n_s_total;
    var f_t_total;
    var j_p_total;
    var e_or_i_score_pct;
    var n_or_s_score_pct;
    var f_or_t_score_pct;
    var j_or_p_score_pct;
    //
    // Values pushed onto the array that this function returns:
    //
    var e_or_i_entry;
    var n_or_s_entry;
    var f_or_t_entry;
    var j_or_p_entry;
    var score_bars_data = [];

    //
    // Find and save the values in the passed-in score object
    //
    for (var index in score ) {
      pair = score[index];
      for (var x_score_key in pair) {
        score_value = pair[x_score_key];
        if (x_score_key == 'e_score') { e_score_value = parseInt(score_value); }
        else if (x_score_key == 'i_score') { i_score_value = parseInt(score_value); }
        else if (x_score_key == 'n_score') { n_score_value = parseInt(score_value); }
        else if (x_score_key == 's_score') { s_score_value = parseInt(score_value); }
        else if (x_score_key == 'f_score') { f_score_value = parseInt(score_value); }
        else if (x_score_key == 't_score') { t_score_value = parseInt(score_value); }
        else if (x_score_key == 'j_score') { j_score_value = parseInt(score_value); }
        else if (x_score_key == 'p_score') { p_score_value = parseInt(score_value); }
      }
    }
    //
    // All values are required!
    // If any of them are missing, return an array containing a 0 score
    //
    if ( isNaN(e_score_value) || isNaN(i_score_value) ||
         isNaN(n_score_value) || isNaN(s_score_value) ||
         isNaN(f_score_value) || isNaN(t_score_value) ||
         isNaN(j_score_value) || isNaN(p_score_value)   ) {
      var letter_x = "X";
      var incomplete = "(Score Incomplete)";
      e_or_i_entry = {
        "function_letter": letter_x,"function_name": incomplete, "score_pct": 0
      };
      n_or_s_entry = {
        "function_letter": letter_x, "function_name": incomplete, "score_pct": 0
      };
      f_or_t_entry = {
        "function_letter": letter_x, "function_name": incomplete, "score_pct": 0
      };
      j_or_p_entry = {
        "function_letter": letter_x, "function_name": incomplete, "score_pct": 0
      };

      score_bars_data.push(e_or_i_entry);
      score_bars_data.push(n_or_s_entry);
      score_bars_data.push(f_or_t_entry);
      score_bars_data.push(j_or_p_entry);
      return score_bars_data;
    }
    //
    // Determine the letters and names, and calculate the percents needed
    //
    e_i_total = e_score_value + i_score_value;
    n_s_total = n_score_value + s_score_value;
    f_t_total = f_score_value + t_score_value;
    j_p_total = j_score_value + p_score_value;

    if (e_score_value > i_score_value) {
      e_or_i_letter = 'E';
      e_or_i_name = 'Extraversion';
      e_or_i_score_pct = Math.round(100 * e_score_value / e_i_total);
    }
    else {
      e_or_i_letter = 'I';
      e_or_i_name = 'Introversion';
      e_or_i_score_pct = Math.round(100 * i_score_value / e_i_total);
    }

    if (n_score_value > s_score_value) {
      n_or_s_letter = 'N';
      n_or_s_name = 'iNtuition';
      n_or_s_score_pct = Math.round(100 * n_score_value / n_s_total);
    }
    else {
      n_or_s_letter = 'S';
      n_or_s_name = 'Sensing';
      n_or_s_score_pct = Math.round(100 * s_score_value / n_s_total);
    }

    if (f_score_value > t_score_value) {
      f_or_t_letter = 'F';
      f_or_t_name = 'Feeling';
      f_or_t_score_pct = Math.round(100 * f_score_value / f_t_total);
    }
    else {
      f_or_t_letter = 'T';
      f_or_t_name = 'Thinking';
      f_or_t_score_pct = Math.round(100 * t_score_value / f_t_total);
    }

    if (j_score_value > p_score_value) {
      j_or_p_letter = 'J';
      j_or_p_name = 'Judging';
      j_or_p_score_pct = Math.round(100 * j_score_value / j_p_total);
    }
    else {
      j_or_p_letter = 'P';
      j_or_p_name = 'Perceiving';
      j_or_p_score_pct = Math.round(100 * p_score_value / j_p_total);
    }

    //
    // Use these values to construct the score_bars_data array
    //
    e_or_i_entry = {
      "function_letter": e_or_i_letter,
      "function_name": e_or_i_name,
      "score_pct": e_or_i_score_pct
    };
    n_or_s_entry = {
      "function_letter": n_or_s_letter,
      "function_name": n_or_s_name,
      "score_pct": n_or_s_score_pct
    };
    f_or_t_entry = {
      "function_letter": f_or_t_letter,
      "function_name": f_or_t_name,
      "score_pct": f_or_t_score_pct
    };
    j_or_p_entry = {
      "function_letter": j_or_p_letter,
      "function_name": j_or_p_name,
      "score_pct": j_or_p_score_pct
    };

    score_bars_data.push(e_or_i_entry);
    score_bars_data.push(n_or_s_entry);
    score_bars_data.push(f_or_t_entry);
    score_bars_data.push(j_or_p_entry);

    return score_bars_data;
  }
}
