#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


# Colors
RED = 'r'
BLUE = 'b'
GREEN = 'g'
YELLOW = 'y'
BLACK = 'x'

COLORS = (RED, BLUE, GREEN, YELLOW)

COLOR_ICONS = {
    RED: '❤️',
    BLUE: '💙',
    GREEN: '💚',
    YELLOW: '💛',
    BLACK: '⬛️'
}

# Values
ZERO = '0'
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
DRAW_TWO = 'draw'
REVERSE = 'reverse'
SKIP = 'skip'

VALUES = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, DRAW_TWO,
          REVERSE, SKIP)
WILD_VALUES = (ONE, TWO, THREE, FOUR, FIVE, DRAW_TWO, REVERSE, SKIP)

# Special cards
CHOOSE = 'colorchooser'
DRAW_FOUR = 'draw_four'

SPECIALS = (CHOOSE, DRAW_FOUR)

CARDS_CLASSIC = {
    "normal": {
        "colorchooser": "CAADAQADXwMAAvxXkEQfpNkhezM1twI",
        "draw_four": "CAADAQADJgUAAsLpkURpUokNa-HdAQI",
        "r_0": "CAADAQADXgMAAojdkEQAAYBMa491ooIC",
        "r_1": "CAADAQAD1AQAAnURiUSq51C6MX0jcQI",
        "r_2": "CAADAQADvAMAAh7RkURZ60vakGuePgI",
        "r_3": "CAADAQADMQMAAht-kESgeFYTyYZRkwI",
        "r_4": "CAADAQADNAQAAmSVkUSQGhxm0IulGgI",
        "r_5": "CAADAQADkwMAAsCJkUS0EZNUuz2HRwI",
        "r_6": "CAADAQAD5AIAAsxFkET63Z-eWXO4YwI",
        "r_7": "CAADAQADqgMAAofLkERWFD6789hjYgI",
        "r_8": "CAADAQADfwMAAuoIkUSb-T-_DEPgNwI",
        "r_9": "CAADAQAD-AQAAuGYkETGBw9-KB4OhwI",
        "r_draw": "CAADAQAD9AMAAodikUSXZ7Nes-194wI",
        "r_reverse": "CAADAQADDwUAAvGSkERQEa-k7TfrCgI",
        "r_skip": "CAADAQADpgQAAhbokERI4oXPiK9fEwI",
        "g_0": "CAADAQADLQQAAi2GkER5uw1YBDec9QI",
        "g_1": "CAADAQAD8AIAAv1RkUQVc3m3vw3VRQI",
        "g_2": "CAADAQADPAUAAhW_kEQ9ZqmejI9IiwI",
        "g_3": "CAADAQADIwQAAmcekETHojKy-TF2gwI",
        "g_4": "CAADAQADkwMAAk1skEQ261fb-vE8WAI",
        "g_5": "CAADAQADhgMAAq5JkETU7zznShMdGAI",
        "g_6": "CAADAQADIQUAAp3MkUSXeE14w3zYAgI",
        "g_7": "CAADAQAD4wQAAlAgkES3roTFKmnW8gI",
        "g_8": "CAADAQADUgMAAlQwkEQ68toeSsl3vQI",
        "g_9": "CAADAQADIwYAAvAkkUSyucn14QF-TAI",
        "g_draw": "CAADAQADbwMAApzLkES_59GHthWWVwI",
        "g_reverse": "CAADAQADbQMAAnw3kUQ_krn7N5JXbAI",
        "g_skip": "CAADAQADHQMAAthokUSTAAFO53o_Cg8C",
        "b_0": "CAADAQADRAQAAnDhkESjSZ_RNk4-6wI",
        "b_1": "CAADAQADWAMAAmWUkURVHi_4lQ84lwI",
        "b_2": "CAADAQADuQQAAgefkUS_yW5B0HwB8AI",
        "b_3": "CAADAQADqwMAAhKTkEQPB5r0v7QDcQI",
        "b_4": "CAADAQADEAMAAoY5kETca_cGhj-jdwI",
        "b_5": "CAADAQAD_wIAApfOkEQyctaU-FgYCgI",
        "b_6": "CAADAQADGwMAAqe5kUTq-C8AASYHByUC",
        "b_7": "CAADAQAD2gMAAusTkERKgxfo54_siQI",
        "b_8": "CAADAQAD3wMAAvaMkERreUrlpEgygQI",
        "b_9": "CAADAQADYgMAAp7YkUTbdRsfrX8qkwI",
        "b_draw": "CAADAQADegMAAvEHkETEgGLeWitkwgI",
        "b_reverse": "CAADAQADnAQAAllBkUQeRyeaVu00EAI",
        "b_skip": "CAADAQADqQMAAlKSkESO-4guU6WIBgI",
        "y_0": "CAADAQADFwQAAoELkEREuUz4w7qgIAI",
        "y_1": "CAADAQADrwMAAqE0kEQx_6iSYCwxFQI",
        "y_2": "CAADAQADKAMAAqdfiEStdEG2aYSz-gI",
        "y_3": "CAADAQADWQMAAu61iUTfWNu8QTH-MwI",
        "y_4": "CAADAQADQwQAAi6ciUSVUakVdNhI1AI",
        "y_5": "CAADAQADvAYAAoeGkUTbB4rMaMUhLwI",
        "y_6": "CAADAQADKwMAAmYjiUQuGOVZNAvANQI",
        "y_7": "CAADAQADKAMAAs2ekEQWYT1GZuCFIgI",
        "y_8": "CAADAQAD8QMAAoPFkESOXt-HgW6CNAI",
        "y_9": "CAADAQADBgQAAvbzkEQmO5Pu_K1bOQI",
        "y_draw": "CAADAQADmQMAAh3pkER0L_YlsoXGOwI",
        "y_reverse": "CAADAQADvgQAArPLiESZkhlqkOPr7QI",
        "y_skip": "CAADAQADVQMAAoHEkEQlv-zoSTeQpgI"
    },
    "not_playable": {
        "colorchooser": "CAADAQADDQQAAsJvkERJ3INjeAABL5wC",
        "draw_four": "CAADAQAD1gMAAmxHkUR7qbMs4LLtZQI",
        "r_0": "CAADAQADNAMAAvz7kURL7c0gBa8NsAI",
        "r_1": "CAADAQADuQMAAkaQkURMpD-VfVmK4QI",
        "r_2": "CAADAQAD7wMAAjPOkETdIk31mQABRp8C",
        "r_3": "CAADAQADXwMAAjcakUTKhLXGkCoDdQI",
        "r_4": "CAADAQADXwMAAjrukESLvaHKb7tcUgI",
        "r_5": "CAADAQADKAMAAkAAAZFERit1t3jyQOUC",
        "r_6": "CAADAQADYwMAAmKMkET-1aZt2MYUtQI",
        "r_7": "CAADAQADBwQAAnhIiET3lQ0jmJdzBQI",
        "r_8": "CAADAQAD1QUAArz_kUS-LHZXUCRR2AI",
        "r_9": "CAADAQADVQMAAlpSkUTeAAHOkYh7Hz4C",
        "r_draw": "CAADAQAD_wMAAnZmkETvG1-sEyd_6AI",
        "r_reverse": "CAADAQADuAQAArzGiUQrl8xU7pLgTgI",
        "r_skip": "CAADAQADVgMAAgICkETGYLcMSb4MQAI",
        "g_0": "CAADAQADkAMAAif2kUQrZX85Q0TJwgI",
        "g_1": "CAADAQADUgMAAsS1iUSO00FwpL6rDgI",
        "g_2": "CAADAQADdQQAAsbCkUR1_FE7lJDqXwI",
        "g_3": "CAADAQADhgMAAnzhkUT7jFvErAOpiAI",
        "g_4": "CAADAQADRwQAAvTGiUTDjiWsWWBsRwI",
        "g_5": "CAADAQAD8QIAAuzBkET3vLxIdiMMawI",
        "g_6": "CAADAQADJgQAAjAkkUQbligD2up8GgI",
        "g_7": "CAADAQADBwQAAoNukERqR98ZLvGFGAI",
        "g_8": "CAADAQAD_wMAAu-NiEQ00qFh4fR6bgI",
        "g_9": "CAADAQADpwMAAoUUkETQRGyFOPU51wI",
        "g_draw": "CAADAQADDwMAAgtdkETH7FQlKmoVlQI",
        "g_reverse": "CAADAQADUwQAAi2dkET6JOXm4_0J8wI",
        "g_skip": "CAADAQADigMAAvBdkUQi8ZXHrozc3AI",
        "b_0": "CAADAQADpQQAAriVkEQW1wAB_u5eq7wC",
        "b_1": "CAADAQADpwMAAqDRkETxJh6vtp3thQI",
        "b_2": "CAADAQADowMAAqotkEQF0btgxhsYygI",
        "b_3": "CAADAQADyQMAAkV2kETjukOZUYqbcwI",
        "b_4": "CAADAQADRAMAAnNOkEQ9c4D9GTuD4gI",
        "b_5": "CAADAQADQwUAAtgPkUQSp_19qeFQiAI",
        "b_6": "CAADAQADcgMAAp8nkESvuPuTgSM5wAI",
        "b_7": "CAADAQADEQQAAp5dkUR-pPhZKBxUMQI",
        "b_8": "CAADAQADygMAAmXmkUQKui9gyw_qFwI",
        "b_9": "CAADAQADJwMAAhqSkER8M2KrY0qr3AI",
        "b_draw": "CAADAQADxgIAAglIkEQPtCrpY3ttNQI",
        "b_reverse": "CAADAQADtAMAArm3kESF8qV9yyHU0wI",
        "b_skip": "CAADAQADtQMAAsBqkES8m63c60Zf0gI",
        "y_0": "CAADAQADTwQAAg1-kUTbmyS-MDq_9wI",
        "y_1": "CAADAQADVQQAAgQakETNlQPcMV7AdwI",
        "y_2": "CAADAQADxQIAAjVXiERk7iQzf9GSIAI",
        "y_3": "CAADAQADBwYAAl7vkERpCmLqSViTowI",
        "y_4": "CAADAQAD-wMAAsnHkUQrU06IT6wY_QI",
        "y_5": "CAADAQADRAUAAh9OkUSsjZ62THankQI",
        "y_6": "CAADAQADcwcAAuD3kURQmN79D2YnUwI",
        "y_7": "CAADAQADNQUAAodykETF-zfJiQ-vOgI",
        "y_8": "CAADAQADEgQAAmbhkUS4e6ao9DQWPQI",
        "y_9": "CAADAQADUQMAArO6iESu4pCFrjnr3wI",
        "y_draw": "CAADAQADMAMAApBvkEThlZG9WyU8RQI",
        "y_reverse": "CAADAQADvwMAArArkEQp3__TSzCG2gI",
        "y_skip": "CAADAQADIAQAAlUZkURqji4r61DTbQI"
    },
}

