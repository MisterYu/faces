import collections


class MorseCodeDecoder():
    eye_states_2_words = {
        'C'*3: '.',
        'C'*4: '.',
        'C'*5: '_',
        'C'*6: '_',
        'C'*7: '_',
        'O'*3: ' ',
        'O'*4: ' ',
        'O'*5: ' ',
        'O'*6: '  ',
    }
    valid_eye_states = eye_states_2_words.keys()

    words_2_char = {}
    words_2_char = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '  ': ' ',
        ' ': '',
    }
    valid_word_buffers = words_2_char.keys()

    def __init__(self):
        '''
        structure to track consecutive eye state
        state can be:
            open - both eyes open
            closed - single or both eyes closed
        '''
        self.eye_states = ''

        '''
        structure to track consecutive word state
        word can be:
            dot: 3-4 counts of closed eyes
            dash: 5-7 counts of closed eyes
            short space: 3-5 counts of open eyes
            long space: at least 6 counts of open eyes
        '''
        self.word_buffer = ''
        self.char_buffer_max = 40
        self.char_buffer = collections.deque()

    def update_state(self, n_eyes_open):
        # determine state of eyes
        eye_state = 'O' if n_eyes_open == 2 else 'C'

        # only do lots of processing if pre-existing eye state
        if self.eye_states:
            # append current eye state to previous ones
            next_eye_states = self.eye_states + eye_state

            # init to nothing
            next_word = ''

            # check if current is good and next is not
            if self.eye_states in self.valid_eye_states \
                    and next_eye_states not in self.valid_eye_states:
                next_word = self.eye_states_2_words[self.eye_states]
                # reset
                self.eye_states = eye_state

            # if next eye state not homogenous then reset
            elif self.eye_states[-1] != eye_state:
                self.eye_states = eye_state

            # next state is legit and becomes current
            else:
                self.eye_states = next_eye_states
            next_word_buffer = self.word_buffer + next_word

            # check for white spaces 1st
            if next_word in ['  ', ' ']:
                if self.word_buffer in self.valid_word_buffers:
                    self.char_buffer.append(self.words_2_char[self.word_buffer])
                self.char_buffer.append(self.words_2_char[next_word])
                self.word_buffer = ''
            elif self.word_buffer in self.valid_word_buffers \
                    and next_word_buffer not in self.valid_word_buffers:
                self.char_buffer.append(self.words_2_char[next_word])
                self.word_buffer = next_word
            else:
                self.word_buffer = next_word_buffer

        # init
        else:
            self.eye_states = eye_state

    def char_buffer_append(self, char):
        if char:
            if len(self.char_buffer) == self.char_buffer_max:
                self.char_buffer.popleft()
            self.char_buffer.append(char)

    def get_char_buffer(self):
        string = ''.join(list(self.char_buffer))
        return string
