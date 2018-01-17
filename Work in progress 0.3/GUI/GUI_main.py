import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *
import webbrowser

from TesktTilGui import tekst, posisjoner

class Window(QtGui.QMainWindow):
    def __init__(self):
        #Starting the main window (QtGui.QMainWindow)
        super(Window, self).__init__()

        # Setting the geometry of the window
        # and moving it to a fixed area when started
        self.setGeometry(400, 200, 1200, 800)

        # Locking the size to (1200, 800)
        self.setFixedSize(posisjoner('Vindu_b'), posisjoner('Vindu_h'))

        # Setting the title of the window
        self.setWindowTitle("Preferansevalg")

        # Setting the GUI icon
        self.setWindowIcon(QtGui.QIcon('VT vest logo.png'))

        # Setting the style of the GUI.
        # Other alternatives: Plastique, Windows etc.
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("CleanLooks"))

        # Creating a exit function
        extract_action = QtGui.QAction("&Exit", self)

        # Setting a exit shortcut
        extract_action.setShortcut("Ctrl+Q")

        # Close the GUI if shortcut is used
        extract_action.triggered.connect(self.close_application)



        # Code for picture, can be used if needed
        """picture = QtGui.QPixmap("tf.jpg")
        picture_label = QtGui.QLabel(self)
        picture_label.setPixmap(picture)
        picture_label.setVisible(True)
        picture_label.move(400, 200)"""


        # Creating the menubar and adding a filemenu
        main_menu = self.menuBar()

        # Adding 'File' to the menu
        file_menu = main_menu.addMenu(tekst('Menu1'))

        # Connecting function to 'File'
        file_menu.addAction(extract_action)

        # Creating an 'Help' box
        open_help_box = QtGui.QAction(tekst('Menu2'), self)

        # Setting a shortcut for 'Help'
        open_help_box.setShortcut("Ctrl+H")

        # Open 'Help' window when shortcut is used
        open_help_box.triggered.connect(self.open_help)

        # Adding 'Help' to menu
        help_menu = main_menu.addMenu(tekst('Menu2'))

        # Connecting function to 'Help'
        help_menu.addAction(open_help_box)

        # Creating an 'About' box
        open_about_box = QtGui.QAction(tekst('Menu3'), self)

        # Setting a shortcut for 'About'
        open_about_box.setShortcut("Ctrl+E")

        # Open 'About' window when shortcut is used
        open_about_box.triggered.connect(self.open_about)

        # Adding 'About' to menu
        about_menu = main_menu.addMenu(tekst('Menu3'))

        # Connecting function to 'About'
        about_menu.addAction(open_about_box)

        # Starting the home function that creates buttons
        # texteditor, toolbar and progress bar
        self.home()

    def home(self):

        # Creating a textfield for output
        self.output_field = QtGui.QTextEdit(self)

        # Disabling the textfield for user input,
        # making it a read only
        self.output_field.setReadOnly(True)

        # Creating a font
        font = QtGui.QFont()

        # Setting the font size to 10
        font.setPointSize(10)

        # Adding the font size to the textedit field
        self.output_field.setFont(font)

        # Setting the intro text
        self.output_field.setText(tekst('1'))
        self.output_field.append('\n' + tekst('2'))

        # Moving the textfield
        self.output_field.move(posisjoner('Marg_b'), posisjoner('Marg_topp'))

        # Setting the textfield size
        self.output_field.resize(posisjoner('Vindu_b') - posisjoner('Marg_b') * 2,
                                 posisjoner('Vindu_h') - posisjoner('Marg_h') * 3 - posisjoner('Knapp_h') * 2
                                 - posisjoner('Marg_topp'))

        # Creating buttons
        self.btn_calculateBallot = QtGui.QPushButton(tekst('Button1'), self)
        self.btn_createExample = QtGui.QPushButton(tekst('Button2'), self)
        self.btn_FAQ = QtGui.QPushButton(tekst('Button3'), self)
        self.btn_doner = QtGui.QPushButton(tekst('Button4'), self)

        # Set fixed size to buttons
        self.btn_FAQ.setFixedSize(posisjoner('Knapp_b'), posisjoner('Knapp_h'))
        self.btn_createExample.setFixedSize(posisjoner('Knapp_b'), posisjoner('Knapp_h'))
        self.btn_calculateBallot.setFixedSize(posisjoner('Knapp_b'), posisjoner('Knapp_h'))
        self.btn_doner.setFixedSize(posisjoner('Knapp_b'), posisjoner('Knapp_h'))

        # Move buttons
        self.btn_calculateBallot.move(posisjoner('Marg_b'),
                                      (posisjoner('Vindu_h') - posisjoner('Marg_h') * 2 - posisjoner('Knapp_h') * 2))
        self.btn_FAQ.move((posisjoner('Marg_b') * 2 + posisjoner('Knapp_b')),
                          (posisjoner('Vindu_h') - posisjoner('Marg_h') * 2 - posisjoner('Knapp_h') * 2))
        self.btn_createExample.move(posisjoner('Marg_b'),
                                    (posisjoner('Vindu_h') - posisjoner('Marg_h') - posisjoner('Knapp_h')))
        self.btn_doner.move((posisjoner('Marg_b') * 2 + posisjoner('Knapp_b')),
                            (posisjoner('Vindu_h') - posisjoner('Marg_h') - posisjoner('Knapp_h')))

        # Adding functions to buttons
        self.btn_doner.clicked.connect(self.clicked_Doner)
        self.btn_createExample.clicked.connect(self.predict_model)
        self.btn_calculateBallot.clicked.connect(self.clicked_run_count_votes)
        self.btn_FAQ.clicked.connect(self.clicked_FAQ)

        # Creating a progressbar to indicate
        # that a process is running
        self.progress = QtGui.QProgressBar(self)

        # Set max and min to zero: this make the progressbar
        # run even though it does not
        # know the length of the process
        self.progress.setMaximum(0)
        self.progress.setMinimum(0)

        # Set processbar size
        self.progress.setGeometry(350, 650, 500, 55)

        # Hide progress bar until it is needed
        self.progress.hide()

        # show all the buttons, gif and textedit fields
        # that has been created in this function
        self.show()

    def buttons_on(self):
        #Method to turn on buttons
        # after they have been disabled
        self.btn_calculateBallot.setEnabled(True)
        self.btn_FAQ.setEnabled(True)
        self.btn_createExample.setEnabled(True)

    def buttons_off(self):
        # Method to turn off buttons during a process
        self.btn_calculateBallot.setEnabled(False)
        self.btn_FAQ.setEnabled(False)
        self.btn_createExample.setEnabled(False)

    def open_about(self):
        # Opening messagebox with information
        choice = QtGui.QMessageBox.information(self, tekst('Menu3'), tekst('Menu3_text'), QtGui.QMessageBox.Ok)
        if choice == QtGui.QMessageBox.Ok:
            pass
        else:
            pass

    def open_help(self):
        # Opening messagebox with information
        choice = QtGui.QMessageBox.information(self, tekst('Menu2'), tekst('Menu2_text'), QtGui.QMessageBox.Ok)
        if choice == QtGui.QMessageBox.Ok:
            pass
        else:
            pass

    def clicked_FAQ(self):
        try:
            webbrowser.open(tekst('www_FAQ'))
            self.ui.actionFsa_format.triggered.connect(self.open_url)
            self.buttons_off()
        except:
            self.buttons_on()
            self.output_field.setText(tekst('Button3_error'))

    def clicked_Doner(self):
        try:
            webbrowser.open(tekst('www_Doner'))
            self.ui.actionFsa_format.triggered.connect(self.open_url)
            self.buttons_off()
        except:
            self.buttons_on()
            self.output_field.setText(tekst('Button4_error'))

    def clicked_run_count_votes(self):
        # .ckpt-fil
        file_name = ""
        iteration_number = 0
        self.output_field.setText(tekst('Button1_clicked'))

        # Creating buttons
        button_classification = QtGui.QPushButton("Classification")
        button_indent = QtGui.QPushButton("Indentation")
        button_cancel_model = QtGui.QPushButton("Cancel")
        button_inner = QtGui.QPushButton("Innerring")
        button_outer = QtGui.QPushButton("Outerring")
        button_ball = QtGui.QPushButton("Ball")
        button_base = QtGui.QPushButton("No damage")
        button_cancel = QtGui.QPushButton("Cancel")
        button_yes = QtGui.QPushButton("Yes")
        button_no = QtGui.QPushButton("No")

        # Creating Messageboxes for user input
        choose_model_msgBox = QtGui.QMessageBox()
        choose_model_msgBox.setWindowTitle("Choose model")
        choose_model_msgBox.setIcon(QMessageBox.Question)
        choose_model_msgBox.setText('Which model would you like to train?')

        choose_model_msgBox.setDetailedText("To define the size of the"
                                            " damage to the ball "
                                            "bearing it is necessary to "
                                            "use two models. Firstly the "
                                            "classification model to "
                                            "determine if there is a "
                                            "damage, and which type "
                                            "it is most likely to be. "
                                            "Secondly the indentation"
                                            " model to determine the "
                                            "size of the indentation.")

        class_msgBox = QtGui.QMessageBox()
        class_msgBox.setText('Where is the damage located?')
        class_msgBox.setIcon(QMessageBox.Question)

        class_msgBox.setDetailedText("To train a model each sets of"
                                     " features in csv-format needs"
                                     " to add a label so to know what"
                                     " the correct results of the "
                                     "training.Each csv-file added "
                                     "to thetraining of the model "
                                     "needs a label.\n\nIt is "
                                     "necessary to add data sets"
                                     " of all the types of cases "
                                     "the model should be able "
                                     "to predict.")

        class_msgBox.setWindowTitle("Classification model")
        add_files_msgBox = QtGui.QMessageBox()
        add_files_msgBox.setWindowTitle("Add files")
        add_files_msgBox.setIcon(QMessageBox.Question)
        add_files_msgBox.setText('Do you wish to add another set of files')

        add_files_msgBox.setDetailedText("To train a model that are able "
                                         "to recognise every type of "
                                         "damage in a ball bearing "
                                         "it will be necessary to at "
                                         "least supply one data set"
                                         " representing each type"
                                         " of damage, and one to represent"
                                         " the no-damage baseline.")

        # Adding icon
        class_msgBox.setWindowIcon(QtGui.QIcon('tf.jpg'))
        choose_model_msgBox.setWindowIcon(QtGui.QIcon('tf.jpg'))
        add_files_msgBox.setWindowIcon(QtGui.QIcon('tf.jpg'))

        # Adding buttons to the different messageboxes
        class_msgBox.addButton(button_inner, QtGui.QMessageBox.YesRole)
        class_msgBox.addButton(button_outer, QtGui.QMessageBox.YesRole)
        class_msgBox.addButton(button_ball, QtGui.QMessageBox.YesRole)
        class_msgBox.addButton(button_base, QtGui.QMessageBox.YesRole)
        class_msgBox.addButton(button_cancel, QtGui.QMessageBox.RejectRole)
        add_files_msgBox.addButton(button_yes, QtGui.QMessageBox.YesRole)
        add_files_msgBox.addButton(button_no, QtGui.QMessageBox.YesRole)
        choose_model_msgBox.addButton(button_classification,
                                      QtGui.QMessageBox.YesRole)
        choose_model_msgBox.addButton(button_indent,
                                      QtGui.QMessageBox.YesRole)
        choose_model_msgBox.addButton(button_cancel_model,
                                      QtGui.QMessageBox.YesRole)

        # Starting the messagebox
        choose_model_msgBox.exec_()
        # Try/Except in case of errors
        try:
            self.buttons_off()
            if choose_model_msgBox.clickedButton() == button_cancel_model:
                self.output_field.setText("TRAIN MODEL\n\nCancelled.")
                self.buttons_on()

            if choose_model_msgBox.clickedButton() == button_classification:
                continue_append = True
                self.output_field.append("\nClassification model chosen")

                while continue_append:

                    file = QtGui.QFileDialog.getOpenFileName(self, "Open "
                                                                   "CSV "
                                                                   "file"
                                                                    , " ",
                                                                    "*."
                                                                    "csv")
                    if file is "":
                        self.buttons_on()
                        break
                    else:
                        class_feature.append(file)
                    # initize  classification messagebox
                    class_msgBox.exec_()

                    if class_msgBox.clickedButton() == button_cancel:
                        self.progress.hide()
                        self.output_field.setText("TRAIN MODEL"
                                                  "\n\nCancelled")
                        # Cancel process and break from while loop
                        break
                    # initize add files messagebox
                    add_files_msgBox.exec_()
                    if add_files_msgBox.clickedButton() == button_no:
                        continue_append = False

                # show the progressbar
                self.progress.show()
                new_train_feature, new_train_label, new_test_feature, new_test_label, info_string = \
                    import_csv_for_classification(class_feature, class_label, batch_split_percent)

                # Showing what parameters are being used
                self.output_field.append(info_string)
                # Create save file
                file_name = QtGui.QFileDialog.getSaveFileName(self, 'Save'
                                                                    ' File'
                                                                    ,'',
                                                                    '*.'
                                                                    'ckpt')
                print(file_name)
                # Add all components to tuplet
                class_train_tuplet = new_train_feature, new_train_label, \
                                     new_test_feature, new_test_label,\
                                     class_gradient_length, \
                                     class_print_intermidiate_values_train,\
                                     class_print_intermidiate_values_test, \
                                     class_print_error_rate, class_print_graph,\
                                     file_name, iteration_number, \
                                     class_new_file
                reset_tf()

                self.output_field.append("Training process started:"
                                         "\nThis can take minutes, hours "
                                         "or even days depending "
                                         "on your setup")
                show_result = train_model_classification(class_train_tuplet)
                self.output_field.append(show_result)
                self.buttons_on()
                self.progress.hide()

            elif choose_model_msgBox.clickedButton() == button_indent:
                continue_append = True
                self.output_field.append("\nIndentation model chosen")

                # While method to add more files
                # to the training process
                while continue_append:

                    file = QtGui.QFileDialog.getOpenFileName(self, "Open "
                                                                   "CSV "
                                                                   "file"
                                                                    ," ",
                                                                    "*."
                                                                    "csv")
                    if file is "":
                        self.buttons_on()
                        break
                    else:
                        indent_feature.append(file)
                    num, ok = QInputDialog.getDouble(self, "Damage", "Enter indent in millimeters", 0.0000, 0, 1000, 4)

                    if ok:
                        indent_label.append([num])
                        # intiate add files messagebox
                        add_files_msgBox.exec_()
                    else:
                        break

                    if add_files_msgBox.clickedButton() == button_no:
                        continue_append = False

                # Show the progressbar
                self.progress.show()

                new_train_feature, new_train_label, new_test_feature,\
                new_test_label, info_string =\
                    import_csv_for_indent(indent_feature,
                                          indent_label,
                                          batch_split_percent)

                self.output_field.append(info_string)
                self.output_field.append("Training process started:"
                                         "\nThis can take minutes or"
                                         " hours depending on your setup.")
                file_name = QtGui.QFileDialog.getSaveFileName(self, 'Save '
                                                                    'File'
                                                                     , '',
                                                                    '*.'
                                                                    'ckpt')
                indent_train_tuplet = new_train_feature, new_train_label,\
                                      new_test_feature, new_test_label,\
                                      indent_gradient_length,\
                                      indent_print_intermidiate_values_train,\
                                      indent_print_intermidiate_values_test,\
                                      indent_print_error_rate,\
                                      indent_print_graph, \
                                      file_name, iteration_number, \
                                      indent_new_file


                reset_tf()

                show_result = train_model_indent(indent_train_tuplet)

                # Hide progressbar, show result of training
                # and enable buttons
                self.output_field.append(show_result)

                self.progress.hide()
                self.buttons_on()

        except:
            # Exception that activates the buttons,
            # hides the progressbar
            # and resets the output text
            self.buttons_on()
            self.output_field.setText("TRAIN MODEL\n\nCancelled")
            self.progress.hide()

    def predict_model(self):

        # Creating messagebox for input
        predict_model_msgBox = QtGui.QMessageBox()
        predict_model_msgBox.setWindowTitle("Choose model")
        predict_model_msgBox.setIcon(QMessageBox.Question)
        predict_model_msgBox.setText('Which model would you like to '
                                     'prediction?')

        # Creating buttons
        predict_classification_btn = QtGui.QPushButton("Classification")
        predict_indent_btn = QtGui.QPushButton("Indentation")
        predict_cancel_model_btn = QtGui.QPushButton("Cancel")

        # Adding the buttons to predict_model_msgbox
        predict_model_msgBox.addButton(predict_classification_btn,
                                       QtGui.QMessageBox.YesRole)
        predict_model_msgBox.addButton(predict_indent_btn,
                                       QtGui.QMessageBox.YesRole)
        predict_model_msgBox.addButton(predict_cancel_model_btn,
                                       QtGui.QMessageBox.YesRole)
        predict_model_msgBox.setDetailedText("It is necessary to already"
                                             " have trained a model"
                                             " to use one.")

        # Set icon
        predict_model_msgBox.setWindowIcon(QtGui.QIcon('tf.jpg'))

        # Try/Except in case of errors
        try:
            self.buttons_off()
            self.output_field.setText("PREDICT\n\nPlease select CKPT file"
                                      " and CSV file for prediction.")
            predict_model_msgBox.exec_()
            if predict_model_msgBox.clickedButton() == predict_classification_btn:

                class_model_name = QtGui.QFileDialog.getOpenFileName(self, 'Open CKPT File' , '' ,'(*.meta)(*.index)(*.data-00000-of-00001)')
                # Redudancy: Is covered by class_model_name QFileDialog
                if class_model_name is "":
                    self.buttons_on()
                    raise Exception
                elif class_model_name.endswith('.meta'):
                    class_model_name = class_model_name[:-5]
                elif class_model_name.endswith('.index'):
                    class_model_name = class_model_name[:-6]
                elif class_model_name.endswith('.data-00000-of-00001'):
                    class_model_name = class_model_name[:-20]
                print(class_model_name)
                class_pred_file = QtGui.QFileDialog.getOpenFileName(self,
                                                                    'Open '
                                                                    'CSV '
                                                                    'File'
                                                                    , '',
                                                                    '(*.'
                                                                    'csv)')
                if class_pred_file is "":
                    self.buttons_on()
                    raise Exception
                self.progress.show()

                print("Creating label shape")
                class_model_label_shape = []
                class_model_label_shape.append(
                    [0, 0, 0, 0])  # The values is not important
                                   # but it needs to represent
                                   # the shape of the labels.

                print("Running CSV -> array")
                newBatch_feat, info_string = \
                    import_csv_to_predict_classification(class_pred_file)
                self.output_field.append(info_string)


                print("Creating tuplet for prediction")
                class_predict_tuplet = \
                    newBatch_feat, class_model_label_shape,\
                    class_model_name

                print("Reset TF")
                reset_tf()

                print("Running prediction")
                result_string = \
                    predict_classification(class_predict_tuplet)
                print("Shows results of prediction")
                # Hide progressbar, show result of training
                # and enable buttons
                self.progress.hide()
                self.output_field.append(result_string)
                self.buttons_on()
            elif predict_model_msgBox.clickedButton() == predict_indent_btn:

                indent_model_name = QtGui.QFileDialog.getOpenFileName(self, 'Open CKPT File', '','(*.meta)(*.index)(*.data-00000-of-00001)')
                if indent_model_name is "":
                    self.buttons_on()
                    raise Exception
                elif indent_model_name.endswith('.meta'):
                    indent_model_name = indent_model_name[:-5]
                elif indent_model_name.endswith('.index'):
                    indent_model_name = indent_model_name[:-6]
                elif indent_model_name.endswith('.data-00000-of-00001'):
                    indent_model_name = indent_model_name[:-20]
                class_pred_file = QtGui.QFileDialog.getOpenFileName(self,
                                                                    'Open '
                                                                    'CSV '
                                                                    'File'
                                                                    , '',
                                                                    '(*.'
                                                                    'csv)')
                if class_pred_file is "":
                    self.buttons_on()
                    raise Exception

                self.progress.show()
                indent_predict_tuplet = []
                indent_model_label_shape = []
                indent_model_label_shape.append(
                    [0])  # The values is not important
                          # but it needs to represent
                          # the shape of the labels.

                newBatch_feat, info_string = \
                    import_csv_to_predict_classification(class_pred_file)
                self.output_field.append(info_string)

                indent_predict_tuplet = newBatch_feat\
                    , indent_model_label_shape, indent_model_name
                reset_tf()
                result_string = predict_indent(indent_predict_tuplet)

                self.progress.hide()
                self.output_field.append(result_string)
                self.buttons_on()

            elif predict_model_msgBox.clickedButton() == predict_cancel_model_btn:
                self.buttons_on()
                self.output_field.setText("PREDICT\n\nCancelled.")

        except:
            self.buttons_on()
            self.output_field.setText("PREDICT\n\nCancelled.")
            self.output_field.append("\nDid you select the correct file?")
            self.progress.hide()

    def convert_clicked(self):
        # Using try in case user types in unknown file
        # or closes without choosing a file.
        try:
            self.buttons_off()
            self.output_field.setText("CONVERT .TXT TO .CSV")
            self.output_field.append("\nChoose .txt-file to convert.")
            name_input_txt = QtGui.QFileDialog.getOpenFileName(self,
                                                               'Open '
                                                               'text '
                                                               'file'
                                                               , ' ',
                                                               '*.txt')

            # Checking if there is a file
            if name_input_txt is "":
                raise Exception
            print(name_input_txt)
            self.output_field.append("\nName the .csv-file and where "
                                     "to save it.")
            name_output_csv = QtGui.QFileDialog.getSaveFileName(self,
                                                                'Save '
                                                                'File'
                                                                , '',
                                                                '*.csv')

            # Checking if there is a file
            if name_output_csv is "":
                raise Exception
            self.output_field.append("\n\nStarting convertion...\n\nThis "
                                     "may take a while, given the size "
                                     "of the .txt-file.")
            self.progress.show()

            # Number of features can be adjusted
            # 500 is the optimized size for our program
            number_of_features = 500
            show_result = convert_txt_to_csv(number_of_features,
                                             name_input_txt,
                                             name_output_csv)
            self.output_field.setText(show_result)
            self.progress.hide()
            self.buttons_on()
        except:
            self.progress.hide()
            self.buttons_on()
            self.output_field.setText("CONVERT .TXT TO .CSV\n\nError,"
                                      " did you select a file?"
                                      "\nPlease try again.\n\n"
                                      "Remember you can only "
                                      "select .txt-formated files.")

    def close_application(self):
        exit_program = QtGui.QMessageBox.question(self,
                                                  'Exit'
                                                  ,
                                                  "Are you "
                                                  "sure you"
                                                  " want to"
                                                  " quit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if exit_program == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

# Running the GUI
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()