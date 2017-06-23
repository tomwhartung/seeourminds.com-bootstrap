/*
 * Code for general use on seeourminds.com
 */
var seeourminds = {};

/**
 * Set the name of the transition effect desired
 * for each four letter type, to add some variety
 * Note: the "pulsate" effect is a bit annoying.
 */
seeourminds.effect_for_type = {
  'ENFJ': 'shake',
  'ENFP': 'bounce',
  'ENTJ': 'explode',
  'ENTP': 'drop',
  'ESFJ': 'puff',
  'ESFP': 'explode',
  'ESTJ': 'shake',
  'ESTP': 'highlight',
  'INFJ': 'blind',
  'INFP': 'fold',
  'INTJ': 'scale',
  'INTP': 'fade',
  'ISFJ': 'size',
  'ISFP': 'slide',
  'ISTJ': 'highlight',
  'ISTP': 'clip',
}

/**
 * Set the name of the color corresponding to the
 * dominant function for each four letter type
 */
seeourminds.color_name_for_dom = {
  'ENFJ': 'Red',
  'ENFP': 'Blue',
  'ENTJ': 'Green',
  'ENTP': 'Blue',
  'ESFJ': 'Red',
  'ESFP': 'Yellow',
  'ESTJ': 'Green',
  'ESTP': 'Yellow',
  'INFJ': 'Blue',
  'INFP': 'Red',
  'INTJ': 'Blue',
  'INTP': 'Green',
  'ISFJ': 'Yellow',
  'ISFP': 'Red',
  'ISTJ': 'Yellow',
  'ISTP': 'Green',
}

/**
 * Set the name of the color corresponding to the
 * auxiliary function for each four letter type
 */
seeourminds.color_name_for_aux = {
  'ENFJ': 'Blue',
  'ENFP': 'Red',
  'ENTJ': 'Blue',
  'ENTP': 'Green',
  'ESFJ': 'Yellow',
  'ESFP': 'Red',
  'ESTJ': 'Yellow',
  'ESTP': 'Green',
  'INFJ': 'Red',
  'INFP': 'Blue',
  'INTJ': 'Green',
  'INTP': 'Blue',
  'ISFJ': 'Red',
  'ISFP': 'Yellow',
  'ISTJ': 'Green',
  'ISTP': 'Yellow',
}

/**
 * Set the bootstrap class for the color corresponding to the
 * dominant function for each four letter type
 */
seeourminds.bootstrap_class_for_dom = {
  'ENFJ': 'som-btn-red',
  'ENFP': 'som-btn-blue',
  'ENTJ': 'som-btn-green',
  'ENTP': 'som-btn-blue',
  'ESFJ': 'som-btn-red',
  'ESFP': 'som-btn-yellow',
  'ESTJ': 'som-btn-green',
  'ESTP': 'som-btn-yellow',
  'INFJ': 'som-btn-blue',
  'INFP': 'som-btn-red',
  'INTJ': 'som-btn-blue',
  'INTP': 'som-btn-green',
  'ISFJ': 'som-btn-yellow',
  'ISFP': 'som-btn-red',
  'ISTJ': 'som-btn-yellow',
  'ISTP': 'som-btn-green',
}

/**
 * Set the bootstrap class for the color corresponding to the
 * auxiliary function for each four letter type
 */
seeourminds.bootstrap_class_for_aux = {
  'ENFJ': 'som-btn-blue',
  'ENFP': 'som-btn-red',
  'ENTJ': 'som-btn-blue',
  'ENTP': 'som-btn-green',
  'ESFJ': 'som-btn-yellow',
  'ESFP': 'som-btn-red',
  'ESTJ': 'som-btn-yellow',
  'ESTP': 'som-btn-green',
  'INFJ': 'som-btn-red',
  'INFP': 'som-btn-blue',
  'INTJ': 'som-btn-green',
  'INTP': 'som-btn-blue',
  'ISFJ': 'som-btn-red',
  'ISFP': 'som-btn-yellow',
  'ISTJ': 'som-btn-green',
  'ISTP': 'som-btn-yellow',
}
