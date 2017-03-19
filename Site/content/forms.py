##
#  forms.py: forms used by the app
#     1. populate the quiz page and implement the questionnaire
#     2. ???
#
from django import forms
import json
import os

##
#  QuizForm: convert our json to a list of questions and multiple-choice answers
#
class QuizForm( forms.Form ):
   quiz_dictionary = []

   ##
   #  Read the quiz questions and answers from the json file
   #
   def read_quiz_json():
      site_content_dir = os.path.abspath(os.path.dirname(__file__))
      quiz_file_name = 'seeourminds_quiz.json'
      quiz_file_path = site_content_dir + '/static/content/json/quiz/' + quiz_file_name
      quiz_json_file = open( quiz_file_path )
      quiz_json_string = quiz_json_file.read()
      quiz_json_file.close()
      quiz_dictionary = json.loads( quiz_json_string )
      return( quiz_dictionary )

   ##
   #  Get and return the question_text (aka. "label") for the given question
   #
   def get_label( question_no, quiz_question ):
      ## print( 'get_label - question_no:', question_no )
      label = str(question_no) + '. ' + quiz_question['question_text']
      return label

   ##
   #  Get and return the answers that are populated in the json for the given question
   #
   def get_choices( quiz_question ):
      ## print( 'get_choices - quiz_question:', quiz_question )
      choices = []

      if len(quiz_question['answer_1_text']) > 0 and int(quiz_question['answer_1_weight']) > 0 :
         choice_1 = [ '1', quiz_question['answer_1_text'] ]
         choices.append( choice_1 )

      if len(quiz_question['answer_2_text']) > 0 and int(quiz_question['answer_2_weight']) > 0 :
         choice_2 = [ '2', quiz_question['answer_2_text'] ]
         choices.append( choice_2 )

      if len(quiz_question['answer_3_text']) > 0 and int(quiz_question['answer_3_weight']) > 0 :
         choice_3 = [ '3', quiz_question['answer_3_text'] ]
         choices.append( choice_3 )

      if len(quiz_question['answer_4_text']) > 0 and int(quiz_question['answer_4_weight']) > 0 :
         choice_4 = [ '4', quiz_question['answer_4_text'] ]
         choices.append( choice_4 )

      if len(quiz_question['answer_5_text']) > 0 and int(quiz_question['answer_5_weight']) > 0 :
         choice_5 = [ '5', quiz_question['answer_5_text'] ]
         choices.append( choice_5 )

      if len(quiz_question['answer_6_text']) > 0 and int(quiz_question['answer_6_weight']) > 0 :
         choice_6 = [ '6', quiz_question['answer_6_text'] ]
         choices.append( choice_6 )

      return choices

   name = forms.CharField( max_length=50 )
   email = forms.EmailField()
   quiz_dictionary = read_quiz_json()
   ## print( 'quiz_dictionary:', quiz_dictionary )
   print( 'len(quiz_dictionary):', len(quiz_dictionary) )
   ## print( 'quiz_dictionary[0]:', quiz_dictionary[0] )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_01 = get_label( 1, quiz_dictionary[0] )
   choices_01 = get_choices( quiz_dictionary[0] )
   question_01 = forms.ChoiceField( widget=radio_widget, label=label_01, choices=choices_01 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_02 = get_label( 2, quiz_dictionary[1] )
   choices_02 = get_choices( quiz_dictionary[1] )
   question_02 = forms.ChoiceField( widget=radio_widget, label=label_02, choices=choices_02 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_03 = get_label( 3, quiz_dictionary[2] )
   choices_03 = get_choices( quiz_dictionary[2] )
   question_03 = forms.ChoiceField( widget=radio_widget, label=label_03, choices=choices_03 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_04 = get_label( 4, quiz_dictionary[3] )
   choices_04 = get_choices( quiz_dictionary[3] )
   question_04 = forms.ChoiceField( widget=radio_widget, label=label_04, choices=choices_04 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_05 = get_label( 5, quiz_dictionary[4] )
   choices_05 = get_choices( quiz_dictionary[4] )
   question_05 = forms.ChoiceField( widget=radio_widget, label=label_05, choices=choices_05 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_06 = get_label( 6, quiz_dictionary[5] )
   choices_06 = get_choices( quiz_dictionary[5] )
   question_06 = forms.ChoiceField( widget=radio_widget, label=label_06, choices=choices_06 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_07 = get_label( 7, quiz_dictionary[6] )
   choices_07 = get_choices( quiz_dictionary[6] )
   question_07 = forms.ChoiceField( widget=radio_widget, label=label_07, choices=choices_07 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_08 = get_label( 8, quiz_dictionary[7] )
   choices_08 = get_choices( quiz_dictionary[7] )
   question_08 = forms.ChoiceField( widget=radio_widget, label=label_08, choices=choices_08 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_09 = get_label( 9, quiz_dictionary[8] )
   choices_09 = get_choices( quiz_dictionary[8] )
   question_09 = forms.ChoiceField( widget=radio_widget, label=label_09, choices=choices_09 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_10 = get_label( 10, quiz_dictionary[9] )
   choices_10 = get_choices( quiz_dictionary[9] )
   question_10 = forms.ChoiceField( widget=radio_widget, label=label_10, choices=choices_10 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_11 = get_label( 11, quiz_dictionary[10] )
   choices_11 = get_choices( quiz_dictionary[10] )
   question_11 = forms.ChoiceField( widget=radio_widget, label=label_11, choices=choices_11 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_12 = get_label( 12, quiz_dictionary[11] )
   choices_12 = get_choices( quiz_dictionary[11] )
   question_12 = forms.ChoiceField( widget=radio_widget, label=label_12, choices=choices_12 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_13 = get_label( 13, quiz_dictionary[12] )
   choices_13 = get_choices( quiz_dictionary[12] )
   question_13 = forms.ChoiceField( widget=radio_widget, label=label_13, choices=choices_13 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_14 = get_label( 14, quiz_dictionary[13] )
   choices_14 = get_choices( quiz_dictionary[13] )
   question_14 = forms.ChoiceField( widget=radio_widget, label=label_14, choices=choices_14 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_15 = get_label( 15, quiz_dictionary[14] )
   choices_15 = get_choices( quiz_dictionary[14] )
   question_15 = forms.ChoiceField( widget=radio_widget, label=label_15, choices=choices_15 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_16 = get_label( 16, quiz_dictionary[15] )
   choices_16 = get_choices( quiz_dictionary[15] )
   question_16 = forms.ChoiceField( widget=radio_widget, label=label_16, choices=choices_16 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_17 = get_label( 17, quiz_dictionary[16] )
   choices_17 = get_choices( quiz_dictionary[16] )
   question_17 = forms.ChoiceField( widget=radio_widget, label=label_17, choices=choices_17 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_18 = get_label( 18, quiz_dictionary[17] )
   choices_18 = get_choices( quiz_dictionary[17] )
   question_18 = forms.ChoiceField( widget=radio_widget, label=label_18, choices=choices_18 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_19 = get_label( 19, quiz_dictionary[18] )
   choices_19 = get_choices( quiz_dictionary[18] )
   question_19 = forms.ChoiceField( widget=radio_widget, label=label_19, choices=choices_19 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_20 = get_label( 20, quiz_dictionary[19] )
   choices_20 = get_choices( quiz_dictionary[19] )
   question_20 = forms.ChoiceField( widget=radio_widget, label=label_20, choices=choices_20 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_21 = get_label( 21, quiz_dictionary[20] )
   choices_21 = get_choices( quiz_dictionary[20] )
   question_21 = forms.ChoiceField( widget=radio_widget, label=label_21, choices=choices_21 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_22 = get_label( 22, quiz_dictionary[21] )
   choices_22 = get_choices( quiz_dictionary[21] )
   question_22 = forms.ChoiceField( widget=radio_widget, label=label_22, choices=choices_22 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_23 = get_label( 23, quiz_dictionary[22] )
   choices_23 = get_choices( quiz_dictionary[22] )
   question_23 = forms.ChoiceField( widget=radio_widget, label=label_23, choices=choices_23 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_24 = get_label( 24, quiz_dictionary[23] )
   choices_24 = get_choices( quiz_dictionary[23] )
   question_24 = forms.ChoiceField( widget=radio_widget, label=label_24, choices=choices_24 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_25 = get_label( 25, quiz_dictionary[24] )
   choices_25 = get_choices( quiz_dictionary[24] )
   question_25 = forms.ChoiceField( widget=radio_widget, label=label_25, choices=choices_25 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_26 = get_label( 26, quiz_dictionary[25] )
   choices_26 = get_choices( quiz_dictionary[25] )
   question_26 = forms.ChoiceField( widget=radio_widget, label=label_26, choices=choices_26 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_27 = get_label( 27, quiz_dictionary[26] )
   choices_27 = get_choices( quiz_dictionary[26] )
   question_27 = forms.ChoiceField( widget=radio_widget, label=label_27, choices=choices_27 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_28 = get_label( 28, quiz_dictionary[27] )
   choices_28 = get_choices( quiz_dictionary[27] )
   question_28 = forms.ChoiceField( widget=radio_widget, label=label_28, choices=choices_28 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_29 = get_label( 29, quiz_dictionary[28] )
   choices_29 = get_choices( quiz_dictionary[28] )
   question_29 = forms.ChoiceField( widget=radio_widget, label=label_29, choices=choices_29 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_30 = get_label( 30, quiz_dictionary[29] )
   choices_30 = get_choices( quiz_dictionary[29] )
   question_30 = forms.ChoiceField( widget=radio_widget, label=label_30, choices=choices_30 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_31 = get_label( 31, quiz_dictionary[30] )
   choices_31 = get_choices( quiz_dictionary[30] )
   question_31 = forms.ChoiceField( widget=radio_widget, label=label_31, choices=choices_31 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_32 = get_label( 32, quiz_dictionary[31] )
   choices_32 = get_choices( quiz_dictionary[31] )
   question_32 = forms.ChoiceField( widget=radio_widget, label=label_32, choices=choices_32 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_33 = get_label( 33, quiz_dictionary[32] )
   choices_33 = get_choices( quiz_dictionary[32] )
   question_33 = forms.ChoiceField( widget=radio_widget, label=label_33, choices=choices_33 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_34 = get_label( 34, quiz_dictionary[33] )
   choices_34 = get_choices( quiz_dictionary[33] )
   question_34 = forms.ChoiceField( widget=radio_widget, label=label_34, choices=choices_34 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_35 = get_label( 35, quiz_dictionary[34] )
   choices_35 = get_choices( quiz_dictionary[34] )
   question_35 = forms.ChoiceField( widget=radio_widget, label=label_35, choices=choices_35 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_36 = get_label( 36, quiz_dictionary[35] )
   choices_36 = get_choices( quiz_dictionary[35] )
   question_36 = forms.ChoiceField( widget=radio_widget, label=label_36, choices=choices_36 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_37 = get_label( 37, quiz_dictionary[36] )
   choices_37 = get_choices( quiz_dictionary[36] )
   question_37 = forms.ChoiceField( widget=radio_widget, label=label_37, choices=choices_37 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_38 = get_label( 38, quiz_dictionary[37] )
   choices_38 = get_choices( quiz_dictionary[37] )
   question_38 = forms.ChoiceField( widget=radio_widget, label=label_38, choices=choices_38 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_39 = get_label( 39, quiz_dictionary[38] )
   choices_39 = get_choices( quiz_dictionary[38] )
   question_39 = forms.ChoiceField( widget=radio_widget, label=label_39, choices=choices_39 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_40 = get_label( 40, quiz_dictionary[39] )
   choices_40 = get_choices( quiz_dictionary[39] )
   question_40 = forms.ChoiceField( widget=radio_widget, label=label_40, choices=choices_40 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_41 = get_label( 41, quiz_dictionary[40] )
   choices_41 = get_choices( quiz_dictionary[40] )
   question_41 = forms.ChoiceField( widget=radio_widget, label=label_41, choices=choices_41 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_42 = get_label( 42, quiz_dictionary[41] )
   choices_42 = get_choices( quiz_dictionary[41] )
   question_42 = forms.ChoiceField( widget=radio_widget, label=label_42, choices=choices_42 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_43 = get_label( 43, quiz_dictionary[42] )
   choices_43 = get_choices( quiz_dictionary[42] )
   question_43 = forms.ChoiceField( widget=radio_widget, label=label_43, choices=choices_43 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_44 = get_label( 44, quiz_dictionary[43] )
   choices_44 = get_choices( quiz_dictionary[43] )
   question_44 = forms.ChoiceField( widget=radio_widget, label=label_44, choices=choices_44 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_45 = get_label( 45, quiz_dictionary[44] )
   choices_45 = get_choices( quiz_dictionary[44] )
   question_45 = forms.ChoiceField( widget=radio_widget, label=label_45, choices=choices_45 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_46 = get_label( 46, quiz_dictionary[45] )
   choices_46 = get_choices( quiz_dictionary[45] )
   question_46 = forms.ChoiceField( widget=radio_widget, label=label_46, choices=choices_46 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_47 = get_label( 47, quiz_dictionary[46] )
   choices_47 = get_choices( quiz_dictionary[46] )
   question_47 = forms.ChoiceField( widget=radio_widget, label=label_47, choices=choices_47 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_48 = get_label( 48, quiz_dictionary[47] )
   choices_48 = get_choices( quiz_dictionary[47] )
   question_48 = forms.ChoiceField( widget=radio_widget, label=label_48, choices=choices_48 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_49 = get_label( 49, quiz_dictionary[48] )
   choices_49 = get_choices( quiz_dictionary[48] )
   question_49 = forms.ChoiceField( widget=radio_widget, label=label_49, choices=choices_49 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_50 = get_label( 50, quiz_dictionary[49] )
   choices_50 = get_choices( quiz_dictionary[49] )
   question_50 = forms.ChoiceField( widget=radio_widget, label=label_50, choices=choices_50 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_51 = get_label( 51, quiz_dictionary[50] )
   choices_51 = get_choices( quiz_dictionary[50] )
   question_51 = forms.ChoiceField( widget=radio_widget, label=label_51, choices=choices_51 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_52 = get_label( 52, quiz_dictionary[51] )
   choices_52 = get_choices( quiz_dictionary[51] )
   question_52 = forms.ChoiceField( widget=radio_widget, label=label_52, choices=choices_52 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_53 = get_label( 53, quiz_dictionary[52] )
   choices_53 = get_choices( quiz_dictionary[52] )
   question_53 = forms.ChoiceField( widget=radio_widget, label=label_53, choices=choices_53 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_54 = get_label( 54, quiz_dictionary[53] )
   choices_54 = get_choices( quiz_dictionary[53] )
   question_54 = forms.ChoiceField( widget=radio_widget, label=label_54, choices=choices_54 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_55 = get_label( 55, quiz_dictionary[54] )
   choices_55 = get_choices( quiz_dictionary[54] )
   question_55 = forms.ChoiceField( widget=radio_widget, label=label_55, choices=choices_55 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_56 = get_label( 56, quiz_dictionary[55] )
   choices_56 = get_choices( quiz_dictionary[55] )
   question_56 = forms.ChoiceField( widget=radio_widget, label=label_56, choices=choices_56 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_57 = get_label( 57, quiz_dictionary[56] )
   choices_57 = get_choices( quiz_dictionary[56] )
   question_57 = forms.ChoiceField( widget=radio_widget, label=label_57, choices=choices_57 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_58 = get_label( 58, quiz_dictionary[57] )
   choices_58 = get_choices( quiz_dictionary[57] )
   question_58 = forms.ChoiceField( widget=radio_widget, label=label_58, choices=choices_58 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_59 = get_label( 59, quiz_dictionary[58] )
   choices_59 = get_choices( quiz_dictionary[58] )
   question_59 = forms.ChoiceField( widget=radio_widget, label=label_59, choices=choices_59 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_60 = get_label( 60, quiz_dictionary[59] )
   choices_60 = get_choices( quiz_dictionary[59] )
   question_60 = forms.ChoiceField( widget=radio_widget, label=label_60, choices=choices_60 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_61 = get_label( 61, quiz_dictionary[60] )
   choices_61 = get_choices( quiz_dictionary[60] )
   question_61 = forms.ChoiceField( widget=radio_widget, label=label_61, choices=choices_61 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_62 = get_label( 62, quiz_dictionary[61] )
   choices_62 = get_choices( quiz_dictionary[61] )
   question_62 = forms.ChoiceField( widget=radio_widget, label=label_62, choices=choices_62 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_63 = get_label( 63, quiz_dictionary[62] )
   choices_63 = get_choices( quiz_dictionary[62] )
   question_63 = forms.ChoiceField( widget=radio_widget, label=label_63, choices=choices_63 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_64 = get_label( 64, quiz_dictionary[63] )
   choices_64 = get_choices( quiz_dictionary[63] )
   question_64 = forms.ChoiceField( widget=radio_widget, label=label_64, choices=choices_64 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_65 = get_label( 65, quiz_dictionary[64] )
   choices_65 = get_choices( quiz_dictionary[64] )
   question_65 = forms.ChoiceField( widget=radio_widget, label=label_65, choices=choices_65 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_66 = get_label( 66, quiz_dictionary[65] )
   choices_66 = get_choices( quiz_dictionary[65] )
   question_66 = forms.ChoiceField( widget=radio_widget, label=label_66, choices=choices_66 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_67 = get_label( 67, quiz_dictionary[66] )
   choices_67 = get_choices( quiz_dictionary[66] )
   question_67 = forms.ChoiceField( widget=radio_widget, label=label_67, choices=choices_67 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_68 = get_label( 68, quiz_dictionary[67] )
   choices_68 = get_choices( quiz_dictionary[67] )
   question_68 = forms.ChoiceField( widget=radio_widget, label=label_68, choices=choices_68 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_69 = get_label( 69, quiz_dictionary[68] )
   choices_69 = get_choices( quiz_dictionary[68] )
   question_69 = forms.ChoiceField( widget=radio_widget, label=label_69, choices=choices_69 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_70 = get_label( 70, quiz_dictionary[69] )
   choices_70 = get_choices( quiz_dictionary[69] )
   question_70 = forms.ChoiceField( widget=radio_widget, label=label_70, choices=choices_70 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_71 = get_label( 71, quiz_dictionary[70] )
   choices_71 = get_choices( quiz_dictionary[70] )
   question_71 = forms.ChoiceField( widget=radio_widget, label=label_71, choices=choices_71 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_72 = get_label( 72, quiz_dictionary[71] )
   choices_72 = get_choices( quiz_dictionary[71] )
   question_72 = forms.ChoiceField( widget=radio_widget, label=label_72, choices=choices_72 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_73 = get_label( 73, quiz_dictionary[72] )
   choices_73 = get_choices( quiz_dictionary[72] )
   question_73 = forms.ChoiceField( widget=radio_widget, label=label_73, choices=choices_73 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_74 = get_label( 74, quiz_dictionary[73] )
   choices_74 = get_choices( quiz_dictionary[73] )
   question_74 = forms.ChoiceField( widget=radio_widget, label=label_74, choices=choices_74 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_75 = get_label( 75, quiz_dictionary[74] )
   choices_75 = get_choices( quiz_dictionary[74] )
   question_75 = forms.ChoiceField( widget=radio_widget, label=label_75, choices=choices_75 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_76 = get_label( 76, quiz_dictionary[75] )
   choices_76 = get_choices( quiz_dictionary[75] )
   question_76 = forms.ChoiceField( widget=radio_widget, label=label_76, choices=choices_76 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_77 = get_label( 77, quiz_dictionary[76] )
   choices_77 = get_choices( quiz_dictionary[76] )
   question_77 = forms.ChoiceField( widget=radio_widget, label=label_77, choices=choices_77 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_78 = get_label( 78, quiz_dictionary[77] )
   choices_78 = get_choices( quiz_dictionary[77] )
   question_78 = forms.ChoiceField( widget=radio_widget, label=label_78, choices=choices_78 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_79 = get_label( 79, quiz_dictionary[78] )
   choices_79 = get_choices( quiz_dictionary[78] )
   question_79 = forms.ChoiceField( widget=radio_widget, label=label_79, choices=choices_79 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_80 = get_label( 80, quiz_dictionary[79] )
   choices_80 = get_choices( quiz_dictionary[79] )
   question_80 = forms.ChoiceField( widget=radio_widget, label=label_80, choices=choices_80 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_81 = get_label( 81, quiz_dictionary[80] )
   choices_81 = get_choices( quiz_dictionary[80] )
   question_81 = forms.ChoiceField( widget=radio_widget, label=label_81, choices=choices_81 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_82 = get_label( 82, quiz_dictionary[81] )
   choices_82 = get_choices( quiz_dictionary[81] )
   question_82 = forms.ChoiceField( widget=radio_widget, label=label_82, choices=choices_82 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_83 = get_label( 83, quiz_dictionary[82] )
   choices_83 = get_choices( quiz_dictionary[82] )
   question_83 = forms.ChoiceField( widget=radio_widget, label=label_83, choices=choices_83 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_84 = get_label( 84, quiz_dictionary[83] )
   choices_84 = get_choices( quiz_dictionary[83] )
   question_84 = forms.ChoiceField( widget=radio_widget, label=label_84, choices=choices_84 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_85 = get_label( 85, quiz_dictionary[84] )
   choices_85 = get_choices( quiz_dictionary[84] )
   question_85 = forms.ChoiceField( widget=radio_widget, label=label_85, choices=choices_85 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_86 = get_label( 86, quiz_dictionary[85] )
   choices_86 = get_choices( quiz_dictionary[85] )
   question_86 = forms.ChoiceField( widget=radio_widget, label=label_86, choices=choices_86 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_87 = get_label( 87, quiz_dictionary[86] )
   choices_87 = get_choices( quiz_dictionary[86] )
   question_87 = forms.ChoiceField( widget=radio_widget, label=label_87, choices=choices_87 )

   radio_widget = forms.RadioSelect(attrs={'class':'quiz_answer'})
   label_88 = get_label( 88, quiz_dictionary[87] )
   choices_88 = get_choices( quiz_dictionary[87] )
   question_88 = forms.ChoiceField( widget=radio_widget, label=label_88, choices=choices_88 )