CARDS_CLASSIC_COLORBLIND = CARDS_CLASSIC

STICKERS_OPTIONS = {
    "option_bluff": "CAADAQADOwQAAtfQkUTtAUFL5rYIiwI",
    "option_draw": "CAADAQADogMAAl8zkUQy-U5Cbyvp_AI",
    "option_info": "CAADAQADvwMAAj8WkETNbU9oas-uAwI",
    "option_pass": "CAADAQADXwMAApsVkEQrsmFsDCZVdAI"
}

# TODO: Support multiple card packs
# For now, just use classic colorblind
STICKERS = {
    **CARDS_CLASSIC_COLORBLIND["normal"],
    **STICKERS_OPTIONS,
}

STICKERS_GREY = {
    **CARDS_CLASSIC_COLORBLIND["not_playable"],
}


class Card(object):
    """This class represents an UNO card"""

    def __init__(self, color, value, special=None):
        self.color = color
        self.value = value
        self.special = special

    def __str__(self):
        if self.special:
            return self.special
        else:
            return '%s_%s' % (self.color, self.value)

    def __repr__(self):
        if self.special:
            return '%s%s%s' % (COLOR_ICONS.get(self.color, ''),
                               COLOR_ICONS[BLACK],
                               ' '.join([s.capitalize()
                                         for s in self.special.split('_')]))
        else:
            return '%s%s' % (COLOR_ICONS[self.color], self.value.capitalize())

    def __eq__(self, other):
        """Needed for sorting the cards"""
        return str(self) == str(other)

    def __lt__(self, other):
        """Needed for sorting the cards"""
        return str(self) < str(other)


def from_str(string):
    """Decodes a Card object from a string"""
    if string not in SPECIALS:
        color, value = string.split('_')
        return Card(color, value)
    else:
        return Card(None, None, string)
