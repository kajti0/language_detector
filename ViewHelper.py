from LangPredict import LangPredict
import PySimpleGUI as sg


class ViewHelper:
    layout = [
        [sg.Text('Wprowadź tekst do rozpoznania języka:')],
        [sg.InputText(key='-INPUT-', size=(30, 1))],
        [sg.Button('Metoda wbudowana'), sg.Button('Metoda autorska'), sg.Button('Wyjście')],
        [sg.Text(size=(50, 1), key='-OUTPUT-')],
    ]

    def __init__(self):
        self.lang = LangPredict()

    def view(self):
        window = sg.Window('Rozpoznawanie Języka', self.layout)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Wyjście'):
                break

            if event == 'Metoda wbudowana':
                input_text = values['-INPUT-']
                label, probability = self.lang.predict_language(input_text, "../lid.176.bin")
                window['-OUTPUT-'].update(
                    f'Przewidziany język: {label}, Prawdopodobieństwo: {"{:.0%}".format(probability)}')

            if event == 'Metoda autorska':
                input_text = values['-INPUT-']
                label, probability = self.lang.predict_language(input_text, "../model.bin")
                window['-OUTPUT-'].update(
                    f'Przewidziany język: {label}, Prawdopodobieństwo: {"{:.0%}".format(probability)}')

        window.close()
